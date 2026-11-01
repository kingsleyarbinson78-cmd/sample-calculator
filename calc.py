import streamlit as st

st.title("My Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

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
            st.error("Cannot divide by zero!")
            result = None

    if result is not None:
        st.success(f"Result: {result}")