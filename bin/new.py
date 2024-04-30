#!/usr/bin/env python3

"""
Author: The SWE Corner
Purpose: To create new Python programs
"""

import argparse
import os
import platform
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

from typing import NamedTuple, Dict


class Args(NamedTuple):
    """Input Validation Class"""

    program: str
    file: str
    name: str
    email: str
    purpose: str
    overwrite: bool


def get_args() -> Args:
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description="Create Python argparse program",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    defaults = get_defaults()
    username = os.getenv("USER") or "Anonymous"
    hostname = os.getenv("HOSTNAME") or "localhost"

    parser.add_argument("program", help="Program name", type=str)
    parser.add_argument("file", help="Temple content", 
                        type=argparse.FileType("rt"),
                        default=None)

    parser.add_argument(
        "-n",
        "--name",
        type=str,
        default=defaults.get("name", username),
        help="Name for docstring",
    )

    parser.add_argument(
        "-e",
        "--email",
        type=str,
        default=defaults.get("email", f"{username}@{hostname}"),
        help="Email for docstring",
    )

    parser.add_argument(
        "-p",
        "--purpose",
        type=str,
        default=defaults.get("purpose", "SWE the Corner"),
        help="Purpose for docstring",
    )

    parser.add_argument(
        "-f", "--force", help="Overwrite the existing", action="store_true"
    )

    args = parser.parse_args()
    args.program = args.program.strip().replace("-", "_")
    if not args.program:
        parser.error(f'Not a useable filename "{args.program}"')

    return Args(args.program, args.file, args.name, args.email, args.purpose, args.force)


def get_defaults() -> Dict:
    """Get defaults from ~/.new.py"""

    rc = os.path.join(str(Path.home()), ".new.py")
    defaults = {}
    if os.path.isfile(rc):
        with open(rc, encoding="utf-8") as f:
            for line in f:
                match = re.match("([^=]+)=([^=]+)", line)
                if match:
                    key, val = map(str.strip, match.groups())
                    if key and val:
                        defaults[key] = val

    return defaults


def main() -> None:
    """Runs from here"""
    args = get_args()
    program = args.program
    template = args.file

    if os.path.isfile(program) and not args.overwrite:
        is_overwrite = input(f'"{program}" exists. Overwrite? [yN]')
        if not is_overwrite.lower().startswith("y"):
            sys.exit("Will not overwrite. Bye!")

    # write out to the opened file
    # print("Template is ", template)
    # if not os.path.isfile(template):
    #     sys.exit(f"Body file: {template} has error")
        
    # print(generate_script_content(args), file=open(program, "wt"), end="")
    with open(program, "wt", encoding="utf-8") as f:
        print(generate_script_content(args), file=f, end="")

    # makes Linux/IOS executable
    if platform.system() != "Windows":
        subprocess.run(["chmod", "+x", program], check=True)
    print(f'Done, see new script "{program}".')


def generate_script_content(args: Args) -> str:
    """The program template"""
    today = str(date.today())
    with open(args.file.name, 'r') as f:
        template_content = f.read()
    content = template_content.format(today=today, purpose=args.purpose)

    return content


if __name__ == "__main__":
    main()
