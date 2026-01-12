import streamlit as st, requests

API = "http://127.0.0.1:8000/ask"
st.title("GenAI Knowledge Assistant")

q = st.text_input("Ask a question")
if st.button("Ask"):
    r = requests.post(API, json={"question": q})
    st.write(r.json()["answer"])

