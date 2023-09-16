import heapq

N, D = map(int, input().split())

presents = []
for _ in range(N):
    P, V = map(int, input().split())
    presents.append((P, V))

presents.sort()

result = 0

pq = []
s = 0
for P, V in presents:
    while len(pq) > 0 and abs(pq[0][0] - P) >= D:
        curP, curV = heapq.heappop(pq)
        s -= curV

    heapq.heappush(pq, (P, V))
    s += V

    result = max(result, s)

print(result)
