A, B, C = map(int, input().split())
N = int(input())

result = 0
for _ in range(N):
    sum = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        sum += A * a + B * b + C * c

    result = max(result, sum)

print(result)
