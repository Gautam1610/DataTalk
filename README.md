# DataTalk
This is a Streamlit app that allows you to upload a CSV file and ask questions to it using a large language model (LLM) from OpenAI. The app uses LangChain, a framework for building LLM applications, to create an agent that can interact with the CSV file and generate natural language responses. The app also uses dotenv to load environment variables from a .env file.

# Installation
To run this app, you need to install the following dependencies:

streamlit
langchain
langchain-experimental
python-dotenv
You can install them using pip:

pip install streamlit langchain langchain-experimental python-dotenv

You also need to create a .env file in the same directory as your app and add your OpenAI API key:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Usage
Usage
To run the app, use the following command:

streamlit run app.py

Then, you can upload your CSV file and type your questions in the text input. The app will use the OpenAI LLM and the LangChain agent to generate a response for you. You can also see the verbose output of the agent in the terminal.

# Working
![Screenshot (17)](https://github.com/Gautam1610/DataTalk/assets/98054056/7a1a83f9-5cf1-4d3c-9534-2eb18852b57e)
![Screenshot (19)](https://github.com/Gautam1610/DataTalk/assets/98054056/f7e84453-71d8-4aff-81cb-d50a53fe0ac4)

![Screenshot (18)](https://github.com/Gautam1610/DataTalk/assets/98054056/94ce5a7c-6a64-413f-84f3-72ac6baa4deb)


![Screenshot (18)](https://github.com/Gautam1610/DataTalk/assets/98054056/2604dd6c-8a90-4386-b968-01113474a2a2)
![Screenshot (19)](https://github.com/Gautam1610/DataTalk/assets/98054056/17a33302-8d13-43b1-aaca-7d2dfa6525b4)
