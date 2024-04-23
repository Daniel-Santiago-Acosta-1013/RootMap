import os
import argparse
import re

def should_exclude(directory):
    """Determines if a directory should be excluded based on name patterns."""
    exclude_patterns = [
        r'^[a-f0-9]{2}$',  # Excluye directorios de dos caracteres que parecen ser de objetos de Git
        r'^[a-f0-9]{40}$',  # Excluye nombres de archivo que parecen ser hashes de commit de Git
        'info', 'logs', 'refs', '.github', '.git'  # Directorios específicos a excluir
    ]
    for pattern in exclude_patterns:
        if re.match(pattern, directory):
            return True
    return False

def print_directory_tree(startpath, output_file):
    """Recursively prints a visual tree of the directory structure starting from `startpath` to a file."""
    exclude_dirs = {'node_modules', 'vendor', 'target'}  # Set de directorios a excluir por defecto
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(startpath, topdown=True):
            # Filtra los directorios y archivos que deben ser excluidos
            dirs[:] = [d for d in dirs if d not in exclude_dirs and not should_exclude(d)]
            files = [f for f in files if not should_exclude(f)]
            
            # Ordena directorios y archivos alfabéticamente
            dirs.sort()
            files.sort()

            level = root.replace(startpath, '').count(os.sep)
            indent = '│   ' * (level)
            print(f"{indent}├── {os.path.basename(root)}/", file=file)
            subindent = '│   ' * (level + 1)
            
            # Imprime primero los directorios, luego los archivos, conforme al estilo VS Code
            for d in dirs:
                print(f"{subindent}├── {d}/", file=file)
            for f in files:
                print(f"{subindent}├── {f}", file=file)

def main():
    parser = argparse.ArgumentParser(description="Display directory tree")
    parser.add_argument('path', nargs='?', default=None, help="Path to the directory to scan")
    parser.add_argument('-o', '--output', default='directory_tree.txt', help="Output file to write the directory tree")
    args = parser.parse_args()
    
    if args.path is None:
        args.path = input("Please enter the path to the directory you want to scan: ")
    
    path = os.path.abspath(args.path)
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    print_directory_tree(path, args.output)

if __name__ == "__main__":
    main()
