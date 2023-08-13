import sys

p, q, N, M = map(int, input().split())

target = q - p
for r in range(1, M):
    for g in range(r, M):
        if r + g > M or r + g < N:
            continue

        if (r * (r - 1) + g * (g - 1)) / ((r + g) * (r + g - 1)) * q == target:
            print(r, g)
            sys.exit()

print("NO SOLUTION")
