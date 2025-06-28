from dataclasses import dataclass
from google.genai import types
from ai_integration.call_function import call_function
from ai_integration.runprompt import run_prompt
from typing import Union

@dataclass
class AiResponse:
    prompt_token_count: int
    candidates_token_count: int
    result: str

def get_content(user_prompt: str, is_verbose: bool) -> Union[AiResponse, Exception]:
    messages: list[types.ContentUnion] = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    response = run_prompt(messages)

    if response is None:
        return Exception("There was an error generating the response")
    if response.usage_metadata == None:
        return Exception("Usage data was unavailable")

    if not response.text is None and len(response.text) > 0:
        print(response.text)
    
    call_result = None
    if not response.function_calls is None:
        call_result = call_function(response.function_calls[0], is_verbose)

    if isinstance(call_result, Exception) or call_result is None or \
        call_result.parts is None or call_result.parts[0].function_response \
        is None or call_result.parts[0].function_response.response is None:
        return Exception("There was an error executing a tool call")

    result = call_result.parts[0].function_response.response['result']
    pt_count = -1 if response.usage_metadata.prompt_token_count is None \
                else response.usage_metadata.prompt_token_count
    ct_count = -1 if response.usage_metadata.candidates_token_count is None \
                else response.usage_metadata.candidates_token_count

    ai_response = AiResponse(result=result,
                            prompt_token_count=pt_count,
                            candidates_token_count=ct_count
                            )

    return ai_response
