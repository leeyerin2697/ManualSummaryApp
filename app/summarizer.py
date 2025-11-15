import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

# Initialize DeepSeek/OpenAI-compatible client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

def summarize_to_three_sentences(text):
    """
    Summarize text into exactly three sentences in Korean using system + user messages.
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a summarization assistant. "
                    "Summarize the given content into exactly 3 Korean sentences. "
                    "Do not add explanations—output only the summary."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.3,
        max_tokens=200
    )

    return response.choices[0].message.content


