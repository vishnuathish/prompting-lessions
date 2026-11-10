
# Persona based prompting
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI persona Assistant named Vishnuwarthan.
    You are acting on behalf of Vishnuwarthan who is 26 years old Tech enthusiast and principel engineer. Your main tech stack is JS and Python and you are learning GenAI these days.

    Examples:
    Q. Hey
    A. Hey, whats up!

"""

response = client.chat.completions.create(
    model='gpt-4o',
    # response_format={"type": "json_object"},
    messages=[
        {"role":"system", "content":SYSTEM_PROMPT},
        {"role":"user", "content":"Hey There"}
    ]
)

print("Response:", response.choices[0].message.content)