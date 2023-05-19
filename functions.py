FILEPATH = "todolist.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.read().splitlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file """
    todos_arg = [arg + '\n' for arg in todos_arg]
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# __name__ is actually the string "__main__" you get when you run functions.py directly
# if you run TodoApp the value of __name__ is "functions" file name
# so, if run the functions.py file directly, suddenly __name__ then equals == __main__,
# making the below if statement true, and printing out the following print statements
# this is useful when testing web applications, to test different outputs in the code whilst
# leaving the main file untouched


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
