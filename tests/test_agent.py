import os
import sys
import pytest
from agent import create_agent, get_response

@pytest.fixture(scope="module")
def agent_chain():
    # Ensure the environment variable is set for tests
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "test_key")
    return create_agent()

def test_agent_returns_non_empty(agent_chain):
    question = "What is the capital of France?"
    response = get_response(agent_chain, question)
    assert isinstance(response, str)
    assert response.strip() != ""

def test_agent_handles_empty_question(agent_chain):
    question = ""
    response = get_response(agent_chain, question)
    assert isinstance(response, str)
    assert response.strip() != ""
