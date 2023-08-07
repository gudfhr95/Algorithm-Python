N = int(input())

reversedBinary = bin(N)[2:][::-1]

result = 0
for c in reversedBinary:
    result *= 2
    result += ord(c) - ord('0')

print(result)
