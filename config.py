import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:1234/v1")

def get_llm():
    """
    Returns a LangChain ChatOpenAI instance configured to use LM Studio.
    """
    return ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.2,
        base_url=BASE_URL,
        api_key="lmstudio",  # LM Studio accepts any non-empty key
    )
