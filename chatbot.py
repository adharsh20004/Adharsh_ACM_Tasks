import streamlit as st
import openai
import json
import os

# Get OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Sidebar setup
with st.sidebar:
    st.text("OpenAI API Key is set via environment variable")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    
    model = st.selectbox("Select model", ["gpt-3.5-turbo", "gpt-4"], index=0)

# Main title
st.title("💬 Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to the environment variables.")
        st.stop()
    
    if len(prompt) > 2048:
        st.warning("Input exceeds the 2048 character limit. Please shorten your input.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        openai.api_key = openai_api_key
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=150
        )
        msg = response.choices[0].text.strip()
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Add a button to download chat history
if st.button("Download Chat History"):
    chat_history = json.dumps(st.session_state.messages, indent=2)
    st.download_button("Download", chat_history, "chat_history.json", "application/json")
