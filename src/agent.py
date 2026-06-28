from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from src.tools import get_current_time, add_numbers

def create_simple_agent():
    """
    Create and return a simple LangChain agent that can use the defined tools.
    """
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    tools = [get_current_time, add_numbers]
    agent_executor = create_agent(
        llm=llm,
        tools=tools,
        agent_type="openai-functions",
        verbose=True,
    )
    return agent_executor
