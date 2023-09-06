import sys

N, M = map(int, input().split())
equations = [[*map(int, input().split())] for _ in range(M)]

for i in range(1 << (N + 1)):
    n = i
    booleans = [0] * (N + 1)
    index = 0
    while n > 0:
        booleans[index] = n & 1
        n >>= 1
        index += 1

    result = True
    for (xi, xj) in equations:
        bi = booleans[abs(xi)]
        if xi < 0:
            bi = not bi

        bj = booleans[abs(xj)]
        if xj < 0:
            bj = not bj

        if not (bi or bj):
            result = False

    if result:
        print(1)
        print(" ".join(map(str, booleans[1:])))
        sys.exit()

print(0)
