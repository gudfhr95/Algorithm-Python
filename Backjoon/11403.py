N = int(input())
dist = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dist[i][i] = 1

for y in range(N):
    for x, e in enumerate(map(int, input().split())):
        dist[y][x] = e

for k in range(N):
    for y in range(N):
        for x in range(N):
            if dist[y][k] == 1 and dist[k][x] == 1:
                dist[y][x] = 1

for y in range(N):
    print(" ".join(map(str, dist[y])))
