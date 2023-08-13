# FILEPATH = "files/todos.txt"
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Get the todos list"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def set_todos(todos, filepath=FILEPATH):
    """Set the todos list"""
    with open(filepath, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":
    """
     When run the function directly
    """
    print("Hello")
    print(get_todos("../files/todos.txt"))
