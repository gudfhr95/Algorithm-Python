import math

n = int(input())

s = int(math.sqrt(n))

if s * s >= n:
    print(s)
else:
    print(s + 1)
