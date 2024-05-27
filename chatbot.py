import streamlit as st
import openai
import json

# Sidebar setup
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
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
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    
    if len(prompt) > 2048:
        st.warning("Input exceeds the 2048 character limit. Please shorten your input.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        openai.api_key = openai_api_key
        response = openai.ChatCompletion.create(
            model=model,
            messages=st.session_state.messages
        )
        msg = response.choices[0].message["content"]
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
    except openai.error.OpenAIError as e:
        st.error(f"An error occurred: {e}")

# Add a button to download chat history
if st.button("Download Chat History"):
    chat_history = json.dumps(st.session_state.messages, indent=2)
    st.download_button("Download", chat_history, "chat_history.json", "application/json")
