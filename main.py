from agent import create_agent

def main():
    agent = create_agent()
    query = "What is the result of 12 * 7?"
    response = agent.run(query)
    print("Agent response:")
    print(response)

if __name__ == "__main__":
    main()
