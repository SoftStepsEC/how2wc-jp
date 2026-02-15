#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Checker
Checks for updates in WooCommerce documentation and identifies new/changed pages.
"""

import os
import json
import hashlib
from pathlib import Path
from scraper import WooCommerceDocScraper


class UpdateChecker:
    """Check for documentation updates."""
    
    METADATA_FILE = "metadata.json"
    PREVIOUS_METADATA_FILE = "metadata_previous.json"
    
    def __init__(self):
        """Initialize the update checker."""
        self.scraper = WooCommerceDocScraper()
        
    def load_metadata(self, filepath):
        """Load metadata from JSON file."""
        path = Path(filepath)
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_metadata(self, metadata, filepath):
        """Save metadata to JSON file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
    
    def compare_metadata(self, old_metadata, new_metadata):
        """Compare old and new metadata to find changes."""
        changes = {
            'new': [],
            'updated': [],
            'deleted': []
        }
        
        old_urls = set(old_metadata.keys())
        new_urls = set(new_metadata.keys())
        
        # Find new pages
        changes['new'] = list(new_urls - old_urls)
        
        # Find deleted pages
        changes['deleted'] = list(old_urls - new_urls)
        
        # Find updated pages (by comparing content hashes)
        for url in old_urls & new_urls:
            old_info = old_metadata[url]
            new_info = new_metadata[url]
            
            # Use content_hash from metadata if available (added in recent scraper update)
            # If not available in old metadata, we assume it might have changed if we strictly want to be safe,
            # or skip. For now, if key is missing, we can't compare, so we assume no change 
            # OR we could fallback to file hash if we hadn't overwritten. 
            # Since we overwrite, missing hash in old metadata means we can't detect update this run.
            
            old_hash = old_info.get('content_hash')
            new_hash = new_info.get('content_hash')
            
            if old_hash and new_hash:
                if old_hash != new_hash:
                    changes['updated'].append(url)
            # Fallback for old scraping style (calculate_file_hash on path) is removed
            # because files are overwritten by scraper.run() before this check.
        
        return changes
    
    def check_for_updates(self):
        """Check for updates in documentation."""
        print("Checking for documentation updates...")
        
        # Load previous metadata
        old_metadata = self.load_metadata(self.PREVIOUS_METADATA_FILE)
        
        # Scrape current documentation
        print("\nFetching current documentation...")
        self.scraper.run()
        
        # Load new metadata
        new_metadata = self.load_metadata(self.METADATA_FILE)
        
        # Compare
        changes = self.compare_metadata(old_metadata, new_metadata)
        
        # Report findings
        print("\n=== Update Report ===")
        print(f"New pages: {len(changes['new'])}")
        for url in changes['new']:
            print(f"  + {url}")
        
        print(f"\nUpdated pages: {len(changes['updated'])}")
        for url in changes['updated']:
            print(f"  * {url}")
        
        print(f"\nDeleted pages: {len(changes['deleted'])}")
        for url in changes['deleted']:
            print(f"  - {url}")
        
        # Save current metadata as previous for next run
        self.save_metadata(new_metadata, self.PREVIOUS_METADATA_FILE)
        
        return changes
    
    def get_changed_files(self, changes):
        """Get list of files that need translation."""
        files_to_translate = []
        
        metadata = self.load_metadata(self.METADATA_FILE)
        
        for url in changes['new'] + changes['updated']:
            if url in metadata:
                file_info = metadata[url]
                files_to_translate.append(file_info['path'])
        
        return files_to_translate


if __name__ == "__main__":
    checker = UpdateChecker()
    changes = checker.check_for_updates()
    
    # Save list of changed files for the translator
    changed_files = checker.get_changed_files(changes)
    if changed_files:
        with open('changed_files.txt', 'w', encoding='utf-8') as f:
            for file_path in changed_files:
                f.write(f"{file_path}\n")
        print(f"\nSaved {len(changed_files)} changed files to changed_files.txt")
    elif os.path.exists('changed_files.txt'):
        # Clean up if no changes
        os.remove('changed_files.txt')

    if changes['new'] or changes['updated']:
        print("\n✓ Changes detected - translation needed")
    else:
        print("\n✓ No changes detected")
