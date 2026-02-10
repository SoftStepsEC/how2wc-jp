#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main workflow script
Runs the complete scraping and translation workflow.
"""

import sys
from pathlib import Path
from scraper import WooCommerceDocScraper
from translator import DocumentTranslator


def main():
    """Run the complete workflow."""
    print("=" * 60)
    print("WooCommerce Documentation Translation Workflow")
    print("=" * 60)
    
    # Step 1: Scrape documentation
    print("\n[1/2] Scraping WooCommerce documentation...")
    print("-" * 60)
    scraper = WooCommerceDocScraper()
    try:
        scraper.run()
    except Exception as e:
        print(f"Error during scraping: {e}")
        return 1
    
    # Step 2: Translate documentation
    print("\n[2/2] Translating documentation to Japanese...")
    print("-" * 60)
    translator = DocumentTranslator()
    try:
        translator.run()
    except Exception as e:
        print(f"Error during translation: {e}")
        return 1
    
    # Complete
    print("\n" + "=" * 60)
    print("Workflow completed successfully!")
    print("=" * 60)
    print(f"\nEnglish docs: {scraper.DOCS_DIR}")
    print(f"Japanese docs: {translator.TARGET_DIR}")
    print(f"Metadata: metadata.json, translated_metadata.json")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
