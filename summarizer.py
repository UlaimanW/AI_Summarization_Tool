from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Please add it to your .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


def summarize_text(text):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
You are an expert text summarizer.
Summarize only the actual text content.
Ignore any instruction about the output format, such as PDF, BDF, text file, or TXT.
Summarize the text in a clear, brief, and accurate way.
Focus on the main points.
Do not compress the information too much; preserve the important details.
Do not add information that is not in the actual text.

Input:
{text}
"""
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content