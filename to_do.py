import streamlit as st

# Title of the app
st.title("To-Do List App")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Input box for adding new tasks
new_task = st.text_input("Add a new task:", "")

# Button to add a task
if st.button("Add Task"):
    if new_task.strip():
        st.session_state.tasks.append(new_task.strip())
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Task cannot be empty.")

# Display the list of tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    # A new list to update tasks after removal
    updated_tasks = st.session_state.tasks[:]
    for i, task in enumerate(st.session_state.tasks):
        # Use columns for task display and remove button
        col1, col2 = st.columns([4, 1])
        with col1:
            st.write(f"{i + 1}. {task}")
        with col2:
            if st.button(f"Remove Task {i + 1}", key=f"remove-{i}"):
                updated_tasks.pop(i)
                break  # Break the loop to avoid modifying the list during iteration
    st.session_state.tasks = updated_tasks  # Update the session state
else:
    st.write("No tasks yet. Add a task to get started!")

# Option to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")
