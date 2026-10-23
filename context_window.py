import os
from dotenv import load_dotenv
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
for model in client.models.list().data:
    if model.id == 'whisper-large-v3':
     print(f'The total number of tokens that can be handled by {model.id}:', model.context_window)

system= {'role':'system','content':'You are FinCoach, a personal finance assistant. Reply in one short sentence.'}     
turns = [
    "My monthly take-home is 5000$.",
    "My expenses are 2,000$ a month.",
    "What is the most important thing I should do this month?",
]

history = [system]  #here history acts as the chat history with LLM
for turn in turns:
   history.append({'role':'user','content':turn})
   response = client.chat.completions.create(model='openai/gpt-oss-120b',messages=history)  
   history.append({'role':'assistant','content':response.choices[0].message.content})  #storing the response of LLM in chat history 
   print(response)
   print(len(history))
