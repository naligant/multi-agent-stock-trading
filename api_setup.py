import requests
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")

OPENAI_API_URL = os.getenv("OPENAI_API_URL")
if not OPENAI_API_URL:
    raise ValueError("OPENAI_API_URL is not set")