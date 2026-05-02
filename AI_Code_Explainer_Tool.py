# AI Code Explainer Tool
# Objective: A tool that takes code as input and explains each line in simple language.

def explain_code(code):
    lines = code.split("\n")
    explanation = []

    print("AI Code Explainer Started\n")

    for i, line in enumerate(lines, start=1):
        line_lower = line.strip().lower()

        if "for" in line_lower and "range" in line_lower:
            explanation.append(
                f"Line {i}: This line starts a loop that runs multiple times.")

        elif "print" in line_lower:
            explanation.append(f"Line {i}: This prints output to the screen.")

        elif "=" in line_lower:
            explanation.append(
                f"Line {i}: This assigns a value to a variable.")

        elif "if" in line_lower:
            explanation.append(f"Line {i}: This checks a condition.")

        elif "def" in line_lower:
            explanation.append(f"Line {i}: This defines a function.")

        else:
            explanation.append(f"Line {i}: This is a code statement.")

    return explanation


while True:
    code_lines = []

    print("Enter your code (type 'done' to finish):")

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip().lower() == "done":
            break

        code_lines.append(line)

    if not code_lines:
        print("No code entered\n")
        continue

    code = "\n".join(code_lines)

    results = explain_code(code)

    print("\nExplanation:")
    for r in results:
        print(r)

    choice = input(
        "\nDo You Want Me To Tell More Code(yes/no): ").lower()
    if choice == "exit":
        print("Thanks For Using")
        break
