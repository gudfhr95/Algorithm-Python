import sys

for a in sys.stdin:
    b = sys.stdin.readline()

    aStr = a[:-1]
    bStr = b[:-1]

    aCount = [0] * 26
    bCount = [0] * 26
    for c in aStr:
        aCount[ord(c) - ord('a')] += 1

    for c in bStr:
        bCount[ord(c) - ord('a')] += 1

    result = ""
    for i in range(26):
        result += chr(ord('a') + i) * min(aCount[i], bCount[i])

    print(result)
