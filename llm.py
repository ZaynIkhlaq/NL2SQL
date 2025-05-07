import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Try to load from .env file (local development)
load_dotenv()

# Check for API key in environment
if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("Please set GOOGLE_API_KEY in your .env file for local development or in Streamlit Cloud secrets")

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-04-17')
