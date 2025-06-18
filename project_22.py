# Bulk file renamer

import os

def bulk_rename(folder_path, prefix):
    try:
        files = os.listdir(folder_path)
        files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
        files.sort()  # optional: for consistent ordering

        for index, filename in enumerate(files, start=1):
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}_{index}{ext}"
            src = os.path.join(folder_path, filename)
            dst = os.path.join(folder_path, new_name)
            os.rename(src, dst)
            print(f"Renamed: {filename} → {new_name}")

        print("\n✅ Done renaming all files.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter new filename prefix (e.g., image, doc, file): ")
    bulk_rename(folder, prefix)
