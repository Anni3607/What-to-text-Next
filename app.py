import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="What to Text Next", page_icon="💬")
st.title("💬 What to Text Next")
st.markdown("Enter a message and get a reply based on the tone you want!")

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small")

generator = load_model()

def generate_reply(user_message, tone):
    prompt = f"Reply {tone} to: {user_message}"
    response = generator(prompt, max_length=60)[0]['generated_text']
    return response.strip()

user_input = st.text_input("📨 Enter the message you received:")
tone = st.radio("🎭 Choose tone of your reply:", ['positive', 'negative'])

if st.button("💡 Suggest a Reply"):
    if user_input:
        with st.spinner("Generating..."):
            reply = generate_reply(user_input, tone)
        st.success(f"💬 Suggested Reply: {reply}")
    else:
        st.warning("Please enter a message.")
