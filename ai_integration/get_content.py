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

    ai_response = None
    for i in range(20):
        print(f'Iteration {i}')
        print('Running run_prompt')
        response = run_prompt(messages)
        if isinstance(response, Exception):
            return response

        if response.usage_metadata is None:
            return Exception('Usage data was unavailable')

        if response.candidates is None:
            return Exception('Response candidates were "None"')

        for candidate in response.candidates:
            messages.append(candidate.content)
        
        call_result = None
        result = '' 

        if not response.function_calls is None:
            print('Running call_vunction')
            call_result = call_function(response.function_calls[0], is_verbose)

            if isinstance(call_result, Exception) or call_result is None or \
                call_result.parts is None or call_result.parts[0].function_response \
                is None or call_result.parts[0].function_response.response is None:
                return Exception("There was an error executing a tool call")

            messages.append(call_result)

            result = call_result.parts[0].function_response.response['result']

        pt_count = -1 if response.usage_metadata.prompt_token_count is None \
                    else response.usage_metadata.prompt_token_count
        ct_count = -1 if response.usage_metadata.candidates_token_count is None \
                    else response.usage_metadata.candidates_token_count

        ai_response = AiResponse(result=result,
                                prompt_token_count=pt_count,
                                candidates_token_count=ct_count
                                )
        if response.function_calls is None:
            ai_response.result = 'Empty response' if response.text is None \
                                    else response.text
            break

    if ai_response is None:
        return Exception('No response was generate')
    return ai_response
