import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="SakhiCopilot")
st.title("🌾 SakhiCopilot – AI for Women SHGs")

query = st.text_input("Ask your business question (in Hindi/English)")

if st.button("Ask"):
    response = generate_response(query)
    st.success(response)
