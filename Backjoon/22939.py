import math
from itertools import permutations

field = {
    "J": "Assassin",
    "C": "Healer",
    "B": "Mage",
    "W": "Tanker"
}


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


N = int(input())

board = []
for _ in range(N):
    board.append(input())

home = ()
cookie = ()
topping = {
    'J': [],
    'C': [],
    'B': [],
    'W': []
}
for y in range(N):
    for x in range(N):
        if board[y][x] == 'X':
            continue

        if board[y][x] == 'H':
            home = (x, y)
        elif board[y][x] == '#':
            cookie = (x, y)
        else:
            topping[board[y][x]].append((x, y))

result = {
    'J': math.inf,
    'C': math.inf,
    'B': math.inf,
    'W': math.inf
}
minValue = math.inf
for k, v in topping.items():
    permutation = permutations(v, 3)

    for p in permutation:
        d = dist(home, p[0]) + dist(p[0], p[1]) + dist(p[1], p[2]) + dist(p[2], cookie)

        result[k] = min(result[k], d)
        minValue = min(minValue, d)

for k, v in result.items():
    if v == minValue:
        print(field[k])
        break
