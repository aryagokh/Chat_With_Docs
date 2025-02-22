from PyPDF2 import PdfReader
from docx import Document

def get_file_text(docs):
    text = ""
    
    for i, doc in enumerate(docs):
        file_extension = doc.name.split('.')[-1]
        text+=f"Doc {i+1} starts from here:\n{text}\n\n"
        
        if file_extension == 'pdf':
            pdf_reader = PdfReader(doc)
            for page in pdf_reader.pages:
                text += page.extract_text()
        
        elif file_extension == 'txt':
            text = doc.read().decode('utf-8')  

        elif file_extension == 'docx':
            docx = Document(doc)
            for para in docx.paragraphs:
                text += para.text + '\n'
        
    return text