# task 1
# num = 10

# while num>0:
#     print(num)
#     num-=1

# print("Done!")

# task 2
# names = ["Sam", "Alex", "Jo"]
# num = 0
# while (num<len(names)):
#     print(num, names[num])
#     num+=1

# task 3
# list = [1,2,3,4]
# tempList = list
# #counter = 0
# total = 0

# while (len(tempList) != 0):
#     total += tempList[0]
#     tempList.pop(0)

# print(total)

#task 4
list = [1, -2, 3, 4]
counter = 0
total = 0
while (counter < len(list)):
    if(list[counter]>0):
        total += list[counter]
    counter +=1

print(total)
