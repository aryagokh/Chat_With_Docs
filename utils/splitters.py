from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        separators='\n',
        chunk_size=1000,
        chunk_overlap=100,
    )
    chunks = splitter.split_text(text)
    return chunks