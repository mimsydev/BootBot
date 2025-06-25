import os

def get_files_info(working_directory: str, directory: str | None = None) -> str:
    try:
        working_directory = os.path.join(".", working_directory)
        if directory == None:
            return f"Error: Please specify a directory to get files from "
        if not os.path.exists(working_directory):
            return f"Error:  There is a problem with the working directory: {working_directory}"
        
        directory = directory.lstrip(os.path.sep)
        abs_path = os.path.abspath(working_directory)
        dir_path = os.path.join(abs_path, directory)

        if not os.path.exists(dir_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(dir_path):
            return f'Error: "{directory}" is not a directory'
        
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
