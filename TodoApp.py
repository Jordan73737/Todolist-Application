# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    # Get user input and strip space characters from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todolist = functions.get_todos()

        todolist.append(todo + '\n')

        functions.write_todos(todolist)

    elif user_action.startswith("show"):

        todolist = functions.get_todos()

        for index, item in enumerate(todolist):
            item = item.strip('\n')
            # to be more client friendly we say index starts with 1
            row = f"{index + 1}.{item.capitalize()}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            # user does not know that list starts with index 0 instead of 1
            # so, we adjust for this and say number (which could be 1) -1 so its then 0
            print(number)
            number = number - 1

            todolist = functions.get_todos()

            newtodo = input("Enter new todo: ")
            # had to add in \n since it didn't have that when I ran it the first time
            todolist[number] = newtodo + '\n'

            functions.write_todos(todolist)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todolist = functions.get_todos()
            index = number - 1
            todo_to_remove = todolist[index].strip('\n')
            todolist.pop(index)

            functions.write_todos(todolist)

            message = f"Todo: '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        input("Command is not valid:")
