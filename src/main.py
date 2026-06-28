import os
from dotenv import load_dotenv
from src.agent import create_simple_agent

def main():
    load_dotenv()
    agent = create_simple_agent()
    print("Simple AI Agent. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            break
        result = agent.invoke({"input": user_input})
        print(f"Agent: {result['output']}")

if __name__ == "__main__":
    main()
