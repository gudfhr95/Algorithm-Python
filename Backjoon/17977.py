diameter = [0] * 1_000_001
diameter[3] = 0
diameter[4] = 1

for i in range(5, 1_000_001):
    diameter[i] = diameter[(i + 1) // 2] + 2

n = int(input())
print(diameter[n])
