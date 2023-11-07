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

def codeGenerator(deadlock_amount,resource_contention_amount,non_contentious_resources_amount):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are a code generator. Your task is to add {deadlock_amount} instances of deadlock, {resource_contention_amount} instances of 2-thread resource contention, and {non_contentious_resources_amount} instances of non-contentious resources to a multiple-threading Python code with five threads."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate a code that adds {deadlock_amount} instances of deadlock, {resource_contention_amount} instances of 2-thread resource contention, and {non_contentious_resources_amount} instances of non-contentious resources to a multiple-threading Python code with five threads."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(deadlock_amount=deadlock_amount, resource_contention_amount=resource_contention_amount, non_contentious_resources_amount=non_contentious_resources_amount)
    return result # returns string
#
# st.title("Code Generator")
#
# #Get the requested amount of deadlock from the user
# deadlock_amount = st.text_input("Enter the requested amount of deadlock")
# #Get the requested amount of 2-thread resource contention from the user
# resource_contention_amount = st.text_input("Enter the requested amount of 2-thread resource contention")
# #Get the requested amount of non-contentious resources from the user
# non_contentious_resources_amount = st.text_input("Enter the requested amount of non-contentious resources")
#
# #Create a button to trigger the functionality of the app
# if st.button("Generate Code"):
#     if deadlock_amount and resource_contention_amount and non_contentious_resources_amount:
#         code = codeGenerator(deadlock_amount,resource_contention_amount,non_contentious_resources_amount)
#     else:
#         code = ""
#     #Display the generated code to the user
#     st.markdown(code)