import streamlit as st

# Title of the app
st.title("Basic Calculator App")

# Input fields
st.header("Enter two numbers:")
num1 = st.number_input("First Number", value=0.0, step=0.1)
num2 = st.number_input("Second Number", value=0.0, step=0.1)

# Select operation
operation = st.selectbox(
    "Choose an operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Perform calculation based on the selected operation
result = None
if operation == "Addition":
    result = num1 + num2
elif operation == "Subtraction":
    result = num1 - num2
elif operation == "Multiplication":
    result = num1 * num2
elif operation == "Division":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."

# Display result
if st.button("Calculate"):
    st.subheader("Result:")
    st.write(result)
