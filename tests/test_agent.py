import os
import pytest
from src.agent import create_simple_agent

@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="OPENAI_API_KEY not set")
def test_agent_addition():
    agent = create_simple_agent()
    result = agent.invoke({"input": "What is 2 plus 3?"})
    assert "5" in result["output"]

@pytest.mark.skipif(not os.getenv("OPENAI_API_KEY"), reason="OPENAI_API_KEY not set")
def test_agent_time():
    agent = create_simple_agent()
    result = agent.invoke({"input": "What is the current time?"})
    assert "Z" in result["output"]
