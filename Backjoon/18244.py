MOD = 1_000_000_007

N = int(input())

d = [[[0 for _ in range(5)] for _ in range(10)] for _ in range(101)]
for i in range(10):
    d[1][i][2] = 1

for i in range(2, 101):
    for j in range(10):
        if 0 <= j - 1 <= 9:
            d[i][j][3] += d[i - 1][j - 1][0] + d[i - 1][j - 1][1] + d[i - 1][j - 1][2]
            d[i][j][3] %= MOD

            d[i][j][4] += d[i - 1][j - 1][3]
            d[i][j][4] %= MOD

        if 0 <= j + 1 <= 9:
            d[i][j][1] += d[i - 1][j + 1][4] + d[i - 1][j + 1][3] + d[i - 1][j + 1][2]
            d[i][j][1] %= MOD

            d[i][j][0] += d[i - 1][j + 1][1]
            d[i][j][0] %= MOD

result = 0
for i in range(10):
    result += sum(d[N][i])
    result %= MOD

print(result)
