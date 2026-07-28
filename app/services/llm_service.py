from openai import OpenAI
from app.config import settings
from app.prompts import SYSTEM_PROMPT
from functools import lru_cache

class LLMService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.API_KEY,
            base_url=settings.BASE_URL
        )

    @lru_cache
    def get_llm():
        return LLMService()

    stream = self.client.chat.completions.create(
        model=settings.MODEL_NAME,
        stream=True,
        messages=messages
    )

    for chunk in stream:
        if chunk.choices:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta

#    def generate(self, prompt: str):
#       response = self.client.chat.completions.create(
#            model=settings.MODEL_NAME,
#            temperature=settings.TEMPERATURE,
#            messages=[
#                {
#                    "role": "system",
#                    "content": SYSTEM_PROMPT
#                },
#                {
#                    "role": "user",
#                    "content": prompt
#                }
#            ]
#        )

#        return response.choices[0].message.content