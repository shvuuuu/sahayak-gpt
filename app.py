import streamlit as st
import openai
from model import search
from googletrans import Translator

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY

translator = Translator()

st.set_page_config(page_title="Team Ocean Astronauts", page_icon="📁", layout="wide")

st.markdown(
    '<p style="display:inline-block;font-size:40px;font-weight:bold;">Team Ocean Astronauts</p> <p style="display:inline-block;font-size:16px;">With LlamaIndex&#39;s in-context learning approach, LlamaDoc leverages the reasoning capabilities of LLMs to provide accurate and insightful responses from a PDF file. <br><br></p>',
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How Can I Help You Today"):
    t_prompt = translator.translate(prompt)
    src_lang = t_prompt.src
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner('Thinking...'):
            result = search(t_prompt.text)
            message_placeholder = st.empty()
            full_response = result
            fr = str(full_response)
            t_response = translator.translate(fr, dest=src_lang)
            bot_response = t_response.text
            message_placeholder.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": result})

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)