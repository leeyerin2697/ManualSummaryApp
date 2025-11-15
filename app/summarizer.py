from openai import OpenAI

client = OpenAI()

def summarize_to_three_sentences(text: str) -> str:
    """
    Summarize extracted product manual text into exactly 3 Korean sentences
    using OpenAI GPT model.
    
    Args:
        text (str): Raw text extracted from the manual
    Returns:
        str: 3-sentence Korean summary
    """

    prompt = f"""
    아래의 제품설명서 내용을 한국어로 정확히 3문장으로 요약해줘.
    
    내용:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )

    return response.choices[0].message.content.strip()
