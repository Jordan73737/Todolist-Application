import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todolist',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# list of py.simplegui object instances
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todolist = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['todos'].update(values=todolist)

    elif "Edit":
        todolist = values['todos'][0]
        new_todo = values['todo']

        todolist = functions.get_todos()
        index = todos.index(todo_to_edit)
        todolist[index] = new_todo
        functions.write_todos(todolist)
        window['todos'].update(values=todolist)
    elif 'todolist':
        window['todos'].update(values=values['todos'][0])
    elif sg.WIN_CLOSED:
        break


window.close()

