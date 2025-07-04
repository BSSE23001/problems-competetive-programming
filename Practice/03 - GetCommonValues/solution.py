v = [1,2,3,4,5,4,7,4,9,4]
v2 = [1,2,3,4,4,7,9,4]

v = set(v)
v2 = set(v2)

v = v.intersection(v2)

print(" ".join(map(str,v)))