import os
from functions.helpers import validate_path, PathAction

def get_files_info(working_directory: str, directory: str | None = None) -> str:
    try:
        err, dir_path = validate_path(working_directory, directory, PathAction.CHECK_DIR)
        if err != None:
            return err

        dir_contents: list[str] = os.listdir(dir_path)
        return_list: list[str] = []

        for content in dir_contents:
            cont_path = os.path.join(dir_path, content)
            size = os.path.getsize(cont_path)
            is_dir = os.path.isdir(cont_path)
            return_list.append(f"- {content}: file_size={size} bytes, is_dir={is_dir}")

        return "\n".join(return_list)
    except Exception as e:
        return f'Error: {repr(e)}'
