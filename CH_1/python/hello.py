#!/usr/bin/env python
"""
Author : The SWE Corner
Date   : 2024-04-30
Purpose: Say hello
"""

import argparse


def get_arguments():
    """Gets arguments"""
    parser = argparse.ArgumentParser(
        description="Says hello",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
        epilog = "Saying Hello Soon...")
    parser.add_argument('-n',
                        '--name',
                        default='World',
                        type = str,
                        help="Name to greet",
                        metavar='name')
    args = parser.parse_args()
    return args


def greetings(name):
    """Docstring, Pass a name to say hello"""
    print(f"Hello, {name}!")


def main():
    """Runs from here"""
    arguments = get_arguments()
    name = arguments.name
    greetings(name=name)


if __name__ == '__main__':
    """
    Once we add a function we need to add some order
    This is only needed once we run the code as a script
    The alternative is running in an interactive terminal like Jupyter
    """
    main()
