import sys
from google.genai import types
from functions.runprompt import run_prompt
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

    assert response != None

    if response.text != None and len(response.text) > 0:
        print(response.text)
    
    if response.function_calls != None:
        for function_call_part in response.function_calls:
            print((f'Calling function: {function_call_part.name}'
                f'({function_call_part.args})'))

    if response.usage_metadata == None:
        print("Usage data was unavailable")

    assert response.usage_metadata != None

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__=="__main__":
    main()
