from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def summarize_to_three_sentences(text):
    print("=== Step 2: Summarizing to 3 sentences ===")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "Summarize the following text into exactly 3 Korean sentences."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content
