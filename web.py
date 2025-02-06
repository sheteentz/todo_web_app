import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will increase my productivity")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=i)

#for todo in todos:
#    st.checkbox(todo)

st.text_input(label="New todo", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")

st.session_state