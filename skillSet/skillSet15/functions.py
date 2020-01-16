import os

def requirements():

    """This is a dosctring in the room of requirment. This docstring has
    been lost since the time Salizar Slytherin romed these halls."""


    print('''    1. Create write_read_file subdirectory with two filess: main.py and functions.py
    2. Use president Abraham Lincoln's Gettysburg Address: Full Text.
    3. Write address to file.
    4. Read address from same file
    5. Create Python Docstrings for functions in functions in functions.py
    6. display docstrings for functions in functions.py file
    7. Display full file path
    8. Replicate display below''')

def file_read():

    """Usage: Reads contents of a writen file
    Parameteres: None
    Returns speech variable"""
    with open('gettysburgaddress.txt') as address:
        abe = address.read()
    return abe

def write_file(spch: str):
    """Usage: creates new file and writes stored variable
    Parameters: txt variable
     Returns: None"""

    with open("newaddress.txt", 'w') as speech:
        speech.write(spch)

def write_read_file():

    """Usage: To execute read and write functions
    Parameters: None
    Returns: None"""

    spc = file_read()
    print(spc)
    write_file(spc)




def main():
    requirements()
    print()
    write_read_file()

    print('Path of the new file is: ', os.path.abspath("newaddress.txt"))


if __name__ == '__main__':
    pass



