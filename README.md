# Simple LangChain 1.x AI Agent

This project demonstrates a minimal AI agent built with LangChain 1.x and the `langchain-openai` 1.x SDK.  
The agent can answer simple arithmetic questions and report the current UTC time using two custom tools.

## Prerequisites

- Python 3.10 or newer
- An OpenAI API key

## Setup

```bash
# Clone the repository
git clone https://github.com/your-username/simple-langchain-agent.git
cd simple-langchain-agent

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY=sk-...
```

## Running the Agent

```bash
python src/main.py
```

You can then type queries such as:

```
What is 2 plus 3?
What is the current time?
```

Type `exit` or `quit` to stop the program.

## Testing

Run the tests with:

```bash
pytest
```

The tests will skip the agent tests if `OPENAI_API_KEY` is not set.

## Project Structure

```
├── src
│   ├── __init__.py
│   ├── tools.py      # Custom tools
│   ├── agent.py      # Agent creation logic
│   └── main.py       # CLI entry point
├── tests
│   ├── __init__.py
│   ├── test_tools.py
│   └── test_agent.py
├── requirements.txt
└── README.md
```

## License

MIT License
