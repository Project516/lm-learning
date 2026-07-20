# age = 12

# print(age>=16)

# number = 9

# if(number % 2 == 0):
#     print("even")
# else:
#     print("odd")

# def paycheck(hours, rate):

#     """prints a paycheck for the coworker
#     Args:
#         hours: the hours the employee worked
#         rate: the hourly rate of payment
#     """

#     paycheck = 0
#     if (hours<=40):
#         paycheck += rate*hours
#     elif (40<=hours<=55):
#         paycheck += 100 + rate*hours
#     else:
#         print ("TOO MANY HOURS WORKED!")
#     return(paycheck)

# print(paycheck(609, 20))
# print(paycheck(45, 20))


# longhorn_points = [38, 45, 21, 31, 27]

# opponent_points = [20, 14, 24, 10, 34]


# longhorn_points.append(42)
# opponent_points.append(7)


# if(longhorn_points[0]>opponent_points[0]):
#     print("win")
# else:
#     print("lose")


def checkTemperatures(temperature):
    tempCheck = ""
    if temperature > 90:
        tempCheck = "hot"
        return tempCheck
    elif temperature > 60:
        tempCheck = "nice"
        return tempCheck
    else:
        return "cold"


print(checkTemperatures(95))
print(checkTemperatures(72))
print(checkTemperatures(40))
