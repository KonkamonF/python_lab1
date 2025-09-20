import streamlit as st


name = st.text_input("Enter your name")
if st.button("save name"):
    st.write("Hello", name) 
    st.session_state["username"] = name