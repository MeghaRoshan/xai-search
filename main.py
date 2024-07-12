import os

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from constant import DB_FAISS_PATH, FAISS_FILE_PATH, LLM_MODEL, OLLMA_CONTANIER_URL

# Check if FAISS index file exists; if not, perform indexing
if not os.path.isfile(FAISS_FILE_PATH):
    from modules.index_data.index import index_data

    index_data()

else:
    print("Indexing already done")


# Function to load the FAISS index database
def load_knowledgeBase():
    """
    Loads the FAISS index database using specified embeddings.

    Returns:
        FAISS: Loaded FAISS index database.
    """
    embeddings = OllamaEmbeddings(
        model=LLM_MODEL,
        base_url=OLLMA_CONTANIER_URL,
        temperature=0,
    )
    db = FAISS.load_local(
        DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True
    )
    return db


# Function to load the language model (LLM)
def load_llm():
    """
    Loads the Ollama language model (LLM) for generating responses.

    Returns:
        Ollama: Loaded Ollama language model.
    """
    print("Loading LLM")
    llm = Ollama(
        model=LLM_MODEL,
        base_url=OLLMA_CONTANIER_URL,
        verbose=True,
        temperature=0,
    )
    return llm


# Function to load the prompt template for product difference
def load_prompt():
    """
    Loads the prompt template for conversational context.

    Returns:
        ChatPromptTemplate: Loaded prompt template.
    """
    prompt = """Given the list of products, explain why each product is similar or dissimilar to the query. 
        Given below is the list of products and query.
        list of products = {context}
        query = {question}
        if the query is not in the database "No products found"
         """
    prompt = ChatPromptTemplate.from_template(prompt)
    return prompt


# Function to format document contents
def format_docs(docs):
    """
    Formats document contents into a single string separated by double newline.

    Args:
        docs (list): List of documents to format.

    Returns:
        str: Formatted document contents.
    """
    return "\n\n".join(doc.page_content for doc in docs)


# Load knowledge base, LLM, and prompt template
knowledgeBase = load_knowledgeBase()
llm = load_llm()
prompt = load_prompt()

app = FastAPI()


# Default route
@app.get("/")
async def hello():
    """
    Default route to check if the API is running.

    Returns:
        dict: Message indicating the API status.
    """
    return {"message": "Welcome to the XAI-Search API!"}


# Endpoint for handling search queries
@app.post("/search/")
async def search_query(data: dict):
    """
    Endpoint to process search queries.

    Args:
        data (dict): Input data containing 'query'.

    Returns:
        dict: Response containing the generated answer.
    """
    data["query"] = data["query"].upper()
    similar_embeddings = knowledgeBase.similarity_search(query=data["query"], k=10)
    similar_embeddings = FAISS.from_documents(
        documents=similar_embeddings,
        embedding=OllamaEmbeddings(
            model=LLM_MODEL,
            base_url=OLLMA_CONTANIER_URL,
            temperature=0,
        ),
    )
    retriever = similar_embeddings.as_retriever()
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    response = rag_chain.invoke(data["query"])
    return {"response": response}
