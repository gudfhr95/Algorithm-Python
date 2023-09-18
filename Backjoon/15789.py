from collections import deque


def getPower(start, adj, visited):
    q = deque()

    q.append(start)
    visited[start] = True
    result = 0

    while len(q) > 0:
        cur = q.popleft()
        result += 1

        for next in adj[cur]:
            if visited[next]:
                continue

            q.append(next)
            visited[next] = True

    return result


N, M = map(int, input().split())

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    X, Y = map(int, input().split())
    adj[X].append(Y)
    adj[Y].append(X)

C, H, K = map(int, input().split())

visited = [False] * (N + 1)
cPower = getPower(C, adj, visited)
hPower = getPower(H, adj, visited)
powers = []
for i in range(1, N + 1):
    if visited[i]:
        continue

    powers.append(getPower(i, adj, visited))

powers.sort(reverse=True)
for i in range(K):
    if K >= len(powers):
        break

    cPower += powers[i]

print(cPower)
