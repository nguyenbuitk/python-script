import streamlit as st
import functions

# Load the to-do list from the file
todos = functions.get_todos()

# Display the title and subtitle of the app
st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

def on_change_checkbox(task_name):
    print("session state: ", st.session_state)
        

# Display the list of tasks with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo, on_change=on_change_checkbox, args=(todo,))

# Text input for new tasks and edit tasks
new_todo = st.text_input(label="", placeholder="Add new todo ... ")

# Button to add a new task
if st.button("Add"):
    todos.append(new_todo + "\n")
    functions.write_todos(todos)
    st.rerun()

# {"a\n":false,"c\n":true,"b\n":true}
if st.button("Complete"):
    todos = functions.get_todos()
    print("todos: ", todos)
    todos = [todo for todo in todos if st.session_state.get(todo) == False ]
    
    functions.write_todos(todos)
    for key, value in st.session_state.items():
        print(value)
        if value == True:
            del st.session_state[key]
    st.rerun()

if st.button('Edit'):
    count = 0
    
    for key, value in st.session_state.items():
        if value == True:
            count += 1
            todo_edited = key
    
    if count != 1:
        st.write("please select one item!")
    else:
        ## Update in files
        todos = [new_todo + '\n' if todo == todo_edited else todo for todo in todos]
        print("new_todo", new_todo)
        print("todo_edited", todo_edited)
        print("todos", todos)
        functions.write_todos(todos)
    st.rerun()
        
# Display current session state for debugging
# st.session_state
