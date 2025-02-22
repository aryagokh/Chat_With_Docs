import streamlit as st
from dotenv import load_dotenv
from utils.readers import get_file_text
from utils.splitters import get_text_chunks
from utils.embed import vector_store
from utils.chain import get_chain
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()

load_dotenv()

st.set_page_config(page_title="Chat With Multiple Documents", page_icon="./page_data/Book.png")
st.header("Chat With Multiple DOCS 📚")

if "convo" not in st.session_state:
    st.session_state.convo = None  

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.subheader("Your Documents")
    uploaded_docs = st.file_uploader("Upload files here and Click Process", accept_multiple_files=True, type=["pdf", "docx", "txt"])

    if uploaded_docs and st.button("Process Files"):
        with st.spinner("Processing..."):
            try:
                extracted_text = get_file_text(uploaded_docs)
                chunks = get_text_chunks(extracted_text)
                vectorstore = vector_store(chunks)
                st.session_state.convo = get_chain(vectorstore)
                st.success("Processing Complete! Start Asking Questions.")
            except Exception as e:
                st.error(f"Processing failed! {e}")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about your documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    result = ''
    if st.session_state.convo:
        try:
            response = st.session_state.convo.invoke(prompt)
            result = parser.parse(response)
        except Exception as e:
            result = f"Error invoking model: {e}"

    if result!='':
        st.session_state.messages.append({"role": "assistant", "content": result['answer']})
        with st.chat_message("assistant"):
            st.markdown(result['answer'])
    else:
        with st.chat_message("assistant"):
            st.markdown("UPLOAD AND PROCESS DOCUMENTS FIRST!")
