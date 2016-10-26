from collections import defaultdict
x = defaultdict(lambda: 0)
x[2,8] = 4
x[2] = 4
[print(y) for y in x.items() if type(y[0]) == tuple]
print(len(x))