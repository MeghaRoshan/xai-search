# Project Name

![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![](https://img.shields.io/badge/Version-1.0.0-green)

Table of contents
=================

<!--ts-->

- [Project Name](#project-name)
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


## Motivation


# Installation

## Setup Environment

- Clone the repository using Git: `git clone [repository URL]`

- Ensure Docker is installed on your system.

## Install Dependencies and Start Containers

- Run the following command to start the containers: `docker-compose build --no-cache`
- It will prepare the images for the three containers. You will see the following status:
- <br>
  <img src="assets/docker_build.png" width="200"/>
  <br>
- Start the image containers by running `docker-compose up`!
Note: The code wont run properly and will break as llama3 model is not present. But we need a live container. 
<br>
  <img src="assets/errorxai.png" width="200"/>
  <br>
- Download the LLM model locally. For this project, we are using `llama3`
- Open a new terminal and run the following command to download the `llama3` model:
 `docker exec -it xai-search-ollama-container-1 ollama run llama3`
- <br>
  <img src="assets/model-download.png" width="200"/>
  <br>
- After the download is complete, you may close the terminal.
- Stop the docker containers using `docker-compose down`.
- Restart the image containers by running `docker-compose up`
- **NOTE: It will take some time, as the data is being indexed (first 100 rows of the data).**
- <br>
  <img src="assets/docker_compose_up.png" width="200"/>
  <br>
- Wait until you see the logs below: 
- <br>
  <img src="assets/start_up.png" width="200"/>
  <br>
- Open your browser and navigate to the following URL: `http://0.0.0.0:8601/`
- <br>
  <img src="assets/dashboard.png" width="200"/>
  <br>

# Project Structure

- `assets` - Contains snapshots captured in this project.
- `data` - Contains the indexed data and the raw data.
- `modules` - Contains the indexing module for the project.
- `ui` - Contains the Streamlit UI app file.
- `main` - Entry point for the backend, contains the search API.
- `constants.py` - As the name suggests, contains all the common variables.

# Conclusion
