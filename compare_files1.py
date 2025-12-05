import os
from datetime import datetime

def compare_files(file1, file2):
    """Compare size and modified date of two files."""
    try:
        stat1 = os.stat(file1)
        stat2 = os.stat(file2)
        
        size1 = stat1.st_size
        size2 = stat2.st_size
        mtime1 = datetime.fromtimestamp(stat1.st_mtime)
        mtime2 = datetime.fromtimestamp(stat2.st_mtime)
        
        print(f"File 1: {file1}")
        print(f"  Size: {size1} bytes")
        print(f"  Modified: {mtime1}")
        print()
        print(f"File 2: {file2}")
        print(f"  Size: {size2} bytes")
        print(f"  Modified: {mtime2}")
        print()
        print("Comparison:")
        print(f"  Size match: {size1 == size2}")
        print(f"  Modified date match: {mtime1 == mtime2}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file1 = input("Enter first file path: ")
    file2 = input("Enter second file path: ")
    compare_files(file1, file2)