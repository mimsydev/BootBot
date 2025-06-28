import sys
from google.genai import types
from functions.call_function import call_function
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

    assert not response is None

    if not response.text is None and len(response.text) > 0:
        print(response.text)
    
    call_result = None
    if response.function_calls != None:
        call_result = call_function(response.function_calls[0], is_verbose)

    if isinstance(call_result, Exception) or call_result is None:
        print("There was an error executing a tool call")

    assert not call_result is None

    if call_result.parts[0].function_response.response is None:
        print("There was no response from the tool call")

    if response.usage_metadata == None:
        print("Usage data was unavailable")

    assert response.usage_metadata != None

    if is_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"-> {call_result.parts[0].function_response.response['result']}")



if __name__=="__main__":
    main()
