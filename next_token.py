# made-up scores for the word after "The cat sat on the"
scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}

import math
def softmax(scores):
    exp_scores ={word:math.exp(score) for word, score in scores.items()}
    total = sum(exp_scores.values())  #total sum of the exponential scores of all the words(tokens)
    return {word:exp_score/total for word, exp_score in exp_scores.items()}  #returning the softmax probabilities for each word(token)
next_token_probabilities = softmax(scores)
print(next_token_probabilities)
next_word = max(next_token_probabilities, key=next_token_probabilities.get)  #finding the word with the highest probability
print(f"The next word is: {next_word} with probability: {next_token_probabilities[next_word]}")
