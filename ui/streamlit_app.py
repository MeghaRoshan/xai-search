import requests
import streamlit as sl

# Set up the Streamlit header
sl.header("XAI-Search")

# Create a text input box for user queries
query = sl.text_input("Enter your query")

# Check if the user has entered a query
if query:
    # Send a POST request to the serving API with the user's query as JSON
    response = requests.post("http://serving:8080/search/", json={"query": query})

    # Extract the response JSON from the server's response
    result = response.json()["response"]

    # Display the result on the Streamlit interface
    sl.write(result)
