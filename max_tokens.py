#max tokens and finish reason
import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 
prompt = [{"role": "user", "content": "Write a one-sentence apology to a customer whose parcel is late."}]
response = client.chat.completions.create(
        model="openai/gpt-oss-120b", messages=prompt, max_completion_tokens=300
    )
choice = response.choices[0]
content = choice.message.content
print(f'The model generated the following content: {content}')
print(f'The finish reason for the completion is: {choice.finish_reason}')