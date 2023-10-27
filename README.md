### Reddit salary analysis

## Introduction

![Webapp_screen](https://github.com/yahiaakkazi/de-reddit-salary-analysis/assets/83475215/d91e033a-15b1-4421-b3e9-79d69bdfcdd7)

Webapp : https://de-reddit-salary-analysis.streamlit.app/

This repository contains a collection of salary information and relevant data for the role of data engineering worldwide. The dataset is curated based on searches and submissions from the Reddit community, specifically the "Salary on the Data Engineering" subreddit.
To create this dataset, I leveraged the power of OpenAI's GPT-3.5 language model using its API, and praw, the reddit api, to interact and scrape data from Reddit.

The process begins with the Python modules provided by OpenAI, allowing us to communicate with the OpenAI API and present specific prompts to the GPT-3.5 model. We then use gpt to format the raw submissions into a structured JSON format, making it easier to extract and organize the relevant salary and data engineering information, transforming data from purely unstructured data into semi-structured data.

The goal is ot, once the data is formatted, I store it in a database for further analysis and exploration. Provifing a web hosted app showcasing deep diving analysis regarding the data. This repository serves as a comprehensive resource for anyone interested in studying or analyzing data engineering market as a whole. The dataset can be utilized for various purposes.




The code is pretty straightforward, all one needs to have, is to setup an API key from openai and another one from reddit so that one can obtain a similar dataset. The project is still new and still has certain limitations. For instance, the LLM still doesn't abide strictly to the rules...
The aim is to make the formatting work, and then to proceed storing data into a database, and finally presenting its insights into interactive dashboards.



