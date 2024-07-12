# XAI Search 

![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![](https://img.shields.io/badge/Version-1.0.0-green)

Table of contents
=================

<!--ts-->

- [XAI Search](#project-name)
- [Table of contents](#table-of-contents)
- [Introduction](#introduction)
  - [Motivation](#motivation)
- [Installation](#installation)
  - [Setup Environment](#setup-environment)
  - [Install Dependencies and Start Containers](#install-dependencies-and-start-containers)
- [Project Structure](#project-structure)
- [Conclusion](#conclusion)

<!--te-->

# Introduction
Welcome to my project! This AI-driven solution enhances recommendation systems for e-commerce platforms using Python and LangChain.

By combining vector databases, semantic search, and the advanced language model Llama3, this project delivers explanability regarding product recommendations.

## Motivation
- Users often struggle to find specific products due to the vast selection on e-commerce platforms, leading to a poor shopping experience and reduced satisfaction.


# Installation

## Setup Environment

- Clone the repository using Git: `git clone https://github.com/MeghaRoshan/xai-search.git`

- Ensure Docker is installed on your system.

## Install Dependencies and Start Containers

- Run the following command to start the containers: `docker-compose build --no-cache`
- It will prepare the images for the three containers. You will see the following status:
- <br>
  <img src="assets/docker_build.png" width="700"/>
  <br>
- Start the image containers by running `docker-compose up`!
Note: The code wont run properly and will break as llama3 model is not present. But we need a live container. 
<br>
  <img src="assets/errorxai.png" width="700"/>
  <br>
- Download the LLM model locally. For this project, we are using `llama3`
- Open a new terminal and run the following command to download the `llama3` model:
 `docker exec -it xai-search-ollama-container-1 ollama run llama3`
- <br>
  <img src="assets/model-download.png" width="700"/>
  <br>
- After the download is complete, you may close the terminal.
- Stop the docker containers using `docker-compose down`.
- Restart the image containers by running `docker-compose up`
- **NOTE: It will take some time, as the data is being indexed (first 100 rows of the data).**
- <br>
  <img src="assets/docker_compose_up.png" width="900"/>
  <br>
- Wait until you see the logs below: 
- <br>
  <img src="assets/start_up.png" width="900"/>
  <br>
- Open your browser and navigate to the following URL: `http://0.0.0.0:8601/`
- <br>
  <img src="assets/dashboard.png" width="500"/>
  <br>

# Project Structure

- `assets` - Contains snapshots captured in this project.
- `data` - Contains the indexed data and the raw data.
- `modules` - Contains the indexing module for the project.
- `ui` - Contains the Streamlit UI app file.
- `main` - Entry point for the backend, contains the search API.
- `constants.py` - As the name suggests, contains all the common variables.

# Conclusion
In conclusion, the project represents a significant advancement in GenAI Solutions by integrating LangChain-based technology with a vector database, offering a seamless user experience. 

Through its ability to explain the relevance of specific products in search results, the project enhances transparency and trust, crucial in user interactions. This transparency not only improves user satisfaction but also builds confidence in the system's recommendations.

Overall, this project exemplifies how innovative AI solutions can transform user interactions by combining efficiency, transparency, and accuracy into a cohesive and impactful user experience.