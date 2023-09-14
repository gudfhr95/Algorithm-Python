import math
import sys
from collections import deque


def getDist(start, adj):
    result = [math.inf] * len(adj)

    q = deque()
    q.append(start)
    result[start] = 0

    while len(q) > 0:
        cur = q.popleft()

        for next in adj[cur]:
            if result[next] != math.inf:
                continue

            q.append(next)
            result[next] = result[cur] + 1

    return result


N = int(input())

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())

    adj[u].append(v)
    adj[v].append(u)

a, b, c = map(int, input().split())

aDist = getDist(a, adj)
bDist = getDist(b, adj)
cDist = getDist(c, adj)

for i in range(1, N + 1):
    if len(adj[i]) == 1:
        if aDist[i] < bDist[i] and aDist[i] < cDist[i]:
            print("YES")
            sys.exit()

print("NO")
