FILEPATH="todos.txt"

#Costum Funktion festlegen
def get_todos(filepath=FILEPATH):
    """Gets the ToDos from the ToDo-File."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the ToDos in the ToDo-File."""
    with open(filepath,"w") as file_local:
        file_local.writelines(todos_arg)
