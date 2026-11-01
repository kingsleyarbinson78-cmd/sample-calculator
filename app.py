import streamlit as st

st.title("My First Application")

st.write("Welcome to my Streamlit app!")

name = st.text_input("Enter your name")

if name:
    st.write("Hello", name)

age = st.slider("Select your age", 1, 100, 18)

st.write("Your age is:", age)