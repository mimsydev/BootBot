import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute python files with optional arguments (*args)
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

def run_prompt(messages: list[types.ContentUnion]) ->\
    types.GenerateContentResponse | None:
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description=("Lists files in the specified directory along with their "
        "sizes, constrained to the working directory."),
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description=("The directory to list files from, relative to "
                    "the working directory. If not provided, lists files in the "
                    "working directory itself."),
                ),
            },
        ),
    )

    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description=("Gets the contents of the a file similar to the 'cat' "
            "application, constrained to the working directory."),
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to be retreived.",
                ),
            },
        ),
    )

    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description=("Executes a provided python file. Limited to the working"
                     " directory."),
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the python file to be executed.",
                ),
                "*args": types.Schema(
                    type=types.Type.STRING,
                    description=("Any number of string arguments to pass to the "
                                "python file. For example 'main.py 3 + 5' would "
                                "result in a file_path of 'main.py' and args of "
                                "'3', '+', '5'"
                                )
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description=("Writes the contents to a file at the specified file path."
                     " Creates the file at the path if it does not exist."
                     " Constrined to the working directory."),
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file to write to.",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The text content to write to the file"
                ),
            },
        ),
    )


    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    load_dotenv()
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        print("API KEY COULD NOT BE FOUND")
        return

    client = genai.Client(api_key=api_key)
    return client.models.generate_content(model="gemini-2.0-flash-001",
                                          contents=messages,
                                          config=types.GenerateContentConfig( 
                                          tools=[available_functions],
                                          system_instruction=SYSTEM_PROMPT
                                          )
                                          )
