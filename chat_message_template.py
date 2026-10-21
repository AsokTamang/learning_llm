from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system={'role':'system','content':'You are a financial advisor'}
first = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[system,{'role':'user','content':'What is the meaning of life?'}],
    temperature=0.7
)
print(first.choices[0].message.content)

second = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[system,{'role':'user','content':'How to live a fulfilling life?'}],
    temperature=0.7
)
print(second.choices[0].message.content)