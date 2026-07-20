# foods = ["taco", "burger", "toast"]

# for food in foods:
#     print("I like", food)

# for i in range(1, 11):
#     print(i)

# for i in range(1, 6):
#     print(i * 2)

# list = [45, 67, 943, 345, 2343]
# biggest = list[0]

# for n in list:
#     if n > biggest:
#         biggest = n

# print(biggest)

# list = [45, 67, 943, 345, 2343]
# smallest = list[0]

# for n in list:
#     if n < smallest:
#         smallest = n

# print(smallest)

guesses = ["cat", "dog", "cat", "bird"]
answers = ["cat", "cat", "cat", "bird"]

total = 0


for i in range(len(guesses)):
    if guesses[i] == answers[i]:
        print(i, "correct")
        total += 1
    else:
        print(i, "wrong")

print(total)
