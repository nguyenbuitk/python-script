import streamlit as st
from functools import partial

# Define a callback function that accepts parameters
def on_checkbox_change(task_name):
    print("task_name: ",task_name)
    if st.session_state[task_name]:
        st.write(f"{task_name} is checked!")
    else:
        st.write(f"{task_name} is unchecked.")

# Example tasks
tasks = ["Task 1", "Task 2", "Task 3"]

# Create checkboxes for each task with a callback and pass task name as a parameter
for task in tasks:
    # If using as follow, on_checkbox_change(task) is evaluated immediately, which triggers the function and tries to access st.session_state[task] before it’s actually created by the checkbox.
    
    #  st.checkbox(task, key=task, on_change=on_checkbox_change(task))
    st.checkbox(task, key=task, on_change=on_checkbox_change, args=(task,))
