# import math          # opens the math toolbox; do this once, at the top

# print(math.sqrt(9))  # square root of 9
# print(math.sqrt(2))  # square root of 2, not a whole number

# import math

# point_a = [1.4, 0.2]    # a setosa-ish flower: short, narrow petal
# point_b = [4.5, 1.5]    # a versicolor-ish flower: longer, wider petal

# diff_length = point_a[0] - point_b[0]   # difference in the first feature
# diff_width  = point_a[1] - point_b[1]   # difference in the second feature
# print("length difference:", diff_length)
# print("width difference:", diff_width)

# squared_sum = diff_length**2 + diff_width**2   # square each, then add
# print("squared sum:", squared_sum)

# d = math.sqrt(squared_sum)              # square root of that sum
# print("distance:", d)

import math

point_a = [1.4, 0.2]
point_b = [1.4, 0.2]    # almost the same flower as point_a

d = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
print("distance between two similar flowers:", d)

