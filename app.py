# import streamlit as st

# st.title("To-Do List")

# task = st.text_input("Enter your task", " ")

# if st.button("Add Task"): 
#     if task:
#         st.session_state["task_list"].append(task)

# if "task_list" not in st.session_state:
#     st.session_state["task_list"] = []

# for i, t in enumerate(st.session_state["task_list"]):
#     st.write(f"{i + 1}. {t}")

# for i, t in enumerate(st.session_state["task_list"]):
#     if st.checkbox(f"{i + 1}. {t}"):
#         st.session_state["task_list"].remove(t)

#--------------------------------------------------------------#
import streamlit as st

st.title("To-Do List")

# Initialize the task list in session state if it doesn't exist
if "task_list" not in st.session_state:
    st.session_state["task_list"] = []

# Input field to add tasks
task = st.text_input("Enter your task", "")

# Button to add tasks
if st.button("Add Task"):
    if task.strip():  # Ensure the task is not empty
        st.session_state["task_list"].append(task.strip())

# Display tasks with remove buttons
st.write("### Your Tasks:")
for i, t in enumerate(st.session_state["task_list"]):
    col1, col2 = st.columns([4, 1])  # Create two columns: one for task, one for the remove button
    with col1:
        st.write(f"{i + 1}. {t}")  # Display the task
    with col2:
        # Remove button for the task
        if st.button("Remove", key=f"remove_{i}"):
            st.session_state["task_list"].pop(i)  # Remove the task
            st.experimental_rerun()  # Refresh the app to update the task list
