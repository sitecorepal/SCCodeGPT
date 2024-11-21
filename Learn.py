from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from pathlib import Path

code_files_path = Path("sc_code").resolve()

def get_documents(filenames):
    docs = []
    text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=4000,
            chunk_overlap=50,
            length_function=len,
            )
    for filename in filenames:
        loader = TextLoader(filename, encoding='utf8')
        content = loader.load()
        splits = text_splitter.split_documents(content)
        print(f"{filename} has {len(splits)} splits.")
        docs.extend(splits)
        print(f"{filename} added to index.")
    return docs


def get_document_information(dir_path):
    knowledge = []
    for root, dirs, files in os.walk(dir_path):
        dirs[:] = [d for d in dirs]
        for file in files:
            filepath = os.path.join(root, file)
            try:
                knowledge.extend(get_documents([filepath]))

            except Exception as e:
                print(f"Failed to process {filepath} due to error: {str(e)}")

    return knowledge

def get_openai_embeddings():
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY", "null")
    print(f"OpenAI API key is {api_key}")
    return OpenAIEmbeddings(disallowed_special=(), openai_api_key=api_key)

# Generate embeddings for code snippets
def generate_embedding():
    print("Code file paths...")
    print(code_files_path)
    code_snippets = get_document_information(code_files_path)
    print(f"Generated {len(code_snippets)} embeddings.")
    embedding = get_openai_embeddings()
    documents = code_snippets
    faiss_store = FAISS.from_documents(documents, embedding=embedding)
    return faiss_store

def store_vectordb():
    faiss_code_store = generate_embedding()
    faiss_code_store.save_local("faissindex")

def load_vectordb():
    index_path = Path("faissindex").resolve()
    print("indexpath: ")
    print(index_path)
    faiss_code_store = FAISS.load_local(index_name="index", folder_path= index_path, embeddings=get_openai_embeddings(),allow_dangerous_deserialization=True)
    return faiss_code_store

if __name__ == '__main__':
    store_vectordb() # loads vectors fron FAISS index