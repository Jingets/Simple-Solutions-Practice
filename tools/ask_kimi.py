from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import os
import sys

load_dotenv()

api_key = os.getenv("TOKENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("TOKENROUTER_API_KEY not found in .env")

client = OpenAI(
    base_url="https://api.tokenrouter.com/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser()
parser.add_argument("prompt_file", help="Markdown file with prompt")
args = parser.parse_args()

prompt_path = Path(args.prompt_file)

if not prompt_path.exists():
    print(f"File not found: {prompt_path}")
    sys.exit(1)

prompt = prompt_path.read_text(encoding="utf-8")

messages = [
    {
        "role": "system",
        "content": (
            "You are a senior software engineer. "
            "Follow the specification exactly. "
            "Do not invent architecture. "
            "Return only the requested result."
        ),
    },
    {
        "role": "user",
        "content": prompt,
    },
]

stream = client.chat.completions.create(
    model="moonshotai/kimi-k3-free",
    messages=messages,
    stream=True,
)

for chunk in stream:
    if chunk.choices:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)

print()