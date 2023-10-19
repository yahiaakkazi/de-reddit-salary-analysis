import openai


class LLM():
    def __init__(self, llm_model, system_request, user_request):
        while True:
            try:
                self.completion = openai.ChatCompletion.create(
                    model=llm_model,
                    messages=[
                        {"role": "system", "content": system_request},
                        {"role": "user", "content": user_request}
                    ],
                    temperature = 0
                )
                break
            except:
                print("Timedout, retrying...", end="\r")
                continue
    def get_message(self):
        return self.completion.choices[0].message.content