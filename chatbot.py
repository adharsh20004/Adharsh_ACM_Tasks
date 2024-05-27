pip install openai streamlit
import streamlit as st
from openai import OpenAI, error
import json

# Sidebar setup
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    model = st.selectbox("Select model", ["gpt-3.5-turbo", "gpt-4"], index=0)

# Main title
st.title("Adharsh's Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How may I assist you?"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    
    if len(prompt) > 2048:
        st.warning("Input exceeds the 2048 character limit. Please shorten your input.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(model=model, messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    except error.OpenAIError as e:
        st.error(f"Uh oh, something went wrong.. : {e}")

# Add a button to download chat history
if st.button("Download Chat History"):
    chat_history = json.dumps(st.session_state.messages, indent=2)
    st.download_button("Download", chat_history, "chat_history.json", "application/json")

