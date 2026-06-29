import os
import sys
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def load_api_key() -> str:
    """
    Load the OpenAI API key from the environment.
    Raises an exception if the key is not found.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found in environment. "
            "Please set it in a .env file or export it."
        )
    return api_key

def create_agent() -> LLMChain:
    """
    Create a simple LangChain LLMChain that uses OpenAI's GPT-4.
    """
    api_key = load_api_key()
    llm = ChatOpenAI(
        model_name="gpt-4o-mini",
        temperature=0.7,
        openai_api_key=api_key,
    )
    prompt = PromptTemplate(
        input_variables=["question"],
        template="You are a helpful assistant. Answer the following question:\n\n{question}",
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def get_response(chain: LLMChain, question: str) -> str:
    """
    Get a response from the agent for a given question.
    """
    return chain.run({"question": question})

def main():
    """
    Simple REPL that reads user input and prints the agent's response.
    """
    try:
        chain = create_agent()
    except Exception as e:
        print(f"Error initializing agent: {e}")
        sys.exit(1)

    print("Simple LangChain AI Agent. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if user_input.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input.strip():
            print("Please enter a question.")
            continue

        try:
            response = get_response(chain, user_input)
            print(f"\nAgent: {response}")
        except Exception as e:
            print(f"Error processing request: {e}")

if __name__ == "__main__":
    main()
