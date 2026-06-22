import sys
import os
from pprint import pprint

def recursive_path_to_dict(path):
    if os.path.isdir(path):
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                items[items.index(item)] = recursive_path_to_dict(item_path)
        return {os.path.basename(path): items}
    else:
        return os.path.basename(path)

def create_dict_to_art(dir_dict:dict, indent=0) -> str:
    art = ""
    for key, value in dir_dict.items():
        if indent == -1:
            art += key + "/" + "\n"
        else:
            art += "│   " * indent + "├── " + key + "/" + "\n"
        if isinstance(value, dict):
            art += create_dict_to_art(value, indent + 1)
        if isinstance(value, list):
            i = 0
            for item in value:
                i += 1
                if i == len(value):
                    art += "│   " * (indent + 1) + "└── " + (item if isinstance(item, str) else list(item.keys())[0]) + "\n"
                    art += "│   " * (indent + 1) + "\n"
                else:
                    if isinstance(item, dict):
                        art += create_dict_to_art(item, indent + 1)
                    else:
                        art += "│   " * (indent + 1) + "├── " + item + "\n"
    return art


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_dir_struct_art.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.exists(directory_path):
        print(f"Error: The path '{directory_path}' does not exist.")
        sys.exit(1)

    dir_structure = recursive_path_to_dict(directory_path)
    pprint(dir_structure)
    
    print("\nDirectory Structure Art:\n")
    art = create_dict_to_art(dir_structure, indent=-1)
    print(art)