import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todolist',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# list of py.simplegui object instances
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))


while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if event == "Add":
        todolist = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todolist.append(new_todo)
        functions.write_todos(todolist)
        window['todolist'].update(values=todolist)
    elif event == "Edit":
        try:
            todo_to_edit = values['todolist'][0]
            new_todo = values['todo']

            todolist = functions.get_todos()
            index = todolist.index(todo_to_edit)
            todolist[index] = new_todo
            functions.write_todos(todolist)
            window['todolist'].update(values=todolist)
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Complete":
        try:
            todo_to_complete = values['todolist'][0]
            todolist = functions.get_todos()
            todolist.remove(todo_to_complete)
            functions.write_todos(todolist)
            window['todolist'].update(values=todolist)
            window['todo'].update(values='')
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Exit":
        break
    elif event == 'todolist':
        window['todolist'].update(values=values['todolist'][0])
    elif event == sg.WIN_CLOSED:
        break


window.close()
