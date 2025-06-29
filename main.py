import sys
from ai_integration.get_content import get_content

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

    print("Calling get_content")
    content_response = get_content(user_prompt, is_verbose)
    if isinstance(content_response, Exception):
        print(str(content_response))
        sys.exit(1)

    print('===========================================================')
    print(f"-> {content_response.result}")
    print('===========================================================')



if __name__=="__main__":
    main()
