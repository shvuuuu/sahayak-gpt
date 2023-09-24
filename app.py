import streamlit as st
import openai
import os
import time
from model import search
import random

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="Team Ocean Astronauts", page_icon="📁", layout="wide")

st.markdown(
    '<p style="display:inline-block;font-size:40px;font-weight:bold;">Team Ocean Astronauts</p> <p style="display:inline-block;font-size:16px;">With LlamaIndex&#39;s in-context learning approach, LlamaDoc leverages the reasoning capabilities of LLMs to provide accurate and insightful responses from a PDF file. <br><br></p>',
    unsafe_allow_html=True,
)


def save_uploadedfile(uploaded_file):
    with open(os.path.join("data", uploaded_file.name), "wb") as file:
        file.write(uploaded_file.getbuffer())
    return st.success("Saved File: {} to directory".format(uploaded_file.name))

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How Can I Help You Today"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner('Thinking...'):
            result = search(prompt)
            message_placeholder = st.empty()
            full_response = result
            message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": result})


hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)
