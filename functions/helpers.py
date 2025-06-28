import os
from enum import Enum
from types import FunctionType
from typing import Union


class PathAction(Enum):
    CHECK_DIR = 1
    READ_FILE = 2
    WRITE_FILE = 3
    RUN_FILE = 4

# There are a number of different validation types that need to be handled. This
# will invoke the appropriate validator based on the PathAction
def validate_path(working_directory: str, sub_path:str,  path_action: PathAction)\
    -> Union[str, Exception]:
    try:
        full_path = _initial_validation(working_directory, sub_path)
        if isinstance(full_path, Exception):
            return full_path
        path_validator = _get_path_validator(path_action)
        return path_validator(full_path, working_directory, sub_path)
    except Exception as e:
        return e

def _get_path_validator(path_action: PathAction) -> FunctionType:
    match path_action:
        case PathAction.CHECK_DIR:
            return _validate_dir
        case PathAction.READ_FILE:
            return _validate_file_read
        case PathAction.WRITE_FILE:
            return _validate_file_write
        case PathAction.RUN_FILE:
            return _validate_file_run

# There is some basic validation that is common to all path actions
def _initial_validation(working_directory: str, sub_path: str) \
    -> Union[str,Exception]:
    rel_working_directory = os.path.join(".", working_directory)
    if not os.path.exists(rel_working_directory):
        return Exception(f'Error:  There is a problem with the working '
                f'directory: "{working_directory}"')

    abs_path = os.path.abspath(rel_working_directory)
    full_path = os.path.join(abs_path, sub_path)
    return full_path

# All the individual validators to invoke based on the PathAction
def _validate_dir(full_path: str, working_directory: str, sub_path: str)\
    -> Union[str,Exception]:
    if not working_directory in full_path or '..' in full_path:
        return Exception((f'Error: Cannot list "{sub_path}" as it is outside'
               f' the permitted working directory'))
    if not os.path.isdir(full_path):
        return Exception((f'Error: "{sub_path}" is not a directory'))
    return (full_path)

def _validate_file_read(full_path: str, working_directory: str, sub_path: str)\
    -> Union[str,Exception]:
    if not working_directory in full_path or '..' in full_path:
        return Exception((f'Error: Cannot read "{sub_path}" as it is outside'
                f' the permitted working directory'))
    if not working_directory in full_path or '..' in full_path:
        return Exception((f'Error: File not found or is not a regular file:'
                f' "{sub_path}"'))
    return (full_path)

def _validate_file_write(full_path: str, working_directory: str, sub_path: str)\
    -> Union[str,Exception]:
    if not working_directory in full_path or '..' in full_path:
        return Exception((f'Error: Cannot write to "{sub_path}" as it is'
                f' outside the permitted working directory'))
    dirname = os.path.dirname(full_path)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    return (full_path)

def _validate_file_run(full_path: str, working_directory: str, sub_path: str)\
    -> Union[str,Exception]:
    if not working_directory in full_path or '..' in full_path:
        return Exception((f'Error: Cannot execute "{sub_path}" as it is'
               f' outside the permitted working directory'))
    if not os.path.isfile(full_path):
        return Exception(f'Error: File "{sub_path}" not found')
    if not full_path[-3:] == '.py':
        return Exception(f'Error: "{sub_path}" is not a Python file.')
    return(full_path)
