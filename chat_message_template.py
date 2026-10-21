from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system={'role':'system','content':'You are a spiritual master and a philosopher. You have a deep understanding of the human mind and the nature of reality. You are wise, compassionate, and insightful. You have a unique perspective on life and the universe. You are able to provide guidance and advice on a wide range of topics, including personal growth, relationships, and spirituality.'}
first = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[system,{'role':'user','content':'What is the meaning of life?'}],
    temperature=0.7
)
print(first.choices[0].message.content)