from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--root", default=".")
args = parser.parse_args()

root = Path(args.root)
text = Path(args.input_file).read_text(encoding="utf-8")

current_file = None
buffer = []

def save():
    if current_file is None:
        return

    path = root / current_file
    path.parent.mkdir(parents=True, exist_ok=True)

    content = "\n".join(buffer).rstrip() + "\n"
    path.write_text(content, encoding="utf-8")

    print(f"Created: {path}")

for line in text.splitlines():

    if line.startswith("=== FILE: ") and line.endswith(" ==="):

        save()

        current_file = line[len("=== FILE: "):-len(" ===")]

        buffer = []

        continue

    buffer.append(line)

save()

print("Done.")