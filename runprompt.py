import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

def run_prompt(messages: list[types.ContentUnion]) -> types.GenerateContentResponse | None:

    load_dotenv()
    api_key: str | None = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        print("API KEY COULD NOT BE FOUND")
        return

    client = genai.Client(api_key=api_key)
    return client.models.generate_content(model="gemini-2.0-flash-001",\
                                             contents=messages)
