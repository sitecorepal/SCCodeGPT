from Learn import load_vectordb 
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#query = "write typscript code for Sitecore NextJS promo component with default and wrapper variant. The wrapper variant should be wrapped with a div and a class called container-wrapper to that div."

def load_vector():
    faiss_code_store = load_vectordb()
    retriever = faiss_code_store.as_retriever()
    return RunnableParallel(context=retriever, question=RunnablePassthrough())

def load_llm():
    # Commented out IPython magic to ensure Python compatibility.
    return AzureChatOpenAI(
        azure_deployment="gpt-4o-2",  # or your deployment
        api_version="2023-03-15-preview",  # or your api version
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )

def load_prompt():
    template = """You are a Sitecore XMCloud and NextJS code developer that writes code. Keep the responses clean and complete without any explanation. Embed explanation as comments in code wherever required. If you do not know answer, then say you don't know. But do not try and make up answers. Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    return ChatPromptTemplate.from_template(template)

def load_parser():
    return StrOutputParser()

def create_chain():
    vector = load_vector()
    llm = load_llm()
    prompt = load_prompt()
    parser = load_parser()
    return (
        vector
        | prompt
        | llm
        | parser
    )

def get_chat_response(query):
    chain = create_chain()
    return chain.invoke(query)