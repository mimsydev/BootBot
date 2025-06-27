import os
from enum import Enum

class PathAction(Enum):
    CHECK_DIR = 1
    READ_FILE = 2
    WRITE_FILE = 3


def validate_path(working_directory: str, sub_path: str | None, path_action: \
                  PathAction) -> tuple[str | None, str | None]:
    try:
        rel_working_directory = os.path.join(".", working_directory)
        if sub_path == None:
            return (f"Error: Please specify a directory to get files from ", None)
        if not os.path.exists(rel_working_directory):
            return (f'Error:  There is a problem with the working directory: \
            "{working_directory}"', None)

        abs_path = os.path.abspath(rel_working_directory)
        full_path = os.path.join(abs_path, sub_path)
        print(full_path)

        match path_action:
            case PathAction.CHECK_DIR:
                if not working_directory in full_path:
                    return (f'Error: Cannot list "{sub_path}" as it is outside \
                    the permitted working directory', None)
                if not os.path.isdir(full_path):
                    return (f'Error: "{sub_path}" is not a directory', None)
                return (None, full_path)
            case PathAction.READ_FILE:
                if not working_directory in full_path:
                    return (f'Error: Cannot read "{sub_path}" as it is outside \
                    the permitted working directory', None)
                if not os.path.isfile(full_path):
                    return (f'Error: File not found or is not a regular file: \
                    "{sub_path}"', None)
                return (None, full_path)
            case PathAction.WRITE_FILE:
                if not working_directory in full_path:
                    return (f'Error: Cannot write to "{sub_path}" as it is \
                    outside the permitted working directory', None)
                dirname = os.path.dirname(full_path)
                if not os.path.isdir(dirname):
                    os.makedirs(dirname)
                return (None, full_path)
            case _:
                return(f"Error: The PathAction: {path_action} is invalid.", None)
    except Exception as e:
       return(f"Error: {repr(e)}", None)

