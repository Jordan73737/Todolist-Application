import streamlit as st
import functions

todolist = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todolist.append(todo)
    functions.write_todos(todolist)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todolist.pop(index)
        functions.write_todos(todolist)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
