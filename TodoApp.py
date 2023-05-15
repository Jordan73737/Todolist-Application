todolist = []

while True:
    # Get user input and strip space characters from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action == "add":
            todo = input("Enter a todo: ") + "\n" #break line

            #we could use the following 3 lines but instead we will use 'with'
            #file = open('todolist.txt', 'r')
            #todolist = file.readlines()
            #file.close()

            #using the with context manager we do not need to write the close file line
            with open('todolist.txt', 'r') as file:
                todolist = file.readlines()

            todolist.append(todo)

            with open('todolist.txt', 'w') as file:
                file.writelines(todolist)

    elif user_action == "show":

            with open('todolist.txt', "r") as file:
                todolist = file.readlines()

            # to remove spaces in between list items we can do this:
            ### new_todos = [item.strip('\n') for item in todolist]
            # or we can just write item = item.strip('\n') as shown below

            # then amend the enumerate for new_todos only
            for index, item in enumerate(todolist):
                item = item.strip('\n')
                #to be more client friendly we say index starts with 1
                row = f"{index + 1}.{item.capitalize()}"
                print(row)
            print(f"The length of the list is {index + 1}")

    elif user_action == "edit":
        number = int(input("Number of the todo you would like to edit: "))
        # user does not know that list starts with index 0 instead of 1
        # so, we adjust for this and say number (which could be 1) -1 so its then 0
        number = number - 1

        with open('todolist.txt', "r") as file:
            todolist = file.readlines()

        newtodo = input("Enter new todo: ")
        #had to add in \n since it didn't have that when I ran it the first time
        todolist[number] = newtodo + '\n'

        with open('todolist.txt', 'w') as file:
            file.writelines(todolist)

    elif user_action == "complete":
        number = int(input("Number of the todo to complete: "))

        with open('todolist.txt', "r") as file:
            todolist = file.readlines()
        index = number - 1
        todo_to_remove = todolist[index].strip('\n')
        todolist.pop(index)

        with open('todolist.txt', 'w') as file:
            file.writelines(todolist)

        message = f"Todo: '{todo_to_remove}' was removed from the list"
        print(message)

    elif user_action == "exit":
        break

    else:
        input("Please type either add, show or exit: ")
