import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app will increase my productivity")

for i, todo in enumerate(todos):
    st.checkbox(todo, key=i)

#for todo in todos:
#    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...")