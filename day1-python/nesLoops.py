# grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# total = 0
# items = 0
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         total += grid[i][j]
#         items+=1

# print(total)
# print(items)

# for i in range(1,4):
#     for j in range(1,5):
#         print(i, j)

# task 3
# for i in range(2,5):
#     for j in range(1,6):
#         print(i, " * ", j, " = ", i * j)

# task 4

# def isEven(num):
#     if (num % 2 == 0):
#         return True
#     else:
#         return False

string = ""
for i in range(0, 4):
    for j in range(0, 4):
        if (i + j) % 2 == 0:
            string += "#"
        else:
            string += "."
    string += "\n"
print(string)
