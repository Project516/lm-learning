longhorn_points = [38, 45, 21, 31, 27]
opponent_points = [20, 14, 24, 10, 34]

longhorn_points.append(42)
opponent_points.append(7)

# if(longhorn_points[0]>opponent_points[0]):
#     print("win")
# else:
#     print("lose")

# total = 0
# for lp in longhorn_points:
#     total += lp

# print(total)

# optotal = 0
# for op in opponent_points:
#     optotal += op

# print(optotal)

# biggest = longhorn_points[0]

# for n in longhorn_points:
#     if n > biggest:
#         biggest = n

# print(biggest)

# total = 0


# for i in range(len(longhorn_points)):
#     if longhorn_points[i] > opponent_points[i]:
#         print(i, "win")
#         total += 1
#     else:
#         print(i, "loss")

# print(total)

for opp, lhp in zip(opponent_points, longhorn_points):
    if lhp > opp:
        print("win")
    else:
        print("lose")
