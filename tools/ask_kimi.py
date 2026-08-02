from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("TOKENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("TOKENROUTER_API_KEY not found in .env")

client = OpenAI(
    base_url="https://api.tokenrouter.com/v1",
    api_key=api_key,
)

messages = [
    {
        "role": "system",
        "content": (
            "You are a senior software engineer. "
            "Generate production-quality code only."
        ),
    },
    {
        "role": "user",
        "content": "Who are you?",
    },
]

stream = client.chat.completions.create(
    model="moonshotai/kimi-k3-free",
    messages=messages,
    stream=True,
    stream_options={"include_usage": True},
)

print()

for chunk in stream:

    if chunk.choices:

        delta = chunk.choices[0].delta

        if delta.content:
            print(delta.content, end="", flush=True)

print()