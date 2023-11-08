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

def pythonCodeGenerator(deadlock_amount,resource_contention_amount,non_contentious_resources_amount):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
    )
    system_template = """You are a Python code generator. Your task is to generate a Python code with five threads that includes {deadlock_amount} deadlock, {resource_contention_amount} thread resource contention, and {non_contentious_resources_amount} non-contentious resources. Notice that\
    you need to hide these deadlocks and thread resource contentions, which means that those are hard to find. For example, you can put the code in a certain situation, and rename those deadlocks and resource contention without annotations. And you can increase the depth of the deadlocks"""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate a Python code with five threads that includes {deadlock_amount} deadlock, {resource_contention_amount} thread resource contention, and {non_contentious_resources_amount} non-contentious resources.Notice that\
    you need to hide these deadlocks and thread resource contentions, which means that those are hard to find. For example, you can put the code in a certain situation, and rename those deadlocks and resource contention without annotations. And you can increase the depth of the deadlocks"""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(deadlock_amount=deadlock_amount, resource_contention_amount=resource_contention_amount, non_contentious_resources_amount=non_contentious_resources_amount)
    return result # returns string
