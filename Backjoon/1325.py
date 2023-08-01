import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, n):
    q = deque([])
    visited = [False for _ in range(n + 1)]

    q.append(start)
    visited[start] = True

    result = 1
    while q:
        cur = q.pop()

        for next in adj[cur]:
            if visited[next]:
                continue

            result += 1
            q.append(next)
            visited[next] = True

    return result


n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

hack = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    hack[i] = bfs(i, n)

max_hack = max(hack)
for i, e in enumerate(hack):
    if e == max_hack:
        print(i, end=" ")
