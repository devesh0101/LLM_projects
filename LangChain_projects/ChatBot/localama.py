from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st 
import os 
from dotenv import load_dotenv

load_dotenv()


## Prompt Template 

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant please response to user questions " ),
        ("user","Question:{question}")
        
    ]
)


## Streamlit framework 

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")


# Ollama LLm 
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))