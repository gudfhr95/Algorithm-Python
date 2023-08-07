def isPretty(n, p):
    l = [0] * 4
    while n > 0:
        mod = n % p

        if mod >= 3:
            l[3] += 1
        else:
            l[mod] += 1
        n //= p

    if l[3] > 0:
        return 0
    elif l[1] == 1 and l[2] > 0:
        return 1
    elif l[1] == 2 and l[2] == 0:
        return 1

    return 0


p, n1, n2, n3, n4 = map(int, input().split())
print(isPretty(n1, p), end=" ")
print(isPretty(n2, p), end=" ")
print(isPretty(n3, p), end=" ")
print(isPretty(n4, p), end=" ")
