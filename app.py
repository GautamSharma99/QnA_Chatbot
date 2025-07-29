import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

## prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)
api_key=os.getenv('OPENAI_API_KEY')

def generate_response(question,llm,temperature,max_tokens):
    llm=ChatOpenAI(model=llm,api_key=api_key)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer


#title of the app
st.title("Enhanced Q&A Chatbot with OpenAI")

# sidebar for settings
st.sidebar.title("Settings")

#drop down to select various openai modela
llm = st.sidebar.selectbox("select an Open AI Model",["gpt-4o","gpt-4o-mini","gpt-4"])

# adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)


#main interaface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("please provide the query")