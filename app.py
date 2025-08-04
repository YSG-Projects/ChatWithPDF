import streamlit as st
from PDF_reader import read_pdf
from embeddings import create_vector_store
from chatbot import create_chatbot

st.set_page_config(page_title="Chat with PDF", layout="wide")

st.title("📄 ChatPDF Clone using GenAI")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading and processing the PDF..."):
        # Step 1: Extract text
        pdf_text = read_pdf(uploaded_file)

        # Step 2: Create vector store
        vectordb = create_vector_store(pdf_text)

        # Step 3: Initialize chatbot
        chatbot = create_chatbot(vectordb)

    st.success("PDF processed! Start chatting below.")

    # Chat UI
    chat_history = []

    # Store chat history in session
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_query = st.text_input("💬 Ask something about the PDF")

    if user_query:
        with st.spinner("Generating response..."):
            result = chatbot({
                "question": user_query,
                "chat_history": st.session_state.chat_history
            })

            response = result["answer"]
            st.session_state.chat_history.append((user_query, response))

    # Display chat
    for i, (q, a) in enumerate(reversed(st.session_state.chat_history[-5:]), 1):
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Bot:** {a}")
        st.markdown("---")

