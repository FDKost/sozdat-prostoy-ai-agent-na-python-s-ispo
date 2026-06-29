import unittest
from unittest.mock import patch, MagicMock
from agent import create_agent

class TestAgent(unittest.TestCase):
    @patch("config.get_llm")
    def test_agent_response(self, mock_get_llm):
        # Mock the LLM to return a fixed response
        mock_llm = MagicMock()
        mock_llm.invoke.return_value = MagicMock(content="84")
        mock_get_llm.return_value = mock_llm

        agent = create_agent()
        response = agent.run("What is 12 times 7?")
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

if __name__ == "__main__":
    unittest.main()
