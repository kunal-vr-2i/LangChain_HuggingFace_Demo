import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="bigscience/bloomz-560m",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100, "temperature": 0.01},
)

prompt = PromptTemplate.from_template("Q: {text}\nA:")

# Chain using the pipe operator
chain = prompt | llm

user_question = input("Enter your question: ")
result = chain.invoke({"text": user_question})
print(result)
