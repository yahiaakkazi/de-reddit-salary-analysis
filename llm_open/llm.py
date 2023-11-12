from typing import Optional
import openai


class LLM:
    """class to initialise LLM and send requests to it"""

    def __init__(self, llm_model, system_request, user_request) -> None:
        while True:
            try:
                self.completion = openai.ChatCompletion.create(
                    model=llm_model,
                    messages=[
                        {"role": "system", "content": system_request},
                        {"role": "user", "content": user_request},
                    ],
                    temperature=0,
                )
                break
            except:
                print("Timedout, retrying...", end="\r")
                continue

    def get_message(self) -> Optional[str]:
        """returns the message content"""
        return self.completion.choices[0].message.content
