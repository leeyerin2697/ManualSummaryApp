from deepseek import DeepSeek
import os

# read api key
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# DeepSeek reset client
client = DeepSeek(api_key=DEEPSEEK_API_KEY)


def summarize_to_three_sentences(text):
    """
    Summarize text into 3 sentences using DeepSeek API.
    """
    prompt = f"""
다음 설명서를 한국어로 3줄 정도로 자연스럽게 요약해줘:

{text}
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.3,
    )

    return response.choices[0].message["content"].strip()


