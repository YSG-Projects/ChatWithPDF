from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import os
import streamlit as st

# Get API key from Streamlit Secrets
openai_key = st.secrets["OPENAI_API_KEY"]

def create_chatbot(vectordb):
    """
    Create a conversational chatbot chain that uses the vector DB for context.
    """
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=openai_key,
        model_name="gpt-3.5-turbo"
    )

    # Chain with memory of chat history
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectordb.as_retriever(),
        return_source_documents=True  # Optional: show sources
    )

    return qa_chain

