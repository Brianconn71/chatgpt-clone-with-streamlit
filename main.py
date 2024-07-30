import streamlit as st
import openai
import os
from dotenv import load_dotenv, find_dotenv


# we need to lad the env variables
load_dotenv(find_dotenv())

# need to set the openai api key
openai.api_key = os.environ["OPENAI_PASSWORD"]

# initialize chat model from openai api if not already set
if "" not in st.session_state:
    st.session_state["model"] = "gpt-3.5-turbo"

# use streamlit features to create user interface
# set title
st.title("Brian's ChatGPT")

# initialize a list to hold messages from chat session
if "messages" not in st.session_state:
    st.session_state.messages = []

# display exisiting chat histiry
# loop over list of messages and display each
# allows users to see conversation history when they refresh the page
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# process the user input
# create input field and once mesaage is submitted append to list
if user_prompt := st.chat_input("Your Question"):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

# generate and display chatgpt response
# send the list of messages to chatgpt
# once response is generated add to the list of messages
with st.chat_message("assistant"):
    message_placeholder = st.empty()
    full_response = ""
    for response in openai.ChatCompletion.create(
        model=st.session_state["model"],
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True
    ):
        full_response = response.choices[0].delta.get("content", "")
        message_placeholder.markdown(full_response + " ")
    
    message_placeholder.markdown(full_response)

st.session_state.messages.append({"role": "assistant", "content": full_response})

