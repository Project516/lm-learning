# 4 + 2

print(4 + 2)

# four basic operations
print(4 - 2)  # subtraction, gives 2
print(4 * 2)  # multiplication, gives 8
print(4 / 2)  # division, gives 2.0

# spacing doesnt matter
print(4 - 2)  # subtraction
print(4 * 2)  # multiplication
print(4 / 2)  # division

# other symbols
print(4**2)  # power: 4 to the 2nd, gives 16
print(7 % 2)  # remainder of 7 divided by 2, gives 1

# order of operations
print(4 - 2 * 6)  # -8
print((4 - 2) * 6)  # 12

# data types
print(int)  # <class 'int'>
print(float)  # <class 'float'>
print(str)  # <class 'str'>

# strings != numbers
print(5 + 5)  # adds numbers, gives 10
print("5" + "5")  # glues strings, gives 55

# vars
number_one = 5.5
number_two = 10

print(number_one + number_two)
print(number_one * number_two)

answer = number_one + number_two
print(answer)

new_answer = answer * 2
print(new_answer, answer)

answer = 1
print(answer)
answer = number_one + 10
print(answer)

answer = answer + 2
print(answer)

print(type(answer))
