# Author: Ashish Soni
# Last Modified: 16/02/2024
# Description: This file is the main file for the streamlit app
#################################################################################
# Built-In modules
import os

# Community modules
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

from openai import OpenAI

import requests

import streamlit as st
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac
from streamlit_lottie import st_lottie
from streamlit_extras.add_vertical_space import add_vertical_space

# User-Defined modules
from constants import (LANGCHAIN_API_KEY, 
                       LANGCHAIN_URL,
                       LANGCHAIN_PROJECT,
                       PINECONE_API_KEY)

from models import (gpt35_turbo_llm,
                    gpt4_llm,
                    gpt4_turbo_llm,
                    gpt4_vision_llm
                    )

from utils import load_lottieurl

# Set environment variables to enable logging and tracing in LangSmith 
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = LANGCHAIN_URL
os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT
#################################################################################
i
# Page Configuration
st.set_page_config(
    page_title="Sophia - Digital Realm",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Report a bug': "https://github.com/Ashish-Soni08/NextGen-GPT-AI-Hackathon/issues",
        'About': "# This is a header. This is an *extremely* cool app!" # TODO: Write a good about message 
    }
)

############# SIDE BAR #############
lottie_anime = load_lottieurl("https://lottie.host/a8033181-195d-4419-a596-db1b2dd1f94a/mewB7EhHcc.json")

with st.sidebar:
    st_lottie(lottie_anime, height=230)
    st.markdown(
        """
    ## 
    **:blue[Sophia]** **Agile AI, Harmonizing Work and Personal Growth**
    """
    )
    
    sac.menu([
    sac.MenuItem('About the Author', icon='code-square', children=[
        sac.MenuItem('Github', icon='github', href="https://github.com/Ashish-Soni08"),
        sac.MenuItem('Twitter', icon='twitter', href="https://twitter.com/Ashish_Soni08"),
        sac.MenuItem('Linkedin', icon='linkedin', href="https://www.linkedin.com/in/soni-ashish-2091/"),
        sac.MenuItem('Hugging Face', icon='hypnotize', href="https://huggingface.co/Ashish08")
        ]),
    
        sac.MenuItem(type='divider'),
        
    sac.MenuItem('Built using', icon='wrench-adjustable-circle-fill', children=[
        sac.MenuItem('Clarifai', icon='c-circle-fill', href="https://www.clarifai.com/"),
        sac.MenuItem('Langchain', icon='tools', href="https://www.langchain.com/"),
        sac.MenuItem('Streamlit', icon='magic', href="https://streamlit.io/")
        ]),
    ], 
        size='lg', variant='filled', open_all=False) 
###################################

############# APP TITLE  #############
# Add CSS styling to center the title
st.markdown(
    """
    <style>
        .title {
            text-align: center; /* Center title text */
        }
    </style>
    """,
    unsafe_allow_html=True)

# Display the title in the middle of the page
st.markdown("<h1 class='title' style='color: purple;'><em>Sophia: The Magical Muse of Your Digital Realm</em> <br> <em>  </em></h1>", unsafe_allow_html=True)

###################################
sac.segmented(
    items=[
        sac.SegmentedItem(label='Code', icon='file-code-fill'),
        sac.SegmentedItem(label='Research', icon='search'),
        sac.SegmentedItem(label='Learn', icon='graph-up-arrow'),
        sac.SegmentedItem(label='Random', icon='chat-square-text-fill')
    ],  
        label='**What would you like to do today?**', 
        align='center',
        color='blue',
        use_container_width=True,
        key='sac.tasks'
)
# st.write(f"sac.buttons session value **{st.session_state['sac.tasks']}**")
client = OpenAI(api_key=OPENAI_API_KEY)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize the Chat History
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat messages from the chat history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# Display a different UI based on the user's selection
if st.session_state['sac.tasks'] == 'Code':
    st.write("Code")

elif st.session_state['sac.tasks'] == 'Research':
    st.write("Research")

elif st.session_state['sac.tasks'] == 'Learn':
    st.write("Learn")

elif st.session_state['sac.tasks'] == 'Random':
    st.write("Random")

# Get user input
if user_prompt := st.chat_input("Hello, I'm Sophia, your personal assistant 🌟. Let's make your day a breeze! How can I assist you today?"):
    # Display user message in chat message container
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)
    with st.chat_message("Sophia", avatar="images/Sophia.jpeg"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.chat_history
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.chat_history.append({"role": "Sophia", "content": full_response})