import streamlit as st
import openai
from model import search
from googletrans import Translator

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']

openai.api_key = OPENAI_API_KEY

translator = Translator()

st.set_page_config(page_title="SAHAYAK-GPT", page_icon="🏛️", layout="wide")

st.markdown(
    '<p style="display:inline-block;font-size:40px;font-weight:bold;">SAHAYAK-GPT🏛️    </p> <p style="display:inline-block;font-size:16px;">-by TEAM OCEAN ASTRONAUTS</p> <p style="display:inline-block;font-size:16px;">"Hello, Im SAHAYAK-GPT, your government AI chatbot, here to assist you with information, services, and answers to your questions 24/7. How can I help you today"<br><br></p>',
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
            br = str(bot_response)
            final_response = br + "\n" + fr
            message_placeholder.markdown(final_response)
    st.session_state.messages.append({"role": "assistant", "content": final_response})

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)