from openai import OpenAI
from app.config import settings
from app.prompts import SYSTEM_PROMPT

class LLMClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.API_KEY,
            base_url=settings.BASE_URL
        )

    def ask(self, prompt: str):
        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content