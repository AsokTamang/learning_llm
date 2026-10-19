import os
from dotenv import load_dotenv
load_dotenv()

scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}

import math
def softmax(scores):
    exp_scores ={word:math.exp(score) for word, score in scores.items()}
    total = sum(exp_scores.values())  #total sum of the exponential scores of all the words(tokens)
    return {word:exp_score/total for word, exp_score in exp_scores.items()} 

temperatures = [0.2, 0.5, 0.8]
final = {}
for temp in temperatures:
    scaled_scores = {word: score / temp for word, score in scores.items()}  #scaling the scores based on the temperature
    next_token_probabilities = softmax(scaled_scores)
    final[temp] = next_token_probabilities
print(final)    
    
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 
prompt = [{"role": "user", "content": "Suggest a name for a cafe. Reply with the name only."}]

for temperature in [0.2, 0.5, 0.8]:
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=temperature,
    )
    print(f"Temperature: {temperature}")
    print(f"Response: {response.choices[0].message.content}\n")