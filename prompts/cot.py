from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
Solve the arithmetic word problem carefully. Return a concise explanation
of the calculation followed by the final answer.
"""

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": (
                "A notebook costs $4. If Maya buys 3 notebooks and pays with "
                "$20, how much change should she receive?"
            ),
        },
    ],
)

print("Response:", response.choices[0].message.content)
