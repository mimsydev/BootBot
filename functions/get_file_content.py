import os
from functions.helpers import validate_path, PathAction
MAX_CHARS = 10000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        err, full_file_path = validate_path(working_directory, file_path, PathAction.READ_FILE)
        if err != None:
            return err
        if full_file_path == None:
            return 'Error: Unexpected empty path'

        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
    except Exception as e:
        return f"Error: {repr(e)}"
