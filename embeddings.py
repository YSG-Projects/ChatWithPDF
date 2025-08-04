from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import streamlit as st

# Get API key from Streamlit Secrets
openai_key = st.secrets["OPENAI_API_KEY"]

def create_vector_store(text: str) -> FAISS:
    """
    Splits text into chunks, generates OpenAI embeddings, 
    and stores them in a FAISS vector database.
    """
    # Split text into overlapping chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)

    # Generate embeddings using OpenAI
    embeddings = OpenAIEmbeddings(openai_api_key=openai_key)

    # Store vectors in FAISS index
    vectordb = FAISS.from_texts(chunks, embeddings)

    return vectordb

