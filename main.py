import streamlit as st
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from dotenv import load_dotenv
def main():
    load_dotenv()
    st.set_page_config(page_title="Talk with your Data")
    st.header("Ask questions to your CSV")
    user_csv=st.file_uploader("Upload your csv")
    if user_csv is not None:
        questions=st.text_input("Ask your questions")
        llm=OpenAI(temperature=0)
        agent=create_csv_agent(llm,user_csv,verbose=True)
        if questions is not None:
            if questions is not None and questions!="":
                st.write(f"Your query is : {questions}")
                response=agent.run(questions)
                st.write(response)


if __name__=="__main__":
    main()
