from typing import Optional
import openai
import g4f


class LLM:
    """class to initialise LLM and send requests to it"""

    def __init__(
        self, llm_model: str, system_request: str, user_request: str, use_g4f: bool
    ) -> None:
        self.use_g4f = use_g4f
        if self.use_g4f:
            self.completion = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": system_request + user_request}],
                stream=False,
            )
        else:
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
        """returns the reponse content"""
        if self.use_g4f:
            return self.completion
        return self.completion.choices[0].message.content
