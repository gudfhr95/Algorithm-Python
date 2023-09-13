import math

c = int(input())
for _ in range(c):
    n, l1, l2, s1, s2 = map(int, input().split())
    p1 = [*map(int, input().split())]
    d1 = [*map(int, input().split())]
    p2 = [*map(int, input().split())]
    d2 = [*map(int, input().split())]

    result = [[math.inf, math.inf] for _ in range(n)]
    result[0][0] = l1
    result[0][1] = l2
    for i in range(1, n):
        result[i][0] = min(result[i][0], result[i - 1][0] + d1[i - 1], result[i - 1][1] + p2[i - 1])
        result[i][1] = min(result[i][1], result[i - 1][1] + d2[i - 1], result[i - 1][0] + p1[i - 1])

    print(min(result[n - 1][0] + s1, result[n - 1][1] + s2))
