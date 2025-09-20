import streamlit as st

st.title("Rectangle Area Calculator")
name = st.text_input("Enter your name")
st.write("Hello", name)

width =st.number_input("Enter the width", 0)
height =st.number_input("Enter the height", 0)
if st.button("Calculate Area"):
    area = width * height
    st.write("Area =", area)