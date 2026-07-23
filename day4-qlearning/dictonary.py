ages = {"bob": 21, "joe": 32, "jimmy": 35}

print(ages["bob"])

ages["guy"] = 43

if "joe" in ages:
    print(ages["joe"])

for a in ages:
    print(ages[a])

classes = {"math": {"mr smith": 322}}

print(classes["math"]["mr smith"])
