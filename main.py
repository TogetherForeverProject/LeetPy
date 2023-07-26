import argparse
import importlib
import os
import re
import sys
import io
import time

pprint = print
from rich import print
from rich.progress import track
from rich.panel import Panel
from rich.markdown import Markdown
from utils import superscript, subscript

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
    if not os.path.isfile(info_file):
        return None

    with open(info_file, "r") as f:
        found_question = False
        question_lines = []
        for line in f:
            if found_question or line.strip().startswith("Question:"):
                line = re.sub(r'<sub>(.*?)<\/sub>', lambda match: subscript(match.group(1)), line.strip())
                line = re.sub(r'<sup>(.*?)<\/sup>', lambda match: superscript(match.group(1)), line)
                question_lines.append(line.replace("Question:", "").strip())
                found_question = True

    return "\n".join(question_lines)


def loading(time_needed: int):
    for _ in track(range(time_needed), description="Compiling..."):
        time.sleep(1)

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    pprint(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)


def run_problem(problem_number):
    problem_folder = f"problems/problem{problem_number}"
    problem_file = f"problems/problem{problem_number}/solution.py"

    if not os.path.isfile(problem_file):
        print(f"[bold red]Error:[/bold red] Problem file 'problem{problem_number}.py' not found.")
        return None

    # Capture the standard output
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    module = importlib.import_module(f"problems.problem{problem_number}.solution")
    module.main()

    # Get the captured output
    title = get_title_from_file(problem_folder)
    category = get_category_from_file(problem_folder)
    question = get_question_from_file(problem_folder)
    input = get_input_comment(problem_file)
    output = sys.stdout.getvalue().strip()

    # Restore the standard output
    sys.stdout = old_stdout
    if title:
        print(f"[b #89b4fa]Problem {problem_number}[/b #89b4fa] │ [b #ffffff]{title}[/b #ffffff]")
    else:
        print(f"[b #89b4fa]Problem {problem_number}[/b #89b4fa]")

    print("[blink]────────────────────────────────────────[/blink]")

    if category:
        print(f"[b #cba6f7]Category:[/b #cba6f7] [#cdd6f4]{category}[/#cdd6f4]")
    else:
        print(f"[b #cba6f7]Category:[/b #cba6f7] [#cdd6f4]None[/#cdd6f4]")

    if question:
        question = Markdown(question)
        print(Panel(question, title="[b #f38ba8]Question[/b #f38ba8]"))

    if input:
        print(Panel(input, title="[b #b4befe]Input[/b #b4befe]"))

    print(Panel(output, title="[b #a6e3a1]Output[/b #a6e3a1]", highlight=True), end=" ")

    return output


def main():
    parser = argparse.ArgumentParser(description="Run LeetCode Problems")
    parser.add_argument("-P", "--problem", type=int, required=True, help="Problem number to run")
    args = parser.parse_args()
    loading(2)
    run_problem(args.problem)

    # print("\n[bold green]Finished![/bold green]")


if __name__ == "__main__":
    main()
