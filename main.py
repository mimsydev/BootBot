import os
import typing
import sys
from dotenv import load_dotenv
from google import genai

def main():
    args: list[str] = sys.argv
    if len(args) == 1:
        print("No prompt was provided. Please provide a prompt.")
        sys.exit(1)
    load_dotenv()
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        print("API KEY COULD NOT BE FOUND")
        return
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.0-flash-001",\
                                             contents="Why is Boot.dev such a great place to learn \
                                             backend development? Use paragraph.")
    print(response.text)
    if response.usage_metadata == None:
        print("Usage data was unavailable")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")



if __name__=="__main__":
    main()
