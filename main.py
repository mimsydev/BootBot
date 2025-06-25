import sys
from google.genai import types
from funcitons.runprompt import run_prompt
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

    messages: list[types.ContentUnion] = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = run_prompt(messages)

    if response == None:
        print("There was an error generating the response")

    print(response.text)

    if response.usage_metadata == None:
        print("Usage data was unavailable")

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__=="__main__":
    main()
