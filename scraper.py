#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WooCommerce Documentation Scraper
Fetches WooCommerce documentation pages and saves them as Markdown files.
"""

import os
import re
import time
import random
import json
import argparse
import hashlib
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup


class WooCommerceDocScraper:
    """Scraper for WooCommerce documentation."""
    
    BASE_URL = "https://woocommerce.com/documentation/woocommerce/"
    DOCS_DIR = "docs/en"
    IMAGES_DIR = "docs/images"
    METADATA_FILE = "metadata.json"
    WP_EXPORT_FILE = "wp_export.json"
    
    def __init__(self, max_pages=None):
        """Initialize the scraper."""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.visited_urls = set()
        self.metadata = {}
        self.request_delay = 2.5
        self.request_jitter = 1.5
        self.max_retries = 4
        self.last_request_at = 0.0
        self.max_pages = max_pages
        self.pages_scraped = 0
        self.images_metadata = {}  # Track downloaded images
        
    def sanitize_filename(self, text):
        """Convert text to a safe filename."""
        # Remove or replace invalid characters
        text = re.sub(r'[<>:"/\\|?*]', '', text)
        text = re.sub(r'\s+', '-', text)
        text = text.strip('-').lower()
        return text[:200]  # Limit length

    def normalize_url(self, url):
        """Normalize a URL for consistent deduplication."""
        parsed = urlparse(url)
        clean_path = parsed.path
        if clean_path and not clean_path.endswith('/'):
            clean_path = f"{clean_path}/"
        return f"{parsed.scheme}://{parsed.netloc}{clean_path}"

    def download_image(self, img_url, page_url, alt_text='', context=''):
        """Download an image and return local path with metadata."""
        try:
            # Create images directory
            images_dir = Path(self.IMAGES_DIR)
            images_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate filename from URL hash to avoid duplicates
            url_hash = hashlib.md5(img_url.encode()).hexdigest()
            parsed = urlparse(img_url)
            ext = Path(parsed.path).suffix or '.jpg'
            filename = f"{url_hash}{ext}"
            filepath = images_dir / filename
            
            # Check if image metadata already exists
            if img_url in self.images_metadata:
                existing = self.images_metadata[img_url]
                # Add new context if different page
                if page_url not in existing.get('used_on_pages', []):
                    existing.setdefault('used_on_pages', []).append(page_url)
                    existing.setdefault('contexts', []).append({'page': page_url, 'alt': alt_text, 'context': context})
                return str(filepath), filename
            
            # Skip download if file exists
            if not filepath.exists():
                # Download image with throttling
                elapsed = time.time() - self.last_request_at
                min_wait = self.request_delay + random.uniform(0, self.request_jitter)
                if elapsed < min_wait:
                    time.sleep(min_wait - elapsed)
                
                print(f"Downloading image: {img_url}")
                response = self.session.get(img_url, timeout=30, stream=True)
                self.last_request_at = time.time()
                response.raise_for_status()
                
                # Save image
                with open(filepath, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                print(f"Saved image: {filepath}")
            
            # Store metadata with context
            self.images_metadata[img_url] = {
                'local_path': str(filepath),
                'filename': filename,
                'source_url': img_url,
                'used_on_pages': [page_url],
                'contexts': [{
                    'page': page_url,
                    'alt': alt_text,
                    'context': context  # Surrounding text for positioning
                }]
            }
            
            return str(filepath), filename
            
        except Exception as e:
            print(f"Error downloading image {img_url}: {e}")
            return None, None
    
    def slug_from_url(self, url):
        """Derive a stable slug from a URL path."""
        path_parts = [p for p in urlparse(url).path.split('/') if p]
        if not path_parts:
            return "index"
        return self.sanitize_filename(path_parts[-1]) or "index"

    def build_slug_path(self, url):
        """Build a stable slug path from the URL path."""
        path_parts = [p for p in urlparse(url).path.split('/') if p]
        start = 0
        if 'documentation' in path_parts:
            start = path_parts.index('documentation') + 1
        if start < len(path_parts) and path_parts[start] == 'woocommerce':
            start += 1
        elif start < len(path_parts) and path_parts[start] == 'document':
            start += 1

        slug_parts = [self.sanitize_filename(p) for p in path_parts[start:]]
        slug_parts = [p for p in slug_parts if p]
        return '/'.join(slug_parts) if slug_parts else ""
    
    def get_page_content(self, url):
        """Fetch and parse a documentation page."""
        # Throttle requests to avoid looking like a bot.
        elapsed = time.time() - self.last_request_at
        min_wait = self.request_delay + random.uniform(0, self.request_jitter)
        if elapsed < min_wait:
            time.sleep(min_wait - elapsed)

        attempt = 0
        backoff = 2.0
        try:
            while attempt <= self.max_retries:
                print(f"Fetching: {url} (attempt {attempt + 1})")
                response = self.session.get(url, timeout=30)
                self.last_request_at = time.time()

                if response.status_code == 429 or 500 <= response.status_code < 600:
                    retry_after = response.headers.get('Retry-After')
                    wait_seconds = float(retry_after) if retry_after and retry_after.isdigit() else backoff
                    print(f"Retrying after {wait_seconds:.1f}s due to {response.status_code}...")
                    time.sleep(wait_seconds + random.uniform(0, 1.0))
                    backoff *= 2
                    attempt += 1
                    continue

                response.raise_for_status()
                return BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_content(self, soup, url):
        """Extract main content from the page."""
        if not soup:
            return None
        
        # Find the main content area
        # WooCommerce documentation typically uses article or main tags
        content_area = (
            soup.find('article') or 
            soup.find('main') or 
            soup.find('div', class_=re.compile(r'content|documentation|entry'))
        )
        
        if not content_area:
            print(f"Could not find content area for {url}")
            return None
        
        # Extract title
        title_tag = (
            content_area.find('h1') or 
            soup.find('h1') or 
            soup.find('title')
        )
        title = title_tag.get_text().strip() if title_tag else "Untitled"

        breadcrumb = self.extract_breadcrumb(soup, url)
        
        # Convert HTML to Markdown
        markdown_content = self.html_to_markdown(content_area, url)
        
        # Generate clean HTML for WordPress
        html_content = self.html_to_clean_html(content_area, url)
        
        return {
            'title': title,
            'content': markdown_content,
            'html_content': html_content,
            'url': url,
            'breadcrumb': breadcrumb
        }
    
    def html_to_markdown(self, element, base_url):
        """Convert HTML element to Markdown preserving structure."""
        self._h1_count = 0  # Track H1 headings to avoid multiple top-level headings
        markdown = self._process_element_to_markdown(element, base_url)
        # Remove multiple consecutive blank lines (MD012)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        return markdown
    
    def _process_element_to_markdown(self, element, base_url, depth=0):
        """Recursively process HTML elements to Markdown."""
        if not element:
            return ""
        
        lines = []
        
        for child in element.children:
            if isinstance(child, str):
                text = re.sub(r'\s+', ' ', child).strip()  # Normalize whitespace
                if text and depth == 0:  # Only add standalone text at top level
                    lines.append(text)
                continue
            
            if not hasattr(child, 'name'):
                continue
            
            tag = child.name
            
            # Headings
            if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(tag[1])
                text = re.sub(r'\s+', ' ', child.get_text()).strip()  # Normalize whitespace
                if text:  # Only add non-empty headings
                    # Skip first H1 (duplicate of frontmatter title) or convert subsequent H1s to H2
                    if level == 1:
                        self._h1_count += 1
                        if self._h1_count == 1:
                            # Skip first H1 as it duplicates the frontmatter title
                            continue
                        else:
                            # Convert subsequent H1s to H2
                            level = 2
                    lines.append(f"{'#' * level} {text}\n")
            
            # Paragraphs
            elif tag == 'p':
                text = self._process_inline_elements(child, base_url)
                text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
                if text:
                    lines.append(f"{text}\n")
            
            # Lists
            elif tag == 'ul':
                list_content = self._process_list(child, base_url, ordered=False)
                if list_content.strip():
                    lines.append(list_content)
            elif tag == 'ol':
                list_content = self._process_list(child, base_url, ordered=True)
                if list_content.strip():
                    lines.append(list_content)
            
            # Code blocks
            elif tag == 'pre':
                code_tag = child.find('code')
                code = code_tag.get_text() if code_tag else child.get_text()
                lang = ''
                if code_tag and code_tag.get('class'):
                    classes = code_tag['class']
                    for cls in classes:
                        if cls.startswith('language-'):
                            lang = cls.replace('language-', '')
                            break
                lines.append(f"\n```{lang}\n{code.rstrip()}\n```\n")
            
            # Blockquotes
            elif tag == 'blockquote':
                inner = self._process_element_to_markdown(child, base_url, depth + 1)
                if inner.strip():
                    quoted = '\n'.join(f"> {line}" for line in inner.split('\n') if line.strip())
                    lines.append(f"{quoted}\n")
            
            # Tables
            elif tag == 'table':
                table_content = self._process_table(child)
                if table_content.strip():
                    lines.append(table_content)
            
            # Images
            elif tag == 'img':
                src = child.get('src', '')
                alt = child.get('alt', '')
                
                # If alt is empty, try to get from title or aria-label
                if not alt:
                    alt = child.get('title', '') or child.get('aria-label', '')
                
                if src:
                    full_src = urljoin(base_url, src)
                    # Get surrounding context for image positioning
                    context = self._get_image_context(child)
                    
                    # If still no alt text, generate from context
                    if not alt and context:
                        # Extract text from context, removing markers like [Preceding:]
                        clean_context = re.sub(r'\[.*?:\s*', '', context)
                        clean_context = re.sub(r'\]', '', clean_context)
                        # Use first meaningful sentence (up to 100 chars)
                        alt = clean_context.split('.')[0].strip()[:100]
                    
                    # If still empty, use filename without extension
                    if not alt:
                        from pathlib import Path
                        alt = Path(urlparse(full_src).path).stem
                    
                    # Download image and get local path
                    local_path, filename = self.download_image(full_src, base_url, alt, context)
                    if local_path:
                        # Use local path in Markdown with placeholder that includes source URL
                        lines.append(f"![{alt}]({local_path} \"{full_src}\")\n")
                    else:
                        # Fallback to original URL if download fails
                        lines.append(f"![{alt}]({full_src})\n")
            
            # Divs and other containers - recurse
            elif tag in ['div', 'section', 'article', 'aside']:
                container_content = self._process_element_to_markdown(child, base_url, depth + 1)
                if container_content.strip():
                    lines.append(container_content)
        
        return '\n'.join(lines)
    
    def _get_image_context(self, img_element):
        """Get surrounding text context for an image."""
        context_parts = []
        
        # Get figcaption if exists
        figure = img_element.find_parent('figure')
        if figure:
            figcaption = figure.find('figcaption')
            if figcaption:
                caption = re.sub(r'\s+', ' ', figcaption.get_text()).strip()
                context_parts.append(f"[Caption: {caption}]")
        
        # Get parent element text before image
        parent = img_element.parent
        if parent:
            for sibling in parent.children:
                if sibling == img_element:
                    break
                if isinstance(sibling, str):
                    text = re.sub(r'\s+', ' ', sibling).strip()
                    if text:
                        context_parts.append(text)
                elif hasattr(sibling, 'get_text'):
                    text = re.sub(r'\s+', ' ', sibling.get_text()).strip()
                    if text:
                        context_parts.append(text)
        
        # If no context found yet, walk up the tree to find preceding paragraph
        if not context_parts:
            current = img_element
            for _ in range(5):  # Walk up max 5 levels
                if current.parent:
                    current = current.parent
                    # Look for preceding sibling paragraph
                    for sibling in current.previous_siblings:
                        if hasattr(sibling, 'name'):
                            if sibling.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                                text = re.sub(r'\s+', ' ', sibling.get_text()).strip()
                                if text:
                                    context_parts.append(f"[Preceding: {text}]")
                                    break
                        if context_parts:
                            break
                if context_parts:
                    break
        
        # Wistia-specific: extract video description from class or data attributes
        wistia_div = img_element.find_parent('div', class_=lambda x: x and 'wistia' in str(x).lower())
        if wistia_div:
            # Extract media ID from class
            classes = wistia_div.get('class', [])
            for cls in classes:
                if 'wistia_async_' in cls:
                    media_id = cls.replace('wistia_async_', '').split()[0]
                    context_parts.append(f"[Wistia video: {media_id}]")
                    break
        
        return ' '.join(context_parts[:500])  # Limit context length
    
    def _process_inline_elements(self, element, base_url):
        """Process inline elements within text."""
        result = []
        
        for child in element.children:
            if isinstance(child, str):
                # Normalize whitespace: replace tabs/newlines with spaces, collapse multiple spaces
                normalized = re.sub(r'\s+', ' ', child)
                result.append(normalized)
                continue
            
            if not hasattr(child, 'name'):
                continue
            
            tag = child.name
            text = child.get_text(' ', strip=True)  # Strip whitespace and collapse spaces
            
            if tag == 'a':
                href = child.get('href', '')
                if href:
                    full_url = urljoin(base_url, href)
                    result.append(f"[{text}]({full_url})")
                else:
                    result.append(text)
            elif tag == 'code':
                result.append(f"`{text}`")
            elif tag in ['strong', 'b']:
                result.append(f"**{text}**")
            elif tag in ['em', 'i']:
                result.append(f"*{text}*")
            elif tag == 'br':
                result.append('  \n')
            else:
                result.append(self._process_inline_elements(child, base_url))
        
        return ''.join(result).strip()
    
    def _process_list(self, element, base_url, ordered=False):
        """Process list elements."""
        lines = []
        items = element.find_all('li', recursive=False)
        
        for idx, li in enumerate(items, 1):
            prefix = f"{idx}." if ordered else "-"
            # Check for nested lists
            nested_ul = li.find('ul')
            nested_ol = li.find('ol')
            
            if nested_ul or nested_ol:
                # Get text before nested list
                text_parts = []
                for child in li.children:
                    if hasattr(child, 'name') and child.name in ['ul', 'ol']:
                        break
                    if isinstance(child, str):
                        text_parts.append(re.sub(r'\s+', ' ', child).strip())
                    else:
                        text_parts.append(re.sub(r'\s+', ' ', child.get_text()).strip())
                text = ' '.join(text_parts).strip()
                if text:
                    lines.append(f"{prefix} {text}")
                
                # Process nested list
                if nested_ul:
                    nested = self._process_list(nested_ul, base_url, False)
                    lines.append('  ' + nested.replace('\n', '\n  '))
                if nested_ol:
                    nested = self._process_list(nested_ol, base_url, True)
                    lines.append('  ' + nested.replace('\n', '\n  '))
            else:
                text = self._process_inline_elements(li, base_url)
                text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
                if text:
                    lines.append(f"{prefix} {text}")
        
        return '\n'.join(lines) + '\n'
    
    def _process_table(self, table):
        """Process table elements to Markdown."""
        lines = []
        
        # Headers
        thead = table.find('thead')
        if thead:
            headers = []
            for th in thead.find_all(['th', 'td']):
                headers.append(th.get_text().strip())
            if headers:
                lines.append('| ' + ' | '.join(headers) + ' |')
                lines.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')
        
        # Rows
        tbody = table.find('tbody') or table
        for tr in tbody.find_all('tr'):
            cells = []
            for td in tr.find_all(['td', 'th']):
                cells.append(td.get_text().strip())
            if cells:
                lines.append('| ' + ' | '.join(cells) + ' |')
        
        return '\n'.join(lines) + '\n' if lines else ''
    
    def html_to_clean_html(self, element, base_url):
        """Clean and prepare HTML for WordPress with local image references."""
        # Clone element to avoid modifying original
        import copy
        cleaned = copy.copy(element)
        
        # Remove script and style tags
        for tag in cleaned.find_all(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()
        
        # Process images: download and update src to include metadata marker
        for img in cleaned.find_all('img'):
            src = img.get('src')
            if src:
                full_src = urljoin(base_url, src)
                alt = img.get('alt', '')
                
                # If alt is empty, try to get from title or aria-label
                if not alt:
                    alt = img.get('title', '') or img.get('aria-label', '')
                
                context = self._get_image_context(img)
                
                # If still no alt text, generate from context
                if not alt and context:
                    # Extract text from context, removing markers like [Preceding:]
                    clean_context = re.sub(r'\[.*?:\s*', '', context)
                    clean_context = re.sub(r'\]', '', clean_context)
                    # Use first meaningful sentence (up to 100 chars)
                    alt = clean_context.split('.')[0].strip()[:100]
                
                # If still empty, use filename without extension
                if not alt:
                    from pathlib import Path
                    alt = Path(urlparse(full_src).path).stem
                
                local_path, filename = self.download_image(full_src, base_url, alt, context)
                if local_path:
                    # Mark image with data attributes for WordPress migration
                    img['data-original-src'] = full_src
                    img['data-local-path'] = local_path
                    img['data-filename'] = filename
                    img['src'] = local_path  # Use local path in HTML
                    if alt:
                        img['alt'] = alt  # Update alt attribute
        
        # Remove unwanted classes and attributes (but keep data-* attributes for images)
        for tag in cleaned.find_all(True):
            attrs_to_keep = {}
            if tag.name == 'a' and tag.get('href'):
                attrs_to_keep['href'] = urljoin(base_url, tag['href'])
            if tag.name == 'img':
                if tag.get('src'):
                    attrs_to_keep['src'] = tag['src']
                if tag.get('alt'):
                    attrs_to_keep['alt'] = tag['alt']
                # Keep data attributes for migration
                for attr in ['data-original-src', 'data-local-path', 'data-filename']:
                    if tag.get(attr):
                        attrs_to_keep[attr] = tag[attr]
            if tag.name in ['td', 'th'] and tag.get('colspan'):
                attrs_to_keep['colspan'] = tag['colspan']
            if tag.name in ['td', 'th'] and tag.get('rowspan'):
                attrs_to_keep['rowspan'] = tag['rowspan']
            
            tag.attrs = attrs_to_keep
        
        return str(cleaned)

    def extract_breadcrumb(self, soup, base_url):
        """Extract breadcrumb trail from the page."""
        nav = soup.find('nav', id='breadcrumb', class_=re.compile(r'wccom-breadcrumb'))
        if not nav:
            nav = soup.find('nav', attrs={'aria-label': re.compile(r'breadcrumb', re.I)})

        if not nav:
            return []

        items = []
        for li in nav.find_all('li', recursive=True):
            link = li.find('a', href=True)
            if link:
                text = link.get_text(' ', strip=True)
                url = self.normalize_url(urljoin(base_url, link['href']))
            else:
                text = li.get_text(' ', strip=True)
                url = None

            if not text:
                continue

            if items and items[-1]['title'] == text:
                continue

            items.append({
                'title': text,
                'url': url
            })

        if not items:
            return []

        return items

    def is_extension_document(self, breadcrumb):
        """Detect extension documents to exclude from scraping."""
        if not breadcrumb:
            return False

        titles = [item.get('title', '').strip().lower() for item in breadcrumb]
        sequence = ['documentation', 'products', 'extensions']

        for idx in range(len(titles) - len(sequence) + 1):
            if titles[idx:idx + len(sequence)] == sequence:
                return True

        return False

    def is_product_page(self, soup):
        """Detect product purchase pages to exclude from scraping."""
        if not soup:
            return False
        
        # Check for product sticky bottom bar component
        sticky_bar = soup.find('div', class_=re.compile(r'wccom-comp-product-sticky-bottom-bar'))
        return sticky_bar is not None

    def build_relative_path(self, url, breadcrumb):
        """Build a directory path from breadcrumbs or URL path."""
        if breadcrumb:
            crumbs = breadcrumb[:]
            while crumbs and crumbs[0].get('title', '').strip().lower() in {'documentation', 'woocommerce'}:
                crumbs = crumbs[1:]

            if len(crumbs) > 1:
                dir_parts = [self.sanitize_filename(item['title']) for item in crumbs[:-1]]
                dir_parts = [p for p in dir_parts if p]
                if dir_parts:
                    return os.path.join(*dir_parts)

        path_parts = [p for p in urlparse(url).path.split('/') if p]
        start = 0
        if 'documentation' in path_parts:
            start = path_parts.index('documentation') + 1
        if start < len(path_parts) and path_parts[start] == 'woocommerce':
            start += 1

        dir_parts = [self.sanitize_filename(p) for p in path_parts[start:-1]]
        dir_parts = [p for p in dir_parts if p]
        return os.path.join(*dir_parts) if dir_parts else ""

    def extract_categories(self, breadcrumb):
        """Extract category labels from breadcrumb items."""
        if not breadcrumb:
            return []

        crumbs = breadcrumb[:]
        while crumbs and crumbs[0].get('title', '').strip().lower() in {'documentation', 'woocommerce'}:
            crumbs = crumbs[1:]

        if len(crumbs) <= 1:
            return []

        return [item['title'] for item in crumbs[:-1] if item.get('title')]

    def render_categories_html(self, categories):
        """Render categories as HTML list for WordPress."""
        if not categories:
            return ""

        lines = ["<ul class=\"documentation_categories\">"]
        for category in categories:
            lines.append(f"  <li class=\"documentation_category\">{category}</li>")
        lines.append("</ul>\n")
        return "\n".join(lines)

    def unique_filepath(self, directory, filename):
        """Avoid overwriting files when multiple pages share the same title."""
        filepath = directory / filename
        if not filepath.exists():
            return filepath

        stem = filepath.stem
        suffix = filepath.suffix
        counter = 2
        while True:
            candidate = directory / f"{stem}-{counter}{suffix}"
            if not candidate.exists():
                return candidate
            counter += 1
    
    def save_page(self, content_data, relative_path=""):
        """Save page content as a Markdown file."""
        if not content_data:
            return

        breadcrumb = content_data.get('breadcrumb', [])
        breadcrumb_path = self.build_relative_path(content_data['url'], breadcrumb)

        # Create directory structure
        base_dir = Path(self.DOCS_DIR)
        save_path = breadcrumb_path or relative_path
        save_dir = base_dir / save_path if save_path else base_dir
        
        save_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filename from URL slug (stable) or title
        filename = self.slug_from_url(content_data['url'])
        if not filename:
            filename = self.sanitize_filename(content_data['title']) or "index"

        filepath = self.unique_filepath(save_dir, f"{filename}.md")
        
        categories = self.extract_categories(breadcrumb)
        categories_html = self.render_categories_html(categories)

        # Prepare markdown content with metadata
        markdown = f"""---
title: {content_data['title']}
url: {content_data['url']}
---

{categories_html}{content_data['content']}
"""
        # Clean up multiple consecutive blank lines (MD012)
        markdown = re.sub(r'\n{3,}', '\n\n', markdown)
        
        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"Saved: {filepath}")
        
        # Update metadata
        breadcrumb_titles = [item['title'] for item in breadcrumb]
        parent_url = None
        if len(breadcrumb) >= 2:
            parent_url = breadcrumb[-2].get('url')

        slug_path = self.build_slug_path(content_data['url'])
        slug = slug_path.split('/')[-1] if slug_path else self.slug_from_url(content_data['url'])

        self.metadata[content_data['url']] = {
            'title': content_data['title'],
            'path': str(filepath),
            'relative_path': save_path,
            'filename': filepath.name,
            'breadcrumb': breadcrumb,
            'breadcrumb_titles': breadcrumb_titles,
            'parent_url': parent_url,
            'categories': categories,
            'slug': slug,
            'slug_path': slug_path,
            'html_content': content_data.get('html_content', '')
        }
    
    def find_doc_links(self, soup, base_url):
        """Find all documentation links on a page."""
        if not soup:
            return []
        
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(base_url, href)
            
            # Only include WooCommerce documentation links
            if (
                'woocommerce.com/documentation/woocommerce' in full_url
                or 'woocommerce.com/document/' in full_url
            ):
                clean_url = self.normalize_url(full_url)
                if clean_url not in self.visited_urls:
                    links.append(clean_url)
        
        return links
    
    def scrape_all_pages(self, start_url):
        """Scrape all reachable documentation pages starting from base URL."""
        queue = [self.normalize_url(start_url)]
        queued = {queue[0]}

        while queue:
            # Check page limit
            if self.max_pages and self.pages_scraped >= self.max_pages:
                print(f"\nReached page limit ({self.max_pages}). Stopping.")
                break

            url = queue.pop(0)
            queued.discard(url)
            if url in self.visited_urls:
                continue

            self.visited_urls.add(url)

            soup = self.get_page_content(url)
            if not soup:
                continue

            # Skip product purchase pages
            if self.is_product_page(soup):
                print(f"Skipped product page: {url}")
                continue

            breadcrumb = self.extract_breadcrumb(soup, url)
            if self.is_extension_document(breadcrumb):
                print(f"Skipped extension document: {url}")
                continue

            content_data = self.extract_content(soup, url)
            if content_data:
                self.save_page(content_data)
                self.pages_scraped += 1

            links = self.find_doc_links(soup, url)
            for link in links:
                if link not in self.visited_urls and link not in queued:
                    queue.append(link)
                    queued.add(link)
    
    def save_metadata(self):
        """Save metadata to JSON file."""
        metadata_path = Path(self.METADATA_FILE)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
        print(f"Metadata saved to {metadata_path}")
        
        # Save images metadata
        if self.images_metadata:
            images_metadata_path = Path('images_metadata.json')
            with open(images_metadata_path, 'w', encoding='utf-8') as f:
                json.dump(self.images_metadata, f, indent=2, ensure_ascii=False)
            print(f"Images metadata saved to {images_metadata_path}")

    def save_wp_export(self):
        """Save WordPress REST API JSON export."""
        export_items = []
        for url, item in self.metadata.items():
            md_content = self.read_markdown_content(item['path'])
            
            # Extract HTML content from metadata if available
            html_content = item.get('html_content', md_content)
            
            # Collect images used in this page with full context
            page_images = []
            for img_url, img_data in self.images_metadata.items():
                # Check if this image is used on this page
                for ctx in img_data.get('contexts', []):
                    if ctx.get('page') == url:
                        page_images.append({
                            'source_url': img_url,
                            'local_path': img_data['local_path'],
                            'filename': img_data['filename'],
                            'alt': ctx.get('alt', ''),
                            'context': ctx.get('context', ''),  # Surrounding text
                            'position_hint': self._extract_position_from_content(html_content, img_url)
                        })
                        break
            
            export_items.append({
                'title': item['title'],
                'slug': item.get('slug') or self.slug_from_url(url),
                'slug_path': item.get('slug_path', ''),
                'content': html_content,  # HTML for WordPress (includes data-* attributes)
                'content_markdown': md_content,  # Markdown backup
                'status': 'draft',
                'parent_url': item.get('parent_url'),
                'categories': item.get('categories', []),
                'source_url': url,
                'images': page_images  # Images with position context
            })

        export_path = Path(self.WP_EXPORT_FILE)
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(export_items, f, indent=2, ensure_ascii=False)
        print(f"WordPress export saved to {export_path}")
    
    def _extract_position_from_content(self, html_content, img_url):
        """Extract position hint from HTML content."""
        # Find the approximate position of image in content
        if img_url in html_content:
            pos = html_content.find(img_url)
            # Get surrounding context (50 chars before and after)
            start = max(0, pos - 50)
            end = min(len(html_content), pos + len(img_url) + 50)
            return html_content[start:end]
        return ''

    def read_markdown_content(self, path):
        """Read Markdown content from a saved file."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return ""
    
    def run(self, start_url=None):
        """Run the scraper."""
        print("Starting WooCommerce documentation scraper...")
        url_to_scrape = start_url or self.BASE_URL
        print(f"Start URL: {url_to_scrape}")
        if self.max_pages:
            print(f"Page limit: {self.max_pages}")
        
        # Create output directory
        Path(self.DOCS_DIR).mkdir(parents=True, exist_ok=True)
        
        # Start scraping
        self.scrape_all_pages(url_to_scrape)
        
        # Save metadata
        self.save_metadata()
        self.save_wp_export()
        
        print(f"\nScraping complete!")
        print(f"Total pages scraped: {self.pages_scraped}")
        print(f"Files saved to: {self.DOCS_DIR}")


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description='Scrape WooCommerce documentation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scrape all documentation
  python scraper.py

  # Test with a specific page (single page only)
  python scraper.py --url "https://woocommerce.com/documentation/woocommerce/getting-started/" --max-pages 1

  # Scrape from a specific starting point with limit
  python scraper.py --url "https://woocommerce.com/documentation/woocommerce/products/" --max-pages 10
        """
    )
    parser.add_argument(
        '--url',
        type=str,
        help='Specific URL to start scraping from (default: base WooCommerce documentation)'
    )
    parser.add_argument(
        '--max-pages',
        type=int,
        help='Maximum number of pages to scrape (useful for testing)'
    )
    
    args = parser.parse_args()
    
    scraper = WooCommerceDocScraper(max_pages=args.max_pages)
    scraper.run(start_url=args.url)


if __name__ == "__main__":
    main()
