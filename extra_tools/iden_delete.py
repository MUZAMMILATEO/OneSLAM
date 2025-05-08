import os
import argparse

def delete_identifier_files(folder_path):
    count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if '.Identifier' in file:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    count += 1
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    print(f"\n? Deleted {count} file(s) containing '.Identifier'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete files with '.Identifier' in filename.")
    parser.add_argument("folder", type=str, help="Path to the folder to clean.")
    args = parser.parse_args()

    if os.path.isdir(args.folder):
        delete_identifier_files(args.folder)
    else:
        print(f"Error: '{args.folder}' is not a valid directory.")
