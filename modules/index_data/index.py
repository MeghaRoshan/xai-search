# Import necessary modules from langchain_community
from langchain_community.document_loaders import CSVLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Import constants for file paths and model
from constant import DB_FAISS_PATH, LLM_MODEL, OLLMA_CONTANIER_URL, RAW_DATA_CSV_PATH


def index_data():
    """
    Indexes data from a CSV file using FAISS vector storage.

    Reads data from RAW_DATA_CSV_PATH, processes it using OllamaEmbeddings
    for vectorization, and stores the resulting FAISS vector store
    locally at DB_FAISS_PATH.

    Note:
    - Assumes RAW_DATA_CSV_PATH contains a CSV file with a 'Description' column.
    - Uses LLM_MODEL for generating embeddings with OllamaEmbeddings.
    """
    # Initialize the CSVLoader with the specified path, delimiter, source column, and encoding
    loader = CSVLoader(
        RAW_DATA_CSV_PATH,
        csv_args={"delimiter": ","},
        source_column="Description",
        encoding="unicode_escape",
    )
    # Load the documents from the CSV file and limit to the first 100 entries
    docs = loader.load()[:100]
    print("Preparing data for indexing")

    # Create a FAISS vector store from the loaded documents using the specified embeddings model
    vectorstore = FAISS.from_documents(
        documents=docs,
        embedding=OllamaEmbeddings(
            model=LLM_MODEL,
            base_url=OLLMA_CONTANIER_URL,
            temperature=0,
        ),
    )
    # Save the FAISS vector store locally to the specified path
    vectorstore.save_local(DB_FAISS_PATH)
    print("Completed indexing")
