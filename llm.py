
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("Please set  GOOGLE_API_KEY in your .env file")

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp')
