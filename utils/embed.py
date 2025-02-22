# from langchain_community.embeddings.huggingface import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

def vector_store(text_chunks):
    # embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-large')
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # embeddings = OllamaEmbeddings(model='gemma2:2b')
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


