import sys
from google.genai import types
from ai_integration.call_function import call_function
from ai_integration.get_content import get_content
from ai_integration.runprompt import run_prompt
from functions.get_files_info import get_files_info

def main():
    args: list[str] = sys.argv
    if len(args) <= 1:
        print("No prompt was provided. Please provide a prompt.")
        sys.exit(1)

    is_verbose = False
    if "--verbose" in args:
        args.remove("--verbose")
        is_verbose = True
    if "-v" in args:
        args.remove("-v")
        is_verbose = True

    user_prompt = args[1]

    content_response = get_content(user_prompt, is_verbose)
    if isinstance(content_response, Exception):
        print(str(content_response))
        sys.exit(1)

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {content_response.prompt_token_count}")
        print(f"Response tokens: {content_response.candidates_token_count}")
        print(f"-> {content_response.result}")



if __name__=="__main__":
    main()
