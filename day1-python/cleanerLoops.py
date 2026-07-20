letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)

prices = [4, 9, 2]
quantities = [2, 1, 5]

for price, quantity in zip(prices, quantities):
    print(price * quantity)
