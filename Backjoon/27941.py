import math

l = [math.inf for _ in range(11)]
r = [-math.inf for _ in range(11)]
s = [0 for _ in range(11)]

for _ in range(2047):
    p = [*map(int, input().split())]

    for i, e in enumerate(p):
        l[i] = min(l[i], e)
        r[i] = max(r[i], e)
        s[i] += e

result = []
for i in range(11):
    result.append(l[i] * 1024 + r[i] * 1024 - s[i])

print(" ".join(map(str, result)))
