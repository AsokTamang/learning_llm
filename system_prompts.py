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

tickets = [
    ("I was charged twice for one order", "billing"),
    ("My parcel has not arrived", "shipping"),
    ("Can I get a refund for the blue mug?", "billing"),
    ("How do I change my password?", "other"),
    ("The parcel arrived but the box was crushed", "shipping"),
    ("The courier asked me to pay a delivery fee at the door", "billing"),
    ("I want to cancel my order before it ships", "other"),
]

#EXPERIMENTING WITH VAGUE PROMPT
vague = "Sort this support ticket into billing, shipping or other and give it aaa priority."
for ticket, category in tickets:
    prompt = [{
        'role':'system',
        'content':vague
    },{
        'role':'user',
        'content':ticket  #here we are passing the info of tickets as the user message
    }]
    print('expected:',category, 'actual:',ask(prompt))


#EXPERIMENTING WITH STRUCTURED PROMPT
structured = """You sort customer support tickets for an online shop.

Categories:
- billing: payments, charges, refunds
- shipping: parcels, delivery, damaged boxes
- other: anything else

Reply with one line of JSON and nothing else, like this:
{"category": "shipping"}
"""

for ticket, category in tickets:
    prompt = [{
        'role':'system',
        'content':structured
    },{
        'role':'user',
        'content':ticket
    }]
    print('expected:',category, 'actual:',ask(prompt))