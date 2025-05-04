import os
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def nemotron_generate(prompt):
    completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-ultra-253b-v1:free",
        messages=[
            {
                "role": "user",
                "user": "user",  # Explicitly declare the LLM role as required
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content