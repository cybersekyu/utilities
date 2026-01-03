import os
from datetime import datetime

def get_file_info(base_folder):
    file_map = {}

    for root, _, files in os.walk(base_folder):
        for file in files:
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_folder)

            stat = os.stat(full_path)

            file_map[rel_path] = {
                "size": stat.st_size,
                "modified": stat.st_mtime
            }

    return file_map


def compare_folders(folder_a, folder_b):
    a_info = get_file_info(folder_a)
    b_info = get_file_info(folder_b)

    only_in_a = []
    only_in_b = []
    differences = []
    matches = []

    all_files = set(a_info.keys()) | set(b_info.keys())

    for rel in all_files:
        if rel not in a_info:
            only_in_b.append(rel)
            continue

        if rel not in b_info:
            only_in_a.append(rel)
            continue

        a_size = a_info[rel]["size"]
        b_size = b_info[rel]["size"]
        a_mod = a_info[rel]["modified"]
        b_mod = b_info[rel]["modified"]

        # Compare size or modified time (1-second tolerance)
        if a_size != b_size or abs(a_mod - b_mod) > 1:
            differences.append({
                "file": rel,
                "size_a": a_size,
                "size_b": b_size,
                "modified_a": datetime.fromtimestamp(a_mod),
                "modified_b": datetime.fromtimestamp(b_mod),
            })
        else:
            matches.append(rel)

    return only_in_a, only_in_b, differences, matches


if __name__ == "__main__":
    folder_a = input("Enter first file path: ")
    folder_b = input("Enter second file path: ")

    only_in_a, only_in_b, differences, matches = compare_folders(folder_a, folder_b)

    print("\n=== Files only in A ===")
    for f in only_in_a:
        print(f)

    print("\n=== Files only in B ===")
    for f in only_in_b:
        print(f)

    print("\n=== Files with Differences ===")
    for diff in differences:
        print(f"\nFile: {diff['file']}")
        print(f"  Size A: {diff['size_a']} bytes")
        print(f"  Size B: {diff['size_b']} bytes")
        print(f"  Modified A: {diff['modified_a']}")
        print(f"  Modified B: {diff['modified_b']}")

    print("\n=== Matching Files ===")
    for f in matches:
        print(f)
