from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file")
parser.add_argument("--root", default=".")
args = parser.parse_args()

root = Path(args.root)
text = Path(args.input_file).read_text(encoding="utf-8")

current_name = None
current_lines = []

def save_file():
    if current_name is None:
        return

    path = root / current_name
    path.parent.mkdir(parents=True, exist_ok=True)

    content = "\n".join(current_lines).rstrip() + "\n"
    path.write_text(content, encoding="utf-8")

    print(f"✓ {current_name}")

for line in text.splitlines():

    if line.startswith("=== FILE: ") and line.endswith(" ==="):

        save_file()

        current_name = line[10:-4].strip()

        current_lines = []

        continue

    current_lines.append(line)

save_file()

print("Done.")