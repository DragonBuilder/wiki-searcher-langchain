import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
# from langchain.agents import AgentType
from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0)

## load the wiki search tool
tools = load_tools(["wikipedia"], llm=llm)

## create the agent.
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

## the prompt template that will be used by the agent.
print(agent.agent.llm_chain.prompt.template)

## to run an agent, use run()
# agent.run("What are LLM agents?")
# agent.run("What are Langchain agents?")
# How are LangChain agents different from LLM agents?

result = agent.run("Research papers on LLM agents.")

## print the result
print(result)