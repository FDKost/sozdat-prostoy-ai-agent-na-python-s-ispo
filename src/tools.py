from langchain.tools import tool

@tool(name="Get Current Time", description="Returns the current UTC time.")
def get_current_time() -> str:
    """Return the current UTC time as an ISO formatted string."""
    from datetime import datetime
    return datetime.utcnow().isoformat() + "Z"

@tool(name="Add Numbers", description="Adds two numbers and returns the result.")
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b
