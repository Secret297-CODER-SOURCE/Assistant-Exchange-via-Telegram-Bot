import openai

class Assistant:
    def __init__(self,message):
        self.result = openai.OpenAI(api_key="").chat.completions.create(
            messages=[{"role": "user","content": message}],model="gpt-4o",
        )