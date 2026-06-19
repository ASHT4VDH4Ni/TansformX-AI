from openai import AsyncOpenAI
from config import GEMINI_API_KEY

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL
)