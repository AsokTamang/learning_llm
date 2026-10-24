import os
from dotenv import load_dotenv
from groq import Groq
import tiktoken

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
for model in client.models.list().data:
    if model.id == 'whisper-large-v3':
     print(f'The total number of tokens that can be handled by {model.id}:', model.context_window)

system= {'role':'system','content':'You are FinCoach, a personal finance assistant. Reply in one short sentence.'}     
turns = [
    "My monthly take-home is $5000.",
    "My expenses are $2,000 a month.",
    "What is the most important thing I should do this month?",
]

history = [system]  #here history acts as the chat history with LLM
for turn in turns:
   history.append({'role':'user','content':turn})
   response = client.chat.completions.create(model='openai/gpt-oss-120b',messages=history) #passing the history of message to LLM
   history.append({'role':'assistant','content':response.choices[0].message.content})  #storing the response of LLM in chat history 
   print(response)
   print(len(history))


#Function to count the tokens in message
encoding = tiktoken.get_encoding('o200k_harmony')
def count_tokens(messages):
   return sum(len(encoding.encode(message['content'] for message in messages)))
   
#Function to trim the old used tokens inorder to avoid exceeding the context window
def trim(messages, budget):
   system,rest = messages[:1] , messages[1:]   #as the very first pair is the system message and after this is the rest of the message
   while rest and count_tokens(system+rest)>budget:
      rest = rest[2:]  #removing the old pair of messages
   return rest   
      


