def fromOctal(n):
    result = 0

    for c in n:
        result *= 8

        if ord(c) >= ord('8'):
            return 0

        result += ord(c) - ord('0')

    return result


def fromHexadecimal(n):
    result = 0

    for c in n:
        result *= 16
        result += ord(c) - ord('0')

    return result


T = int(input())
for _ in range(T):
    K, N = map(str, input().split())

    print("%s %d %d %d" % (K, fromOctal(N), int(N), fromHexadecimal(N)))
