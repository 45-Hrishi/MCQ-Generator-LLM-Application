import os
import json
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from langchain_mistralai import ChatMistralAI
load_dotenv()

# Model Initialization
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
llm = ChatMistralAI(model="mistral-large-latest",temperature=0.3,api_key = MISTRAL_API_KEY)

# PromptTemplate Creation for quiz generation
input_variables = ["text","number","subject","tone","response_json"]
output_key = ["quiz"]
with open("prompts.json",'r') as file:
    content = json.load(file)
    TEMPLATE = content["quiz_generator_prompt"]
    
quiz_generation_prompt = PromptTemplate(input_variables=input_variables,output_key=output_key,template = TEMPLATE)

# Chain creation for quiz generation
quiz_generation_chain = LLMChain(llm=llm,prompt=quiz_generation_prompt,output_key="quiz")

# PromptTemplate Creation for quiz evaluation
input_variables = ["quiz","subject"]
output_variables=["review"]
with open("prompts.json",'r') as file:
    content = json.load(file)
    TEMPLATE = content["quiz_evaluator_prompt"]
    
quiz_evaluator_prompt = PromptTemplate(input_variables=input_variables,output_key=output_key,template = TEMPLATE)

# Chain creation for quiz evaluator 
quiz_evaluator_chain = LLMChain(llm=llm,prompt=quiz_evaluator_prompt,output_key="review")

# Sequential Chain creation
seq_quiz_chain = SequentialChain(chains=[quiz_generation_chain,quiz_evaluator_chain],
                                 input_variables=["text","number","subject","tone","response_json"],
                                 output_variables=["quiz","review"])