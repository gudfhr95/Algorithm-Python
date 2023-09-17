import heapq

N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
exits = [0]

for _ in range(M):
    a, b, c = map(int, input().split())

    adj[a].append((c, b))
    adj[b].append((c, a))

exits.extend([*map(int, input().split())])

pq = []
for i in range(1, N + 1):
    heapq.heappush(pq, (exits[i], i))

result = 0
visited = [False] * (N + 1)
while len(pq) > 0:
    curExit, curIndex = heapq.heappop(pq)

    if visited[curIndex]:
        continue

    result += curExit
    visited[curIndex] = True

    for nextCost, nextIndex in adj[curIndex]:
        heapq.heappush(pq, (nextCost, nextIndex))

print(result)
