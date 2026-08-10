from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    ROOT / "student-work" / "answers.md",
    ROOT / "student-work" / "reflection.md",
]

PLACEHOLDERS = [
    "[Enter your full name]",
    "[Enter your GitHub username]",
    "[Enter your class and college]",
    "[Enter the date]",
    "[Write your answer here]",
    "[Write your explanation here]",
    "[Answer]",
    "[Step 1]",
    "[Step 2]",
    "[Step 3]",
    "[Write 2–4 sentences]",
    "[Write your question here]",
]

errors = []
template_mode = "--template" in sys.argv
for file_path in REQUIRED_FILES:
    if not file_path.exists():
        errors.append(f"Missing required file: {file_path.relative_to(ROOT)}")
        continue
    content = file_path.read_text(encoding="utf-8")
    for placeholder in PLACEHOLDERS:
        if not template_mode and placeholder in content:
            errors.append(
                f"Complete or replace {placeholder!r} in {file_path.relative_to(ROOT)}"
            )

if template_mode and not errors:
    print("Template validation passed.")
    print("Required assignment files are present and ready for students.")
    sys.exit(0)

if errors:
    print("Submission check failed:\n")
    for error in errors:
        print(f"- {error}")
    print("\nComplete the listed fields, commit the corrections and push again.")
    sys.exit(1)

print("Submission structure check passed.")
print("Required files exist and the main placeholders have been completed.")
print("Technical correctness will be assessed by Prof. Dattaraj Vidyasagar.")
