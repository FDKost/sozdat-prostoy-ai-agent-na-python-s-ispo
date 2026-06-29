from langchain.agents import initialize_agent, AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.agents import Tool
from config import get_llm

def create_agent():
    """
    Creates a simple LangChain agent that can execute Python code.
    """
    llm = get_llm()
    python_tool = PythonREPLTool()
    tools = [python_tool]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
    )
    return agent
