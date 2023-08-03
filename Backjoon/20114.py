def getChar(x):
    for y in range(H):
        for xn in range(x, x + W):
            if strings[y][xn] != '?':
                return strings[y][xn]

    return '?'


N, H, W = map(int, input().split())
strings = []
for _ in range(H):
    strings.append(input())

result = ""
for x in range(0, N * W, W):
    result += getChar(x)

print(result)
