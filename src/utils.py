import sys

def load_text(file_path: str) -> str:
    """Load text from a file."""
    try: 
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
        sys.exit(1)