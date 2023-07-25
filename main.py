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

def get_title_comment(problem_file):
    with open(problem_file, "r") as f:
        code = f.read()
        match = re.search(r'# Title:(.*?)\n', code)
        if match:
            comment = match.group(1).strip()
            return comment
    return None

def get_main_comment(problem_file):
    with open(problem_file, "r") as f:
        code = f.read()
        match = re.search(r'#(.*?)(?=class Solution:)', code, re.DOTALL)
        if match:
            comment = match.group(1).strip()
            # Exclude any comments after the class definition
            comment = re.sub(r'Input:.*$', '', comment, flags=re.MULTILINE)
            comment = re.sub(r'Title:.*$', '', comment, flags=re.MULTILINE)
            comment = re.sub(r'from.*$', '', comment, flags=re.MULTILINE)
            comment = '\n'.join(line.lstrip('#').strip() for line in comment.splitlines())
            return comment.strip()
    return None


def run_problem(problem_number):
    problem_file = f"problems/problem{problem_number}.py"

    if not os.path.isfile(problem_file):
        print(f"[bold red]Error:[/bold red] Problem file 'problem{problem_number}.py' not found.")
        return None

    title = get_title_comment(problem_file)
    if title:
        print(f"[bold cyan]Problem {problem_number}[/bold cyan] │ {title}")
    else:
        print(f"[bold cyan]Problem {problem_number}[/bold cyan]")

    print("────────────────────────────────────────")

    main_comment = get_main_comment(problem_file)
    if main_comment:
        print(f"[bold yellow]Question:[/bold yellow] {main_comment}")

    input_comment = get_input_comment(problem_file)
    if input_comment:
        print(f"[bold cyan]Input:[/bold cyan] {input_comment}")

    # Capture the standard output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    module = importlib.import_module(f"problems.problem{problem_number}")
    module.main()

    # Get the captured output
    output = sys.stdout.getvalue().strip()

    # Restore the standard output
    sys.stdout = old_stdout

    print(f"[bold magenta]Output:[/bold magenta] {output}", end=" ")

    return output


def main():
    parser = argparse.ArgumentParser(description="CLI tool to run specific problem files")
    parser.add_argument("-P", "--problem", type=int, required=True, help="Problem number to run")
    args = parser.parse_args()

    run_problem(args.problem)

    # print("\n[bold green]Finished![/bold green]")


if __name__ == "__main__":
    main()
