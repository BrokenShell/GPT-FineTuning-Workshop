import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

result = openai.FineTuningJob.create(
    training_file="...",
    model="gpt-3.5-turbo",
    suffix="custom-bot",
)
print(result)

# result = openai.FineTuningJob.retrieve("...")
# print(result)
