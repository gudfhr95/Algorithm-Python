n, b, a = map(int, input().split())
prices = [*map(int, input().split())]
prices.sort()

cur = 0
result = 0
for i in range(n):
    cur += prices[i] // 2
    if i >= a:
        cur += prices[i - a] // 2

    if cur > b:
        break

    result = i + 1

print(result)
