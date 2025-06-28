import os
from functions.helpers import validate_path, PathAction

MAX_CHARS = 10000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        full_path = validate_path(working_directory, file_path, \
                                       PathAction.READ_FILE)
        if isinstance(full_path, Exception):
            msg = str(full_path)
            if 'Error: ' in msg:
                return msg
            return f'Error: {msg}'

        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'
