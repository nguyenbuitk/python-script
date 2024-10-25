import streamlit as st
import functions
todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in  enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    print(checkbox)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
new_todo = st.text_input(label="", placeholder="Add new todo ... ")
if st.button("Add"):
    todos.append(new_todo + "\n")
    functions.write_todos(todos)
    st.rerun()

print("session_state", st.session_state)