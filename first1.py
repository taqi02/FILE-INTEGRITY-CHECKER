import hashlib
import os

def clean_path(path):
    return path.strip().strip('"').strip("'")

def hash_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            return hashlib.sha256(content).hexdigest()
    except Exception as e:
        print(f"Error reading '{file_path}': {e}")
        return None

# Get file paths
file1 = clean_path(input("Enter path to the first file: "))
file2 = clean_path(input("Enter path to the second file: "))

# Check if both files exist
if not os.path.isfile(file1):
    print(f"File not found: {file1}")
elif not os.path.isfile(file2):
    print(f"File not found: {file2}")
else:
    # Calculate and display hashes
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    if hash1 and hash2:
        print("\n--- File Hashes ---")
        print(f"{file1}:\n{hash1}")
        print(f"{file2}:\n{hash2}")

        # Compare results
        if hash1 == hash2:
            print("\nThe files are IDENTICAL.")
        else:
            print("\nThe files are DIFFERENT.")
