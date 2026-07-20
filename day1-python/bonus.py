guesses = ["cat", "dog", "cat", "bird", "dog"]
answers = ["cat", "cat", "cat", "bird", "dog"]

def ovAcc(guesses, answers):
    total = 0
    for guess, answer in zip(guesses, answers):
        if (guess == answer):
            total +=1
    return total

def labelCount(guesses, answers):
    dict = {}
    for guess, answer in zip(guesses, answers):
        if (guess == answer):
            dict[guess] = dict.get(guess, 0)+1
    return dict

def wrongGuess(guesses, answers):
    output = ""
    for i in range(len(guesses)):
        if(guesses[i] != answers[i]):
            output = output + (guesses[i] + " but the answer is " + answers[i])
    return output

print(ovAcc(guesses, answers))
print(labelCount(guesses, answers))
print(wrongGuess(guesses, answers))