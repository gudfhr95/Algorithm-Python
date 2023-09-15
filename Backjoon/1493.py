import heapq
import sys

length, width, height = sorted(map(int, input().split()), reverse=True)
N = int(input())
cubes = [0] * 20
for _ in range(N):
    a, b = map(int, input().split())
    cubes[a] = b

q = []
heapq.heappush(q, (-length, length, width, height))

result = 0
while len(q) > 0:
    _, x, y, z = q.pop()

    canMake = False
    for i in range(len(cubes) - 1, -1, -1):
        if cubes[i] == 0:
            continue

        size = 2 ** i
        if size > x or size > y or size > z:
            continue

        result += 1
        cubes[i] -= 1
        canMake = True

        if z > size:
            q.append((-x, x, y, z - size))
        if x > size:
            q.append((size - x, x - size, size, size))
        if y > size:
            q.append((-x, x, y - size, size))

        break

    if not canMake:
        print(-1)
        sys.exit()

print(result)
