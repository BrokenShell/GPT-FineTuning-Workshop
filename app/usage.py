import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

system_prompt = "..."
user_prompt = "..."

completion, *_ = openai.ChatCompletion.create(
    model="...",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
).choices
print(completion.message.content)
