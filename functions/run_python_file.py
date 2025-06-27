from functions.helpers import validate_path, PathAction

def run_python_file(working_directory: str, file_path: str) -> str:
    err, validate_path = validate_path(working_directory, file_path, \
                                        PathAction.RUN_FILE)

