import os
from functions.helpers import validate_path, PathAction

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        full_path = validate_path(working_directory, file_path, PathAction.WRITE_FILE)
        if isinstance(full_path, Exception):
            msg = str(full_path)
            if 'Error: ' in msg:
                return msg
            return f'Error: {msg}'

        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'


