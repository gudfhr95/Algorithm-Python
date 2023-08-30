N = int(input())
path = [*map(int, input().split())]

parent = [-1] * (max(path) + 1)
for i in range(1, N):
    p = path[i - 1]
    c = path[i]

    if parent[c] == -1 and parent[p] != c:
        parent[c] = p

print(len(parent))
print(" ".join(map(str, parent)))
