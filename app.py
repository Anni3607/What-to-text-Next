import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="What to Text Next", page_icon="💬")

st.title("💬 What to Text Next")
st.markdown("Enter a message and get a reply based on the tone you want!")

# Load generator
generator = pipeline("text-generation", model="gpt2")

def generate_reply(user_message, tone):
    if tone == 'positive':
        prompt = f"Reply positively to: '{user_message}'\nResponse:"
    else:
        prompt = f"Reply negatively to: '{user_message}'\nResponse:"
    response = generator(prompt, max_length=60, num_return_sequences=1)
    reply = response[0]['generated_text'].split("Response:")[-1].strip()
    return reply

# UI
user_input = st.text_input("📨 Enter the message you received:")
tone = st.radio("🎭 Choose tone of your reply:", ['positive', 'negative'])

if st.button("💡 Suggest a Reply"):
    if user_input:
        reply = generate_reply(user_input, tone)
        st.success(f"💬 Suggested Reply: {reply}")
    else:
        st.warning("Please enter a message.")
