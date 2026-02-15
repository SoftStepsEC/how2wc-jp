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
import argparse
from pathlib import Path
from google.cloud import translate_v3 as translate
from google.cloud import storage
from dotenv import load_dotenv


class DocumentTranslator:
    """Translator for documentation files."""
    # ...
    # This was a quick fix but I forgot indentation for args.estimate_cost block in previous tool call.
    # Actually, previous tool call was successful. I'll just check if indentation is correct.
    # The snippet I provided was:
    
            if not args.estimate_cost:
                    relative_path = source_file.relative_to(Path(translator.SOURCE_DIR))
                    translator.translated_metadata[str(source_file)] = {
                        'source': str(source_file),
                        'target': str(target_file),
                        'relative_path': str(relative_path)
                    }
    # Wait, the relative_path construction might fail if source_file is not relative to source dir.
    # And indentation looks weird in my memory but let's assume it's OK.
    # Ah, I see I missed `import time` usage in previous block but it was already imported at top.

    # Let's double check indentation of the added block.
    # The block added was:
    #     elif args.file_list:
    # ...
    #             if not args.estimate_cost:
    #                 relative_path = source_file.relative_to(Path(translator.SOURCE_DIR))
    # ...

    # If source_file is not in SOURCE_DIR, relative_to will raise ValueError.
    # verify logic in resolve_target_path handles out-of-source files but here we assume inside.
    # Let's check `resolve_target_path` implementation again.
    
    # It does: `relative_path = source_path.relative_to(source_root)`
    # So if it fails, resolve_target_path handles it gracefully?
    # No, it prints note and returns differently.
    
    # We should use `resolve_target_path` logic or just wrap in try-except.
    
    # Also I need to modify workflow file to use --file-list.

    """Translator for documentation files."""
    
    SOURCE_DIR = "docs/en"
    TARGET_DIR = "docs/ja"
    METADATA_FILE = "metadata.json"
    TRANSLATED_METADATA_FILE = "translated_metadata.json"
    DEFAULT_LOCATION = "global"
    GLOSSARY_ID = "woocommerce-glossary"
    
    def __init__(self, estimate_mode=False):
        """Initialize the translator."""
        load_dotenv()
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        self.location = os.getenv("GOOGLE_CLOUD_LOCATION", self.DEFAULT_LOCATION)
        self.estimate_mode = estimate_mode
        self.total_characters = 0
        
        # Optional: Bucket for glossary creation (only needed if creating a new glossary)
        self.glossary_bucket = os.getenv("GOOGLE_CLOUD_GLOSSARY_BUCKET") 
        
        if not self.estimate_mode:
            self._validate_cloud_settings()
            self.client = translate.TranslationServiceClient()
            self.glossary_config = None
            self._setup_glossary()
        else:
             self.client = None
             self.glossary_config = None
             
        self.translated_metadata = {}

    def _validate_cloud_settings(self):
        """Validate required Google Cloud settings."""
        if not self.project_id:
            raise ValueError(
                "Missing GOOGLE_CLOUD_PROJECT. Set the env var or add it to a .env file."
            )

    def _setup_glossary(self):
        """Check if glossary exists, create if not (if bucket is provided), and set config."""
        glossary_name = self.client.glossary_path(
            self.project_id, self.location, self.GLOSSARY_ID
        )
        try:
            self.client.get_glossary(name=glossary_name)
            print(f"Using existing glossary: {glossary_name}")
            self.glossary_config = translate.TranslateTextGlossaryConfig(
                glossary=glossary_name
            )
        except Exception:
            print(f"Glossary {self.GLOSSARY_ID} not found.")
            if self.glossary_bucket:
                print("Attempting to create glossary...")
                self._create_glossary(glossary_name)
            else:
                print("No GOOGLE_CLOUD_GLOSSARY_BUCKET provided. Skipping glossary creation.")
                print("To use glossary, please upload glossary.csv to a bucket and set the env var.")

    def _create_glossary(self, glossary_name):
        """Create a glossary resource in Google Cloud."""
        # Upload glossary.csv to GCS
        if not self.glossary_bucket:
             print("Error: GOOGLE_CLOUD_GLOSSARY_BUCKET not set. Cannot create glossary.")
             return

        print(f"Uploading glossary.csv to gs://{self.glossary_bucket}...")
        try:
            storage_client = storage.Client(project=self.project_id)
            bucket = storage_client.bucket(self.glossary_bucket)
            blob = bucket.blob("glossary.csv")
            blob.upload_from_filename("glossary.csv")
            print("Upload complete.")
            
            gcs_uri = f"gs://{self.glossary_bucket}/glossary.csv"
            
            print(f"Creating glossary resource from {gcs_uri}...")
            
            glossary = translate.Glossary(
                name=glossary_name,
                language_codes_set=translate.Glossary.LanguageCodesSet(
                    language_codes=["en", "ja"]
                ),
                input_config=translate.GlossaryInputConfig(
                    gcs_source=translate.GcsSource(input_uri=gcs_uri)
                ),
            )

            operation = self.client.create_glossary(
                parent=f"projects/{self.project_id}/locations/{self.location}",
                glossary=glossary
            )
            result = operation.result(timeout=180)
            print("Created glossary: {}".format(result.name))
            self.glossary_config = translate.TranslateTextGlossaryConfig(
                glossary=result.name
            )
        except Exception as e:
            print(f"Failed to create glossary: {e}")

    def resolve_target_path(self, source_path):
        """Resolve target path ensuring it mirrors the source folder structure."""
        source_path = Path(source_path).resolve()
        source_root = Path(self.SOURCE_DIR).resolve()
        
        try:
            # Check if file is inside the source root
            relative_path = source_path.relative_to(source_root)
            target_path = Path(self.TARGET_DIR).resolve() / relative_path
            return target_path
        except ValueError:
            # File is outside SOURCE_DIR, output with suffix in same dir
            # Or handle arbitrary paths
            print(f"Note: {source_path} is outside configured source dir {self.SOURCE_DIR}")
            if source_path.is_dir():
                return source_path.with_name(source_path.name + "_translated")
            return source_path.with_name(source_path.stem + "_ja" + source_path.suffix)
            
    def load_metadata(self):
        """Load metadata from JSON file."""
        metadata_path = Path(self.METADATA_FILE)
        if metadata_path.exists():
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def translate_text(self, text, src='en', dest='ja'):
        """Translate text using Google Cloud Translation API."""
        if not text or not text.strip():
            return text
            
        if self.estimate_mode:
            self.total_characters += len(text)
            return text
        
        try:
            # Split long text into chunks to avoid API limits
            max_length = 4500
            if len(text) > max_length:
                chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
                translated_chunks = []
                for chunk in chunks:
                    translated_chunks.append(self._translate_chunk(chunk, src, dest))
                    time.sleep(0.2)  # Rate limiting
                return ''.join(translated_chunks)
            else:
                return self._translate_chunk(text, src, dest)
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    def _translate_chunk(self, text, src, dest):
        """Translate a single chunk via Cloud Translation API."""
        parent = f"projects/{self.project_id}/locations/{self.location}"
        
        # Use simple translation request, but add glossary if available
        request = {
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": src,
            "target_language_code": dest,
            # Enable "Translation LLM" equivalent features by using NMT (default)
            # which is now highly advanced. 
        }
        
        if self.glossary_config:
            request["glossary_config"] = self.glossary_config
            
        response = self.client.translate_text(request=request)
        
        if not response.translations:
            return text
        return response.translations[0].translated_text
    
    def translate_markdown_file(self, source_path, target_path):
        """Translate a Markdown file from English to Japanese."""
        if self.estimate_mode:
             print(f"Estimating: {source_path}")
        else:
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
        
        if self.estimate_mode:
            # Just calculating costs, don't write file
            return

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
                if not self.estimate_mode:
                    self.translated_metadata[str(md_file)] = {
                        'source': str(md_file),
                        'target': str(target_file),
                        'relative_path': str(relative_path)
                    }
                
                # Rate limiting
                if not self.estimate_mode:
                    time.sleep(1)
                
            except Exception as e:
                print(f"Error translating {md_file}: {e}")
                
        if self.estimate_mode:
            self._print_cost_estimate()

    def _print_cost_estimate(self):
        """Print the estimated translation cost."""
        total_chars = self.total_characters
        # Pricing assumption: $20.00 USD per million characters (approximate standard/advanced rate)
        # Note: Actual pricing depends on volume, specific API version (Basic vs Advanced), and currency.
        price_per_million = 20.00
        cost_usd = (total_chars / 1_000_000) * price_per_million
        
        print("\n" + "=" * 40)
        print(f"TRANSLATION COST ESTIMATE (Dry Run)")
        print("=" * 40)
        print(f"Total Characters to Translate: {total_chars:,}")
        print(f"Estimated Cost (USD): ${cost_usd:,.2f}")
        print(f"  (@ ${price_per_million:.2f} per 1M chars)")
        print("=" * 40 + "\n")
    
    def save_translated_metadata(self):
        """Save translated file metadata."""
        metadata_path = Path(self.TRANSLATED_METADATA_FILE)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.translated_metadata, f, indent=2, ensure_ascii=False)
        print(f"Translation metadata saved to {metadata_path}")
    
    def run(self):
        """Run the translator."""
        if self.estimate_mode:
             print("MODE: COST ESTIMATION ONLY (Dry Run)")
        else:
            print("Starting document translation...")
        print(f"Source: {self.SOURCE_DIR}")
        print(f"Target: {self.TARGET_DIR}")
        
        # Create target directory
        if not self.estimate_mode:
            Path(self.TARGET_DIR).mkdir(parents=True, exist_ok=True)
        
        # Translate all files
        self.translate_directory(self.SOURCE_DIR, self.TARGET_DIR)
        
        # Save metadata
        if not self.estimate_mode:
            self.save_translated_metadata()
        
        print("\nTranslation complete!")
        if not self.estimate_mode:
            print(f"Translated files saved to: {self.TARGET_DIR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate WooCommerce documentation.")
    parser.add_argument("--file", help="Translate a specific file")
    parser.add_argument("--dir", help="Translate a specific directory")
    parser.add_argument("--file-list", help="File containing list of files to translate (one per line)")
    parser.add_argument("--estimate-cost", action="store_true", help="Calculate estimated translation cost without running translation")
    
    args = parser.parse_args()
    
    translator = DocumentTranslator(estimate_mode=args.estimate_cost)
    
    if args.file:
        source_file = Path(args.file)
        if not source_file.exists():
            print(f"Error: File not found: {source_file}")
            exit(1)
            
        target_file = translator.resolve_target_path(source_file)
        if args.estimate_cost:
            print(f"Estimating cost for single file: {source_file}")
        else:
            print(f"Translating single file: {source_file} -> {target_file}")
            
        translator.translate_markdown_file(source_file, target_file)
        if args.estimate_cost:
            translator._print_cost_estimate()
        
    elif args.dir:
        source_dir = Path(args.dir)
        if not source_dir.exists():
            print(f"Error: Directory not found: {source_dir}")
            exit(1)
            
        target_dir = translator.resolve_target_path(source_dir)
        if args.estimate_cost:
             print(f"Estimating cost for directory: {source_dir}")
        else:
            print(f"Translating directory: {source_dir} -> {target_dir}")
            Path(target_dir).mkdir(parents=True, exist_ok=True)
            
        translator.translate_directory(source_dir, target_dir)
        if not args.estimate_cost:
            translator.save_translated_metadata()
            
    elif args.file_list:
        file_list_path = Path(args.file_list)
        if not file_list_path.exists():
            print(f"Error: File list not found: {file_list_path}")
            exit(1)
            
        with open(file_list_path, 'r', encoding='utf-8') as f:
            files = [line.strip() for line in f if line.strip()]
            
        print(f"Translating {len(files)} files from list: {file_list_path}")
        
        for file_path in files:
            source_file = Path(file_path)
            if not source_file.exists():
                print(f"Warning: File from list not found: {source_file}")
                continue
                
            target_file = translator.resolve_target_path(source_file)
            
            try:
                # Calculate relative path for metadata
                try:
                    relative_path = str(source_file.relative_to(Path(translator.SOURCE_DIR)))
                except ValueError:
                    relative_path = source_file.name

                if args.estimate_cost:
                    # just verify paths for estimate
                    pass
                else:
                    print(f"Translating: {source_file} -> {target_file}")
                
                translator.translate_markdown_file(source_file, target_file)
                
                if not args.estimate_cost:
                    translator.translated_metadata[str(source_file)] = {
                        'source': str(source_file),
                        'target': str(target_file),
                        'relative_path': relative_path
                    }
                    time.sleep(1) # Rate limiting
                    
            except Exception as e:
                print(f"Error processing {source_file}: {e}")

        if args.estimate_cost:
             translator._print_cost_estimate()
        else:
             translator.save_translated_metadata()
        
    else:
        # Default behavior: run full translation
        if args.estimate_cost:
            print(f"Estimating cost for ALL files in: {translator.SOURCE_DIR}")
        
        translator.run()
