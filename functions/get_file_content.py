import os
MAX_CHARS = 10000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory = os.path.join(".", working_directory)
        if not os.path.exists(working_directory):
            return f"Error:  There is a problem with the working directory: {working_directory}"
        
        file_path = file_path.lstrip(os.path.sep)
        abs_path = os.path.abspath(working_directory)
        full_file_path = os.path.join(abs_path, file_path)

        if not os.path.exists(full_file_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            return file_content_string
    except Exception as e:
        return f"Error: {repr(e)}"
