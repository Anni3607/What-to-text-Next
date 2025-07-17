import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="What to Text Next", page_icon="💬")
st.title("💬 What to Text Next")
st.markdown("Enter a message and get a reply based on the tone you want!")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

def generate_reply(user_message, tone):
    prompt = f"Reply {tone} to: '{user_message}'\nResponse:"
    response = generator(prompt, max_length=60, num_return_sequences=1)
    return response[0]["generated_text"].split("Response:")[-1].strip()

user_input = st.text_input("📨 Enter the message you received:")
tone = st.radio("🎭 Choose tone of your reply:", ['positive', 'negative'])

if st.button("💡 Suggest a Reply"):
    if user_input:
        with st.spinner("Generating reply..."):
            reply = generate_reply(user_input, tone)
        st.success(f"💬 Suggested Reply: {reply}")
    else:
        st.warning("Please enter a message.")
