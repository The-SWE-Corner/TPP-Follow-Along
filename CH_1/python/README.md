# Chapter 1 
## Introduction

- Shebang:
    - Add a shebag line whe we are running to tell OS what python interpreter,e.g to use the environment python, to run the script, give it the directory location
    - **Allows us to run the code as a ./** rather than using the programming language which already has a path.
    E.g 
    ```bash
    ./hello.py

    not 

    Python hello.py
    ```
    - The OS looks in the PATH 
    - We can append a new env to the PATH **or** add the program to the locations searched in our PATH
    - Hint it starts with the comment which essentially comments out that line but it is still interpreted because of the location?
    - The **PATH** is one of the environment variables (An env variable stored data about certain system informations). Example you can create an environment variable for AIRFLOW_HOME if you use Airflow. Hoever this information does not persist by default. But persitence can be enabled.
- Testing a file
    We will test using pytest
    ```
    pytest -vx test_file_name
    ```
    - -v for verbose
    - -x for stop on the first failure
    - -q for quiet,...
    - The - shows the expected and the + shows the actual
- Using Makefile
    - when the file and recipe have the same name use .PHONY
    - [more](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html)
- Arguments
    - We can parse arguments in so many ways using
        - Sys.argvs: do not need to install anything uses the sys library only con is not versatile
        - Argeparse: offers more functionality, contains an automatic help message [official doc](https://docs.python.org/3/library/argparse.html)
        - ..
    - There are different argument types [more](./python_arguments.md)
        - Positional: relevant in order of their position to the executable(file/script run)
        - Keyword Arguments: These are arguments that are passed as key/value pairs in the format argument_name = argument_value
        - Optional Arguments: not required can be ommitted. **Not necessarily a keyword argument**
- if __name__ == "__main__"
    - This tells the python interpreter where to execute the shource file from. See this example
    ```python
    print ("Always executed")
    
    if __name__ == "__main__": 
        print ("Executed when invoked directly")
    else: 
        print ("Executed when imported")
    ```
- Linting
    - This are used for formatting the code
    - Options include
        - yapf
        - pylint
        - flake 8
        - black, ...
    - makes it consistent with community standard
    - mainly for proper documentation