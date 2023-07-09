import os
import requests
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

load_dotenv(dotenv_path=env_path)

API_TOKEN = os.getenv('HFACE_API_TOKEN')
API_URL = "https://api-inference.huggingface.co/models/SG161222/Realistic_Vision_V1.4"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def get_ai_image(payload: str):
	response = requests.post(API_URL, headers=headers, json={"inputs": payload})
	return response.content
