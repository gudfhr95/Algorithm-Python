def getPrimeNumbers(n):
    isPrime = [True for _ in range(n + 1)]
    isPrime[1] = False

    for i in range(2, int(n ** 0.5)):
        if not isPrime[i]:
            continue

        for j in range(i * i, n + 1, i):
            isPrime[j] = False

    result = []
    for i in range(2, n + 1):
        if isPrime[i]:
            result.append(i)

    return result


primeNumbers = getPrimeNumbers(10000000)
d = [0 for _ in range(10000001)]
d[1] = 1
for p in primeNumbers:
    cur = p
    count = 2
    while cur <= 10000000:
        d[cur] = count
        cur *= p
        count += 1

for i in range(1, 10000001):
    for p in primeNumbers:
        cur = i * p
        if cur > 10000000:
            break

        count = 2
        while cur <= 10000000:
            if d[cur] == 0:
                d[cur] = d[i] * count

            cur *= p
            count += 1

C = int(input())
for _ in range(C):
    L, U = map(int, input().split())

    print(max(d[L:U + 1]))
