from crewai import Agent

from tools import yt_tool

from langchain_community.llms import Ollama


from dotenv import load_dotenv
load_dotenv()

import os
model_name = os.getenv("ollama_model_name", "gemma2-9b-it")
# llm = Ollama(model=model_name)

##Create a senior blog researcher
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model=model_name)


blog_researcher=Agent(role='Blog Researcher from Youtube videos',
                      goal='get the relavant video content for the topic{topic}from yt channel',
                      verbose=True,
                      memory=True,
                      backstory=(
                          "Expert in understanding videos in AI Datascience,Machine learning and Gen Ai and llms "
                      ),
                      tools=[],
                      llm=llm,
                      allow_delegation=True
                      )







##CReating a senior blog writer agent with YT tool

blog_writer=Agent(role='Blog Writer',
                      goal='Narrate compelling tech stories about the video{topic}from yt channel',
                      verbose=True,
                      memory=True,
                      backstory=(
                          "With a flair for simplying complex topics,you craft"
                          "engaging narratives that captivate and educate,bringing new"
                          "discoveries to light in an accessible manner"),
                      llm=llm,
                      tools=[],
                      allow_delegation=True
                      )




