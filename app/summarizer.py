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

def summarize_sentences_clear(text):
    """
    Summarize text into Korean using system + user messages.
    """

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",               #ask to deepseek
                "content": (
                    "You are a summarization assistant. "
                    "Provide a Korean summary of the given content. "
                    "Focus on key points, essential information, and important cautions. "
                    "Keep the summary brief—limit it to 5 short sentences. "
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


