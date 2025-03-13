from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

def _get_client():
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    if not gemini_api_key:
        print("GEMINI_API_KEY not found in environment variables.")
        return

    client = genai.Client(api_key=gemini_api_key)
    return client

def _get_gemini_model():
    gemini_model = os.getenv("GEMINI_MODEL")
    if not gemini_model:
        gemini_model = "gemini-2.0-flash"  # Default model if not set
    
    return gemini_model

def generate_content_from_gemini(prompt: str):
    client = _get_client()
    if not client:
        return
    
    gemini_model = _get_gemini_model()
    try:
        response = client.models.generate_content(
            model=gemini_model,
            contents=prompt,
        )
        return response.text

    except Exception as e:
        print(f"An error occurred: {e}")