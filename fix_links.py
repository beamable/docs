import os
import re
import argparse

def fix_links_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find [name](doc:name_of_file)
    pattern = r'\[([^\]]+)\]\(doc:([^)]+)\)'
    
    # Replace with [name](name_of_file.md)
    new_content = re.sub(pattern, r'[\1](\2.md)', content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Fix markdown links in a folder.")
    parser.add_argument("folder_path", help="Path to the folder containing .md files")
    args = parser.parse_args()
    
    folder_path = args.folder_path
    
    print("Starting link fix process...")
    if not os.path.exists(folder_path):
        print(f"Folder does not exist: {folder_path}")
        return
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            filepath = os.path.join(folder_path, filename)
            fix_links_in_file(filepath)
    
    print("All files processed.")

if __name__ == "__main__":
    main()
