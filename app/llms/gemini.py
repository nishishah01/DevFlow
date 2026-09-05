
import os
from google import genai

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ["GEMINI_API_KEY"]
        )

        self.model = "gemini-3.7-flash"

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        return response.text
# Don't instantiate Gemini independently inside every agent.

# Instead:

# Agent
#   ↓
# GeminiClient
#   ↓
# Gemini API

# This makes the LLM layer replaceable.

# Later you could have:

# GeminiClient
# OpenAIClient
# AnthropicClient
# MockLLMClient