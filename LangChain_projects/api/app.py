from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os 
from langchain_community.llms import Ollama
from langchain_core.runnables import Runnable

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


#Creating Fast API App
app = FastAPI(
    title="LangChain Server ",
    version="1.0",
    description="simple api server"
)

#adding routes
add_routes(
    app,
    ChatOpenAI,
    path="/openai"
)

model=ChatOpenAI()
#Ollama model
llm=Ollama(model="llama3")


## Prompt Template 

prompt1= ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words")
prompt2= ChatPromptTemplate.from_template("Write an poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__ =="__main__":
    uvicorn.run(app,host="localhost",port= 8000)