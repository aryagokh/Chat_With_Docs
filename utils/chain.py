from langchain.memory.buffer import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.llms import Ollama
import os
from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

# api_key = os.getenv('GPOQ_API_KEY')
api_key = st.secrets['GROQ_API_KEY']

def get_chain(vectorstore):
    # llm = Ollama(model='gemma2:2b')
    llm = ChatGroq(model='llama-3.3-70b-versatile', api_key=api_key)
    memory = ConversationBufferMemory(memory_key='chat_history',
                                      return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
    )
    return chain
    