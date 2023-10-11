import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("training.jsonl", "rb") as file:
    result = openai.File.create(file=file, purpose='fine-tune')
print(result)
