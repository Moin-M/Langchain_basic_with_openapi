##Integrate our code with openai
import os
from constant import openai_key
from langchain.llms import OpenAI

import streamlit as st
os.environ['OPENAI_API_KEY'] = openai_key
#initialize the streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Search the Topic you want")

##OPENAI LLMS
llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
