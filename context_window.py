import os
from dotenv import load_dotenv
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
for model in client.models.list().data:
    if model.id == 'whisper-large-v3':
     print(f'The total number of tokens that can be handled by {model.id}:', model.context_window)