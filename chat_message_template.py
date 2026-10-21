from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system={'role':'system','content':'You are a career advisor. You will provide guidance and advice to users seeking career-related information and support.'}
first = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[system,{'role':'user','content':'How to choose a better career?'}],
    temperature=0.7
)
print(first.choices[0].message.content)
#here history acts as the buffer for our conversation with the model
history = [
    system,
    {'role':'user','content':'How to choose a better career?'},
    {'role':'assistant','content':first.choices[0].message.content},
    {'role':'user','content':'What are the best career options for a person with a background in computer science?'}
]   
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=history
)
print(response.choices[0].message.content)

import tiktoken
encoding = tiktoken.get_encoding('o200k_harmony')
text = 'What is enlightenment?'
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{'role':'user','content':text}],
    temperature=0.7
)
print(len(encoding.encode(text)),'token in text')
print('Total number of tokens used in the conversation:',response.usage.prompt_tokens) 