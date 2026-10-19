from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
#logic of top k and top p sampling in next word prediction
scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}
#USING MATHMATICAL FORMULA FOR TOP K AND TOP P SAMPLING
import math
def softmax(scores):
    exp_scores ={word:math.exp(score) for word, score in scores.items()}
    total = sum(exp_scores.values())  #total sum of the exponential scores of all the words(tokens)
    return {word:exp_score/total for word, exp_score in exp_scores.items()} 
probabilities = softmax(scores)
kept , total = [], 0.0
sorted_scores = sorted(probabilities,key = probabilities.get,reverse=True)  #sorting the words(tokens) based on their probabilities in descending order or sorting them based on their likelihood
#here we are choosing 0.9 as the threshold of probability
print(sorted_scores)
for word in sorted_scores:
    if total>=0.9:
        break
    kept.append(word)
    total+=probabilities[word]
print(f"Top p sampling: {kept} with total probability: {total}")    


#USING GROQ API FOR TOP K AND TOP P SAMPLING
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  
#USING VARIOUS PROBABILITIES FOR TOP P SAMPLING
for top_p in [0.5,0.7,0.8]: 
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": "Suggest a name for a cafe. Reply with the name only."}],
        top_p=top_p,
        temperature=0.9,
    )
    print(f"Top p: {top_p}")
    print(f"Response: {response.choices[0].message.content}\n")


for model in client.models.list().data:
    if model.id == "openai/gpt-oss-120b":
        print(model.supported_sampling_parameters)    