import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

def codeAnalyzer(code):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
    )
    system_template = """You are a code analyzer. Your task is to output only the number of potential resources contention as a single integer with no additional text or explanation. The given code is {code}."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please output only the number of potential resources contention as a single integer with no additional text or explanation. The given code is {code}."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(code=code)
    print(result)
    return int(result) # returns string
#
# st.title("Code Analyzer")
#
# code = st.text_area("Enter Python code")
#
# if st.button("Analyze Code"):
#     if code:
#         count_code = codeAnalyzer(code)
#         st.markdown(count_code)
#     else:
#         st.markdown("Please enter Python code to analyze")