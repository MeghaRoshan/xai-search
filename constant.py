import os

# Get the current working directory
CWD = os.getcwd()

# Define paths and constants using the current working directory

# Path to the directory containing FAISS vector store
DB_FAISS_PATH = (
    CWD + os.path.sep + "data" + os.path.sep + "vectorstore" + os.path.sep + "db_faiss"
)

# Path to the raw data CSV file
RAW_DATA_CSV_PATH = (
    CWD + os.path.sep + "data" + os.path.sep + "raw_data" + os.path.sep + "data.csv"
)

# Name of the LLM model
LLM_MODEL = "llama3"

# Path to the FAISS index file
FAISS_FILE_PATH = (
    CWD
    + os.path.sep
    + "data"
    + os.path.sep
    + "vectorstore"
    + os.path.sep
    + "db_faiss"
    + os.path.sep
    + "index.faiss"
)

# URL for the Ollama container
OLLMA_CONTANIER_URL = "http://ollama-container:11434"
