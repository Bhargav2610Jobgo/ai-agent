import os
import re

base_dir = r"C:\Users\Asus\OneDrive\Desktop\Video SDK Plugin\ai-agent\.venv\Lib\site-packages\videosdk"

for root, _, files in os.walk(base_dir):
    for fname in files:
        if fname.endswith(".py"):
            path = os.path.join(root, fname)
            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            # Remove @dataclass decorator if applied to TypedDict or dict
            fixed = re.sub(
                r"@dataclass\s*\n(class .*TypedDict)",
                r"\1",
                code
            )
            fixed = re.sub(
                r"@dataclass\s*\n(class .*dict)",
                r"\1",
                fixed
            )

            if fixed != code:
                print("Patched:", path)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(fixed)
