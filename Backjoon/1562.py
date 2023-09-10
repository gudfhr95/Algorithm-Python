N = int(input())

d = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10):
    d[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(1 << 10):
            if 0 <= j - 1 < 10:
                d[i][j][k | (1 << j)] += d[i - 1][j - 1][k]

            if 0 <= j + 1 < 10:
                d[i][j][k | (1 << j)] += d[i - 1][j + 1][k]

            d[i][j][k | (1 << j)] %= 1_000_000_000

result = 0
for j in range(10):
    result += d[N][j][1023]
    result %= 1_000_000_000

print(result)
