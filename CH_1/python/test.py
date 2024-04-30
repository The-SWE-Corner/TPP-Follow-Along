"""test for hello.py"""

import os
from subprocess import getoutput, getstatusoutput

program = "./hello.py"

def test_exists():
    """Checks that it is a file and exists"""
    assert os.path.isfile(program)

def test_runnable():
    output = getoutput(f"python {program}")
    assert output.strip() == "Hello, World!"

def test_executable():

    """Run it without the python command"""
    output = getoutput(program)
    assert output.strip() == "Hello, World!"

def test_usage():

    for flag in ["-h", "--help"]:
        exitcode, output = getstatusoutput(f"{program} {flag}")
        assert exitcode == 0 # on success
        assert output.lower().startswith("usage")

def test_input():
    """Test with input"""
    test_vals = ['Universe', 'Multiverse']
    flags = ['-n', '--name']

    for val in test_vals:
        for flag in flags:
            exitcode, output = getstatusoutput(f"{program} {flag} {val}")
            assert exitcode == 0
            assert output.strip() == f'Hello, {val}!'