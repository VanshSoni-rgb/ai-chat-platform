from abc import ABC, abstractmethod
from typing import List, Optional
from openai import OpenAI
from app.config.settings import OPENAI_API_KEY, AI_MODEL

class AIChatMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class AIPlatform(ABC):
    @abstractmethod
    def chat(self, prompt: str, history: Optional[List[AIChatMessage]] = None) -> str:
        pass

class OpenAIClient(AIPlatform):
    def __init__(self, system_prompt: str = None):
        self.system_prompt = system_prompt
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = AI_MODEL

    def chat(self, prompt: str, history: Optional[List[AIChatMessage]] = None) -> str:
        messages = []

        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})

        if history:
            for msg in history:
                messages.append({"role": msg.role, "content": msg.content})

        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message.content
