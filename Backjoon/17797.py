import math


def dist(pos):
    sum = math.pow(pos[0], 2) + math.pow(pos[1], 2) + math.pow(pos[2], 2)
    return math.sqrt(sum)


n, k = map(int, input().split())

clouds = []
for _ in range(n):
    x, y, z = map(float, input().split())
    clouds.append((x, y, z))

clouds.sort(key=lambda x: dist(x))

print(dist(clouds[k - 1]))
