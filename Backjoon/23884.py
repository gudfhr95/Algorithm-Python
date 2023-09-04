import heapq
import sys

N, K = map(int, input().split())
A = [*map(int, input().split())]

valuePq = []
indexPq = []
indexMap = {}
for i, e in enumerate(A):
    heapq.heappush(valuePq, (-e, e))
    heapq.heappush(indexPq, (-i, e))
    indexMap[e] = i

result = [0] * N
index = N - 1
while K > 0:
    if len(valuePq) == 0:
        print(-1)
        sys.exit()

    _, curValue = heapq.heappop(valuePq)
    curIndex = indexMap[curValue]

    while indexPq[0][1] > curValue or abs(indexPq[0][0]) > index:
        heapq.heappop(indexPq)
    _, lastValue = heapq.heappop(indexPq)
    lastIndex = indexMap[lastValue]

    if curIndex != lastIndex:
        K -= 1

    result[index] = curValue

    indexMap[lastValue] = curIndex
    del indexMap[curValue]
    heapq.heappush(indexPq, (-curIndex, lastValue))
    index -= 1

for k, v in indexMap.items():
    result[v] = k

print(" ".join(list(map(str, result))))
