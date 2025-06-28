import os
from functions.helpers import validate_path, PathAction

def get_files_info(working_directory: str, directory: str = '') -> str:
    try:
        full_path = validate_path(working_directory, directory, PathAction.CHECK_DIR)
        if isinstance(full_path, Exception):
            msg = str(full_path)
            if 'Error: ' in msg:
                return msg
            return f'Error: {msg}'

        dir_contents: list[str] = os.listdir(full_path)
        return_list: list[str] = []

        for content in dir_contents:
            cont_path = os.path.join(full_path, content)
            size = os.path.getsize(cont_path)
            is_dir = os.path.isdir(cont_path)
            return_list.append(f"- {content}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(return_list)
    except Exception as e:
        return f'Error: {str(e)}'
