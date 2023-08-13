import streamlit as stl
import modules.functions as fct

todos = fct.get_todos()


def add_todo():
    new_todo = stl.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    fct.set_todos(todos)


stl.title("My Todo App")
stl.subheader("This is my todo app.")
stl.write("This app is to increase your productivity!")

for index, todo in enumerate(todos):
    checkbox = stl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fct.set_todos(todos)
        del stl.session_state[todo]
        stl.experimental_rerun()


stl.text_input(label="", placeholder="Enter a todo...",
               on_change=add_todo, key="new_todo")


stl.session_state
