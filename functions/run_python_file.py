import subprocess
from functions.helpers import validate_path, PathAction

def run_python_file(working_directory: str, file_path: str) -> str:
    full_path = validate_path(working_directory, file_path, PathAction.RUN_FILE)
    if isinstance(full_path, Exception):
        msg = str(full_path)
        if 'Error: ' in msg:
            return msg
        return f'Error: {msg}'
    
    try:
        result = subprocess.run(['python3', full_path], timeout=30, \
                                capture_output=True, text=True, check=True)
        msg = str()
        if len(result.stdout) > 0:
            msg += f'STDOUT: {result.stdout} '
        if len(result.stderr) > 0:
            msg += f'STDERR: {result.stderr}'
        if len(msg) == 0:
            return 'No output produced'
        return msg
    except subprocess.CalledProcessError as exex:
        error_string = f'STDERR: {exex.stderr}'
        if exex.returncode > 0:
            error_string += f' Process exited with code {exex.returncode}'
        return error_string
    except subprocess.TimeoutExpired as tex:
            return (f'Error: execution timed out for {file_path}. '
                    f'Exception: {str(tex)}')
    except Exception as e:
        return f'Error: executing python file {e}'

