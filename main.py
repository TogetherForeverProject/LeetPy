import argparse
import importlib
import os
from rich import print
import re
import sys
import io

def get_input_comment(problem_file):
    with open(problem_file, "r") as f:
        code = f.read()
        match = re.search(r'# Input:(.*?)\ndef main\(\):', code, re.DOTALL)
        if match:
            return match.group(1).strip()
    return None


def get_title_from_file(problem_folder):
    info_file = os.path.join(problem_folder, "info.txt")
    if os.path.isfile(info_file):
        with open(info_file, "r") as f:
            for line in f:
                if line.startswith("Title:"):
                    return line.strip().replace("Title:", "").strip()
    return None


def get_category_from_file(problem_folder):
    info_file = os.path.join(problem_folder, "info.txt")
    if os.path.isfile(info_file):
        with open(info_file, "r") as f:
            for line in f:
                if line.startswith("Category:"):
                    return line.strip().replace("Category:", "").strip()
    return None


def get_question_from_file(problem_folder):
    info_file = os.path.join(problem_folder, "info.txt")
    if os.path.isfile(info_file):
        with open(info_file, "r") as f:
            found_question = False
            question_lines = []
            for line in f:
                if found_question:
                    question_lines.append(line.strip())
                elif line.strip().startswith("Question:"):
                    found_question = True
                    question_lines.append(line.strip().replace("Question:", "").strip())
            return "\n".join(question_lines)
    return None

def run_problem(problem_number):
    problem_folder = f"problems/problem{problem_number}"
    problem_file = f"problems/problem{problem_number}/solution.py"

    if not os.path.isfile(problem_file):
        print(f"[bold red]Error:[/bold red] Problem file 'problem{problem_number}.py' not found.")
        return None

    title = get_title_from_file(problem_folder)
    if title:
        print(f"[b #89b4fa]Problem {problem_number}[/b #89b4fa] │ {title}")
    else:
        print(f"[b #89b4fa]Problem {problem_number}[/b #89b4fa]")

    print("[blink]────────────────────────────────────────[/blink]")

    category = get_category_from_file(problem_folder)
    if category:
        print(f"[b #cba6f7]Category:[/b #cba6f7] [#cdd6f4]{category}[/#cdd6f4]")
    else:
        print(f"[b #cba6f7]Category:[/b #cba6f7] [#cdd6f4]None[/#cdd6f4]")

    question = get_question_from_file(problem_folder)
    if question:
        print(f"[b #f38ba8]Question:[/b #f38ba8] [#cdd6f4]{question}[/#cdd6f4]")

    input_comment = get_input_comment(problem_file)
    if input_comment:
        print(f"[b #b4befe]Input:[/b #b4befe] [#cdd6f4]{input_comment}[/#cdd6f4]")

    # Capture the standard output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    module = importlib.import_module(f"problems.problem{problem_number}.solution")
    module.main()

    # Get the captured output
    output = sys.stdout.getvalue().strip()

    # Restore the standard output
    sys.stdout = old_stdout

    print(f"[b #a6e3a1]Output:[/b #a6e3a1] {output}", end=" ")

    return output


def main():
    parser = argparse.ArgumentParser(description="Run LeetCode Problems")
    parser.add_argument("-P", "--problem", type=int, required=True, help="Problem number to run")
    args = parser.parse_args()

    run_problem(args.problem)

    # print("\n[bold green]Finished![/bold green]")


if __name__ == "__main__":
    main()
