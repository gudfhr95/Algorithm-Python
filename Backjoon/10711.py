dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

H, W = map(int, input().split())

castle = [[] for _ in range(H)]
count = [[0 for _ in range(W)] for _ in range(H)]

for y in range(H):
    for c in input():
        if c == '.':
            castle[y].append(0)
        else:
            castle[y].append(int(c))

cur = []
for y in range(H):
    for x in range(W):
        for k in range(8):
            xn = x + dx[k]
            yn = y + dy[k]

            if xn < 0 or yn < 0 or xn >= W or yn >= H:
                continue

            if castle[yn][xn] == 0:
                count[y][x] += 1

        if 0 < castle[y][x] <= count[y][x]:
            cur.append((x, y))

result = 0
while len(cur) > 0:
    result += 1

    next = set()
    candidate = set()

    for (x, y) in cur:
        castle[y][x] = 0
        for k in range(8):
            xn = x + dx[k]
            yn = y + dy[k]

            if xn < 0 or yn < 0 or xn >= W or yn >= H:
                continue

            count[yn][xn] += 1
            candidate.add((xn, yn))

    for (x, y) in candidate:
        if 0 < castle[y][x] <= count[y][x]:
            next.add((x, y))

    cur = next

print(result)
