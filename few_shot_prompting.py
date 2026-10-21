#the main purpose of few_shot_prompting is to improve the accuracy of the model by providing with few related examples of the problem.
import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
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
"""

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

#FEW-SHOT PROMPTING
for ticket, category in tickets:
    prompt = [{
        'role':'system',
        'content':structured
    },
    examples
    ,{
        'role':'user',
        'content':ticket
    }]
    print('expected:',category, 'actual:',ask(prompt))