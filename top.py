#logic of top k and top p sampling in next word prediction
scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}

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