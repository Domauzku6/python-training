import shutil
import os

# Source path
src_path = r'C:\Users\uzkur\Desktop\python training\create_edit_text_file-(dont-forget-rbefore_C)\readme.txt'
# Destination path
dest_path = r'C:\Users\uzkur\Desktop\python training\move files\readme.txt'

# Ensure the destination directory exists
os.makedirs(os.path.dirname(dest_path), exist_ok=True)

# Check if the source file exists before moving
if os.path.exists(src_path):
    # Move the file
    shutil.move(src_path, dest_path)
    print(f"File moved from {src_path} to {dest_path}")
else:
    print(f"Source file does not exist: {src_path}")
