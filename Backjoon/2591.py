N = input()

d = [0] * len(N)
d[0] = 1
if N[1] != '0':
    d[1] += 1
if int(N[:2]) <= 34:
    d[1] += 1

for i in range(2, len(N)):
    if N[i] != '0':
        d[i] += d[i - 1]

    if 10 <= int(N[i - 1:i + 1]) <= 34:
        d[i] += d[i - 2]

print(d[len(N) - 1])
