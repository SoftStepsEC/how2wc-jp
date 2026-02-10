#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Document Translator
Translates English Markdown documentation to Japanese using Google Translate.
"""

import os
import re
import json
import time
from pathlib import Path
from googletrans import Translator


class DocumentTranslator:
    """Translator for documentation files."""
    
    SOURCE_DIR = "docs/en"
    TARGET_DIR = "docs/ja"
    METADATA_FILE = "metadata.json"
    TRANSLATED_METADATA_FILE = "translated_metadata.json"
    
    def __init__(self):
        """Initialize the translator."""
        self.translator = Translator()
        self.translated_metadata = {}
        
    def load_metadata(self):
        """Load metadata from JSON file."""
        metadata_path = Path(self.METADATA_FILE)
        if metadata_path.exists():
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def translate_text(self, text, src='en', dest='ja'):
        """Translate text using Google Translate."""
        if not text or not text.strip():
            return text
        
        try:
            # Split long text into chunks to avoid API limits
            max_length = 4500
            if len(text) > max_length:
                chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
                translated_chunks = []
                for chunk in chunks:
                    result = self.translator.translate(chunk, src=src, dest=dest)
                    translated_chunks.append(result.text)
                    time.sleep(0.5)  # Rate limiting
                return ''.join(translated_chunks)
            else:
                result = self.translator.translate(text, src=src, dest=dest)
                return result.text
        except Exception as e:
            print(f"Translation error: {e}")
            return text
    
    def translate_markdown_file(self, source_path, target_path):
        """Translate a Markdown file from English to Japanese."""
        print(f"Translating: {source_path}")
        
        # Read source file
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
        if frontmatter_match:
            frontmatter = frontmatter_match.group(1)
            body = frontmatter_match.group(2)
            
            # Translate frontmatter title
            title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
            if title_match:
                original_title = title_match.group(1)
                translated_title = self.translate_text(original_title)
                frontmatter = re.sub(
                    r'^title:\s*.+$',
                    f'title: {translated_title}',
                    frontmatter,
                    flags=re.MULTILINE
                )
        else:
            frontmatter = ""
            body = content
        
        # Translate body while preserving Markdown structure
        translated_body = self.translate_markdown_content(body)
        
        # Reconstruct file
        if frontmatter:
            translated_content = f"---\n{frontmatter}\n---\n{translated_body}"
        else:
            translated_content = translated_body
        
        # Ensure target directory exists
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write translated file
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"Saved: {target_path}")
        
    def translate_markdown_content(self, content):
        """Translate Markdown content while preserving structure."""
        lines = content.split('\n')
        translated_lines = []
        
        in_code_block = False
        buffer = []
        
        for line in lines:
            # Detect code blocks
            if line.strip().startswith('```'):
                # Translate accumulated buffer
                if buffer and not in_code_block:
                    text = '\n'.join(buffer)
                    translated = self.translate_text(text)
                    translated_lines.extend(translated.split('\n'))
                    buffer = []
                
                # Add code block marker as-is
                translated_lines.append(line)
                in_code_block = not in_code_block
                continue
            
            # Don't translate code blocks
            if in_code_block:
                translated_lines.append(line)
                continue
            
            # Don't translate URLs, image paths
            if re.match(r'^\s*\[.*\]\(.*\)\s*$', line):
                translated_lines.append(line)
                continue
            
            # Accumulate text for translation
            if line.strip():
                buffer.append(line)
            else:
                # Translate accumulated buffer
                if buffer:
                    text = '\n'.join(buffer)
                    translated = self.translate_text(text)
                    translated_lines.extend(translated.split('\n'))
                    buffer = []
                translated_lines.append(line)
        
        # Translate remaining buffer
        if buffer and not in_code_block:
            text = '\n'.join(buffer)
            translated = self.translate_text(text)
            translated_lines.extend(translated.split('\n'))
        
        return '\n'.join(translated_lines)
    
    def translate_directory(self, source_dir, target_dir):
        """Translate all Markdown files in a directory."""
        source_path = Path(source_dir)
        target_path = Path(target_dir)
        
        if not source_path.exists():
            print(f"Source directory not found: {source_dir}")
            return
        
        # Find all Markdown files
        md_files = list(source_path.rglob('*.md'))
        
        print(f"Found {len(md_files)} Markdown files to translate")
        
        for md_file in md_files:
            # Calculate relative path
            relative_path = md_file.relative_to(source_path)
            target_file = target_path / relative_path
            
            # Translate file
            try:
                self.translate_markdown_file(md_file, target_file)
                
                # Update metadata
                self.translated_metadata[str(md_file)] = {
                    'source': str(md_file),
                    'target': str(target_file),
                    'relative_path': str(relative_path)
                }
                
                # Rate limiting
                time.sleep(1)
                
            except Exception as e:
                print(f"Error translating {md_file}: {e}")
    
    def save_translated_metadata(self):
        """Save translated file metadata."""
        metadata_path = Path(self.TRANSLATED_METADATA_FILE)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.translated_metadata, f, indent=2, ensure_ascii=False)
        print(f"Translation metadata saved to {metadata_path}")
    
    def run(self):
        """Run the translator."""
        print("Starting document translation...")
        print(f"Source: {self.SOURCE_DIR}")
        print(f"Target: {self.TARGET_DIR}")
        
        # Create target directory
        Path(self.TARGET_DIR).mkdir(parents=True, exist_ok=True)
        
        # Translate all files
        self.translate_directory(self.SOURCE_DIR, self.TARGET_DIR)
        
        # Save metadata
        self.save_translated_metadata()
        
        print("\nTranslation complete!")
        print(f"Translated files saved to: {self.TARGET_DIR}")


if __name__ == "__main__":
    translator = DocumentTranslator()
    translator.run()
