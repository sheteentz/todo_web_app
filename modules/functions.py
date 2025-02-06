FILEPATH = "todos.txt" #Constants written in UPPERCASE


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
    # it doesn't need to return anything, it behaves as a procedure


# An example of multi line text with triple quotes. No need to use \n break-line character.
text = """
Principles of productivity:
Managing your inflow.
Systemizing everything that repeats.
"""

"""
if you want to print this statement only when executed from this module
and not showing when calling functions module from main.
"""
if __name__ == "__main__":
    print("Hello from functions")