from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
Classify the sentiment of the user's message as positive, negative, or neutral.
Return only the label.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "The package arrived on time and works perfectly."},
    ],
)

print("Response:", response.choices[0].message.content)
