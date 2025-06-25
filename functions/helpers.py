import os
from enum import Enum

class PathAction(Enum):
    CHECK_DIR = 1
    READ_FILE = 2
    WRITE_FILE = 3


def validate_path(working_directory: str, sub_path: str, path_action: PathAction) -> tuple[bool, string]:

        match path_action:
            case PathAction.CHECK_DIR:
                working_directory = os.path.join(".", working_directory)
                if sub_path == None:
                    return (False,f"Error: Please specify a directory to get files from ")
                if not os.path.exists(working_directory):
                    return (False, f'Error:  There is a problem with the working directory: /
                                    "{working_directory}"')
                
                directory = directory.lstrip(os.path.sep)
                abs_path = os.path.abspath(working_directory)
                dir_path = os.path.join(abs_path, directory)

                if not os.path.exists(dir_path):
                    return (False, f'Error: Cannot list "{directory}" as it is outside the /
                                    permitted working directory')
                if not os.path.isdir(dir_path):
                    return (False, f'Error: "{directory}" is not a directory')
                return (True, dir_path)
            case PathAction.READ_FILE:
                pass
            case PathAction.WRITE_FILE:
                pass
            case _:
                pass

