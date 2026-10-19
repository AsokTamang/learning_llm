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



#a complete sentence with the logic of next word prediction
next_word ={
    "Your": {"refund": 0.6, "parcel": 0.4},
    "refund": {"is": 0.7, "was": 0.3},
    "is": {"on": 0.6, "late": 0.4},
    "on": {"its": 0.8, "the": 0.2},
    "its": {"way.": 0.9, "own": 0.1},
}

complete_sentence = ['Your']
while complete_sentence[-1] in next_word:
    options = next_word[complete_sentence[-1]]
    next_word_choice = max(options, key=options.get)  #choosing the next word with the highest probability
    complete_sentence.append(next_word_choice)  #adding the likely next word to the list of sentence
print(" ".join(complete_sentence))  