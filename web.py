import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)

st.title ("Annas ToDo-App")
st.image ("todos_im.png", width=100)
#st.write("Deine ToDo-Liste:")



for index, i in enumerate(todos):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[i]
        st.experimental_rerun()

todo = st.text_input(label="", placeholder= "Gib dein ToDo ein.",
                     on_change=add_todo, key="new_todo")
#st.button("Hinzufügen")


