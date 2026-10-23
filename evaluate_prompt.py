import os
from dotenv import load_dotenv

load_dotenv()
from groq import Groq
from typing import Literal
from pydantic import BaseModel, Field, ValidationError


# class for representing the structure of an output
class structured_output(BaseModel):
    category: Literal[
        "billing", "shipping", "other"
    ]  # category data must be among these values
    priority: int = Field(ge=1, le=5)  # here the priority can be from 1 to 5,


# function to check the structure of an output
def check(answer):
    try:
        return structured_output.model_validate_json(
            answer
        )  # checking the structure of an output
    except ValidationError:
        return None


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# function to have conversation with LLM
def ask(messages, **settings):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b", messages=messages, **settings
    )
    return response.choices[0].message.content


structured = """You sort customer support tickets for an online shop.

Categories:
- billing: payments, charges, refunds
- shipping: parcels, delivery, damaged boxes
- other: anything else

Reply with one line of JSON and nothing else, like this:
{"category": "shipping", "priority":5}
priority is 1 (can wait) to 5 (urgent)
"""


# LOGIC OF FEW-SHOT PROMPTING
examples = [
    {"role": "user", "content": "you took money from my account without permission"},
    {"role": "assistant", "content": '{"category": "billing", "priority": 5}'},
    {"role": "user", "content": "Where is my delivery? It is a week late"},
    {"role": "assistant", "content": '{"category": "shipping", "priority": 4}'},
    {"role": "user", "content": "Can I change the email on my account?"},
    {"role": "assistant", "content": '{"category": "other", "priority": 1}'},
    {"role": "user", "content": "Can I make payment?"},
    {"role": "assistant", "content": '{"category": "billing", "priority": 2}'},
]


tickets = [
    ("I was charged twice for one order", "billing"),
    ("My parcel has not arrived", "shipping"),
    ("Can I get a refund for the blue mug?", "billing"),
    ("How do I change my password?", "other"),
    ("The parcel arrived but the box was crushed", "shipping"),
    ("The courier asked me to pay a delivery fee at the door", "billing"),
    ("I want to stop my subscription", "billing"),
]


# checking the output using the structured prompt
def evaluate_prompt(tickets):
    prompts_variety = {
        "structured": structured,
        "vague": """You sort the online shop's tickets.""",
        "examples": structured,
    }

    total_score = {}
    for content_type, content in prompts_variety.items():
        score = 0
        for ticket, category in tickets:
            if content_type == "examples":
                prompt = [
                    {"role": "system", "content": content},
                    *examples,  #few-shot prompting by unpacking the examples
                    {"role": "user", "content": ticket}
                ]
            else:
                prompt = [
                    {"role": "system", "content": content},
                    {"role": "user", "content": ticket},
                ]
            response = check(ask(prompt))

            if response and response.category == category:
                score += 1
        total_score[content_type] = score/len(tickets)

    return total_score


print("The evaluation score of prompt is:", evaluate_prompt(tickets))
