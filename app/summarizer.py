from openai import OpenAI
import os

# get api key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_to_three_sentences(text: str) -> str:
    """
    Summarize extracted manual text into exactly 3 Korean sentences.
    Uses a FREE model (gpt-4o-mini), so no API credit is needed.
    """

    prompt = f"""
다음 제품 설명서 내용을 한국어로 정확하게 5문장으로 요약해줘.
핵심 기능, 안전사항 또는 사용방법 위주로 정리해줘.

설명서 내용:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # 무료 모델
        messages=[
            {"role": "system", "content": "너는 설명서를 명확하게 요약해주는 도우미야."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    return response.choices[0].message["content"]

