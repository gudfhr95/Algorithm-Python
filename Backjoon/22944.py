import math
from itertools import permutations


def go(start, end, umbrellas):
    result = 0

    curPos = start
    curHealth = H
    curUmbrella = 0
    for u in umbrellas:
        d = abs(curPos[0] - u[0]) + abs(curPos[1] - u[1])
        if d > (curHealth + curUmbrella):
            return math.inf

        curPos = u
        curHealth -= (d - 1)
        curUmbrella = D - 1

        result += d

    d = abs(curPos[0] - end[0]) + abs(curPos[1] - end[1])
    if d > (curHealth + curUmbrella):
        return math.inf

    result += d

    return result


N, H, D = map(int, input().split())
grid = [input() for _ in range(N)]

start = ()
end = ()
umbrellas = []
for y in range(N):
    for x in range(N):
        if grid[y][x] == 'S':
            start = (x, y)
        elif grid[y][x] == 'E':
            end = (x, y)
        elif grid[y][x] == 'U':
            umbrellas.append((x, y))

result = math.inf
for i in range(len(umbrellas) + 1):
    for u in permutations(umbrellas, i):
        d = go(start, end, u)
        result = min(result, d)

if result == math.inf:
    print(-1)
else:
    print(result)
