import streamlit as st
from transformers import pipeline

st.title("📜 What to Text Next?")

# Load text generation pipeline safely
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

user_input = st.text_input("Enter the topic, idea or context you want to text about:")

if st.button("Generate Text"):
    if user_input:
        output = generator(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        st.success(output)
    else:
        st.warning("Please enter something!")
