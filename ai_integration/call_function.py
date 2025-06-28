from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from google.genai import types
from typing import Union

def call_function(function_call_part: types.FunctionCall, verbose: bool = False)\
    -> Union[types.Content, Exception]:
    function_name = function_call_part.name
    if function_name is None:
        return Exception('Error: No function name was provided')

    assert not function_name is None

    function_args = function_call_part.args
    function_args['working_directory']='./calculator'
    if verbose:
        print((f'Calling function: {function_name}'
            f'({function_args})'))
    else:
        print(f' - Calling function: {function_name}')

    if function_name not in globals():
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    function_to_call = globals()[function_name]
    function_result = function_to_call(**function_args)
    
    return types.Content(
        role='tool',
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={'result': function_result},
            )
        ],
    )
