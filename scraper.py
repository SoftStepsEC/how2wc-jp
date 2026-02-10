#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WooCommerce Documentation Scraper
Fetches WooCommerce documentation pages and saves them as Markdown files.
"""

import os
import re
import time
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup


class WooCommerceDocScraper:
    """Scraper for WooCommerce documentation."""
    
    BASE_URL = "https://woocommerce.com/documentation/woocommerce/"
    DOCS_DIR = "docs/en"
    METADATA_FILE = "metadata.json"
    
    def __init__(self):
        """Initialize the scraper."""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.visited_urls = set()
        self.metadata = {}
        
    def sanitize_filename(self, text):
        """Convert text to a safe filename."""
        # Remove or replace invalid characters
        text = re.sub(r'[<>:"/\\|?*]', '', text)
        text = re.sub(r'\s+', '-', text)
        text = text.strip('-').lower()
        return text[:200]  # Limit length
    
    def get_page_content(self, url):
        """Fetch and parse a documentation page."""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=30)
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
        
        # Convert HTML to Markdown
        markdown_content = self.html_to_markdown(content_area, url)
        
        return {
            'title': title,
            'content': markdown_content,
            'url': url
        }
    
    def html_to_markdown(self, element, base_url):
        """Convert HTML element to Markdown."""
        lines = []
        
        # Process headings
        for i in range(1, 7):
            for heading in element.find_all(f'h{i}'):
                text = heading.get_text().strip()
                lines.append(f"{'#' * i} {text}\n")
        
        # Process paragraphs
        for p in element.find_all('p'):
            text = p.get_text().strip()
            if text:
                lines.append(f"{text}\n")
        
        # Process lists
        for ul in element.find_all('ul'):
            for li in ul.find_all('li', recursive=False):
                text = li.get_text().strip()
                lines.append(f"- {text}")
            lines.append("")
        
        for ol in element.find_all('ol'):
            for idx, li in enumerate(ol.find_all('li', recursive=False), 1):
                text = li.get_text().strip()
                lines.append(f"{idx}. {text}")
            lines.append("")
        
        # Process links
        for a in element.find_all('a'):
            href = a.get('href', '')
            text = a.get_text().strip()
            if href and text:
                full_url = urljoin(base_url, href)
                lines.append(f"[{text}]({full_url})")
        
        # Process code blocks
        for pre in element.find_all('pre'):
            code = pre.get_text().strip()
            lines.append(f"\n```\n{code}\n```\n")
        
        # Process inline code
        for code in element.find_all('code'):
            if not code.find_parent('pre'):
                text = code.get_text().strip()
                lines.append(f"`{text}`")
        
        return '\n'.join(lines)
    
    def save_page(self, content_data, relative_path=""):
        """Save page content as a Markdown file."""
        if not content_data:
            return
        
        # Create directory structure
        base_dir = Path(self.DOCS_DIR)
        if relative_path:
            save_dir = base_dir / relative_path
        else:
            save_dir = base_dir
        
        save_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filename from title
        filename = self.sanitize_filename(content_data['title'])
        if not filename:
            filename = "index"
        
        filepath = save_dir / f"{filename}.md"
        
        # Prepare markdown content with metadata
        markdown = f"""---
title: {content_data['title']}
url: {content_data['url']}
---

# {content_data['title']}

{content_data['content']}
"""
        
        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        print(f"Saved: {filepath}")
        
        # Update metadata
        self.metadata[content_data['url']] = {
            'title': content_data['title'],
            'path': str(filepath),
            'relative_path': relative_path,
            'filename': f"{filename}.md"
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
            if 'woocommerce.com/documentation' in full_url:
                # Normalize URL
                parsed = urlparse(full_url)
                clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                if clean_url not in self.visited_urls:
                    links.append(clean_url)
        
        return links
    
    def scrape_page(self, url, depth=0, max_depth=3, parent_path=""):
        """Recursively scrape a documentation page and its children."""
        if depth > max_depth or url in self.visited_urls:
            return
        
        self.visited_urls.add(url)
        
        # Fetch page
        soup = self.get_page_content(url)
        if not soup:
            return
        
        # Extract and save content
        content_data = self.extract_content(soup, url)
        if content_data:
            self.save_page(content_data, parent_path)
        
        # Find and scrape child pages
        if depth < max_depth:
            links = self.find_doc_links(soup, url)
            for link in links[:10]:  # Limit to avoid too many pages
                time.sleep(1)  # Be polite
                
                # Create subdirectory based on URL structure
                path_parts = urlparse(link).path.strip('/').split('/')
                if len(path_parts) > 2:
                    subdir = self.sanitize_filename(path_parts[-1])
                    child_path = os.path.join(parent_path, subdir) if parent_path else subdir
                else:
                    child_path = parent_path
                
                self.scrape_page(link, depth + 1, max_depth, child_path)
    
    def save_metadata(self):
        """Save metadata to JSON file."""
        metadata_path = Path(self.METADATA_FILE)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
        print(f"Metadata saved to {metadata_path}")
    
    def run(self):
        """Run the scraper."""
        print("Starting WooCommerce documentation scraper...")
        print(f"Base URL: {self.BASE_URL}")
        
        # Create output directory
        Path(self.DOCS_DIR).mkdir(parents=True, exist_ok=True)
        
        # Start scraping from base URL
        self.scrape_page(self.BASE_URL, max_depth=2)
        
        # Save metadata
        self.save_metadata()
        
        print(f"\nScraping complete!")
        print(f"Total pages scraped: {len(self.visited_urls)}")
        print(f"Files saved to: {self.DOCS_DIR}")


if __name__ == "__main__":
    scraper = WooCommerceDocScraper()
    scraper.run()
