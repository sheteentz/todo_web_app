import streamlit as st
from modules import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will increase my <b>productivity</b>",
         unsafe_allow_html=True)#only write has html enabled in streamlit

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="New todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")