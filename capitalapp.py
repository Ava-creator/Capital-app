import streamlit as st

st.title("Ava-s capital App 😘😘😘")

user_input = st.text_input("Enter a Word or a Sentence📖:")
if user_input:
    st.write(f"Original String: {user_input}")
    if st.button("Make it Uppercase"):
        st.write(user_input.upper())
    if st.button("Make it Lowercase"):
        st.write(user_input.lower())
    if st.button("Backword String"):
        st.write(user_input[::-1])
    if st.button("Find the Length"):
        st.write(len(user_input))