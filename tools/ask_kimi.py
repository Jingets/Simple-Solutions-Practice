from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import argparse
import os
import sys
import time

load_dotenv()

api_key = os.getenv("TOKENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("TOKENROUTER_API_KEY not found in .env")

client = OpenAI(
    base_url="https://api.tokenrouter.com/v1",
    api_key=api_key,
    timeout=60.0,
)

parser = argparse.ArgumentParser(
    description="Simple Solutions Practice AI Builder"
)

parser.add_argument(
    "prompt_file",
    help="Markdown file with task"
)

parser.add_argument(
    "--model",
    default="moonshotai/kimi-k3-free",
    help="LLM model"
)

parser.add_argument(
    "--output",
    help="Save response to file"
)

args = parser.parse_args()

prompt_path = Path(args.prompt_file)

if not prompt_path.exists():
    print(f"ERROR: file not found: {prompt_path}")
    sys.exit(1)

prompt = prompt_path.read_text(encoding="utf-8")

print(f"Prompt: {prompt_path}")
print(f"Characters: {len(prompt)}")
print(f"Model: {args.model}")
print("Sending request...")

start = time.perf_counter()

try:

    response = client.chat.completions.create(
        model=args.model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior software engineer.\n"
                    "Follow the specification exactly.\n"
                    "Do not invent architecture.\n"
                    "Return only the requested result."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

except Exception as e:
    print()
    print("REQUEST FAILED")
    print(type(e).__name__)
    print(e)
    sys.exit(1)

elapsed = time.perf_counter() - start

text = response.choices[0].message.content

print()
print("=" * 80)
print(text)
print("=" * 80)
print()

print(f"Completed in {elapsed:.2f} sec")

if args.output:
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")
    print(f"Saved to {output_path}")