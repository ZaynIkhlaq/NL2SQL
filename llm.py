
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
if not os.environ.get("GROQ_API_KEY"):
    raise ValueError("Please set GROQ_API_KEY in your .env file")

# Initialize the LLM
llm = init_chat_model("meta-llama/llama-4-maverick-17b-128e-instruct", model_provider="groq")