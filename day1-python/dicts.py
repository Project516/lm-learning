# friends = {"Ben" : 16, "Joe" : 17, "Bob" : 18}
# friends["Kai"] = 19

# print(friends)
# print(friends.get("Jo", 0))

# string = "mississippi"

# counts = {}
# for char in string:
#     counts[char] = counts.get((char), 0) + 1

# for char, number in counts.items():
#     if (number > 2):
#         print(char)

# print(counts)

# words = ["hi", "hello", "hey", "howdy", "yo"]

# big = [ words[n] for n in range(len(words)) if (len(words[n])>3)]

# print(big)

words = ["hi", "hello", "hey", "howdy", "yo"]

big = [ len(word) for word in words]

print(big)