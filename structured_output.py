import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
from typing import Literal
from pydantic import BaseModel, Field, ValidationError

#class for representing the structure of an output
class structured_output(BaseModel):
    category: Literal['billing', 'shipping', 'other']
    priority:int = Field(ge = 1, le = 5)  #here the priority can be from 1 to 5, 


#check function
def check(answer):
    try:
        return structured_output.model_validate_json(answer)  #checking the structure of an output
    except ValidationError:
        return None
    

print(check('{"category":"other","priority":5}'))  #passing the correct input 
print(check('{"category":"other","priority":8}'))  #passing the wrong output

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def ask(messages,**settings):
    response = client.chat.completions.create(
        model ="openai/gpt-oss-120b",
        messages = messages,
        **settings
    )
    return response.choices[0].message.content

structured = """You sort customer support tickets for an online shop.

Categories:
- billing: payments, charges, refunds
- shipping: parcels, delivery, damaged boxes
- other: anything else

Reply with one line of JSON and nothing else, like this:
{"category": "shipping"}
priority is 1 (can wait) to 5 (urgent)
"""

vague = """You sort the online shop's tickets."""

tickets = [
    ("I was charged twice for one order", "billing"),
    ("My parcel has not arrived", "shipping"),
    ("Can I get a refund for the blue mug?", "billing"),
    ("How do I change my password?", "other"),
    ("The parcel arrived but the box was crushed", "shipping"),
    ("The courier asked me to pay a delivery fee at the door", "billing"),
    ("I want to stop my subscription", "billing"),
]

#LOGIC OF FEW-SHOT PROMPTING
examples = {
    'role':'user','content':'you took money from my account without permission',
    'role':'assistant','content':'{"category": "billing","priority": "high"}',
    'role':'user','content':'Where is my delivery? It is a week late',
    'role':'assistant','content':'{"category": "shipping","priority": "high"}',
    'role':'user','content':'Can I change the email on my account?',
    'role':'assistant','content':'{"category": "other","priority": "high"}',
    'role':'user','content':'Can I make payment?',
    'role':'assistant','content':'{"category": "billing","priority": "high"}',
}

#checking the output using the structured prompt
for ticket,category in tickets:
    prompt = [{
        'role':'system','content':structured},
        examples,  #few-shot-prompting
        {'role':'user','content':ticket
    }] 
    print(check(ask(prompt)))  

print('After this, checking with vague prompt')
#checking the output using vague prompt
for ticket,category in tickets:
    prompt = [{
        'role':'system','content':vague},
        examples,  #few-shot-prompting
        {'role':'user','content':ticket
    }] 
    print(check(ask(prompt)))
