import os
import argparse
import re

def should_exclude(directory):
    """Determines if a directory should be excluded based on name patterns."""
    # Aquí se definen patrones para excluir directorios que parecen hashes de Git u otros directorios específicos
    exclude_patterns = [
        r'^[a-f0-9]{2}$',  # Excluye directorios de dos caracteres que parecen ser de objetos de Git
        r'^[a-f0-9]{40}$',  # Excluye nombres de archivo que parecen ser hashes de commit de Git
        'info', 'logs', 'refs', '.github', '.git'  # Directorios específicos a excluir
    ]
    for pattern in exclude_patterns:
        if re.match(pattern, directory):
            return True
    return False

def print_directory_tree(startpath):
    """Recursively prints a visual tree of the directory structure starting from `startpath`"""
    exclude_dirs = {'node_modules', 'vendor', 'target'}  # Set de directorios a excluir por defecto
    for root, dirs, files in os.walk(startpath, topdown=True):
        # Filtra directorios tanto por nombre específico como por patrón
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not should_exclude(d)]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not should_exclude(f):  # También podrías querer filtrar archivos por patrones similares
                print('{}{}'.format(subindent, f))

def main():
    parser = argparse.ArgumentParser(description="Display directory tree")
    parser.add_argument('path', nargs='?', default=None, help="Path to the directory to scan")
    args = parser.parse_args()
    
    if args.path is None:
        args.path = input("Please enter the path to the directory you want to scan: ")
    
    path = os.path.abspath(args.path)
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return
    
    print_directory_tree(path)

if __name__ == "__main__":
    main()
