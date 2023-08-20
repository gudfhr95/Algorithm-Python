import heapq

isPrime = [True for _ in range(5000000)]
isPrime[0] = isPrime[1] = False
for i in range(2, int(5000000 ** 0.5) + 1):
    if not isPrime[i]:
        continue

    for j in range(i * i, 5000000, i):
        isPrime[j] = False

N = int(input())
dHeap = []
gHeap = []
dScore = 0
gScore = 0
for _ in range(N):
    d, g = map(int, input().split())

    if not isPrime[d]:
        if len(gHeap) < 3:
            gScore += 1000
        else:
            _, a = heapq.heappop(gHeap)
            _, b = heapq.heappop(gHeap)
            _, c = heapq.heappop(gHeap)

            gScore += c

            heapq.heappush(gHeap, (-c, c))
            heapq.heappush(gHeap, (-b, b))
            heapq.heappush(gHeap, (-a, a))
    elif (-d, d) in dHeap or (-d, d) in gHeap:
        dScore -= 1000
    else:
        heapq.heappush(dHeap, (-d, d))

    if not isPrime[g]:
        if len(dHeap) < 3:
            dScore += 1000
        else:
            _, a = heapq.heappop(dHeap)
            _, b = heapq.heappop(dHeap)
            _, c = heapq.heappop(dHeap)

            dScore += c

            heapq.heappush(dHeap, (-c, c))
            heapq.heappush(dHeap, (-b, b))
            heapq.heappush(dHeap, (-a, a))
    elif (-g, g) in dHeap or (-g, g) in gHeap:
        gScore -= 1000
    else:
        heapq.heappush(gHeap, (-g, g))

if dScore > gScore:
    print("소수의 신 갓대웅")
elif gScore > dScore:
    print("소수 마스터 갓규성")
else:
    print("우열을 가릴 수 없음")
