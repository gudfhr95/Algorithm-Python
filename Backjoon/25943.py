n = int(input())
rocks = [*map(int, input().split())]
weights = [100, 50, 20, 10, 5, 2, 1]

left = rocks[0]
right = rocks[1]

for i in range(2, n):
    if left == right:
        left += rocks[i]
    elif left > right:
        right += rocks[i]
    else:
        left += rocks[i]

result = 0
diff = abs(left - right)
for w in weights:
    result += diff // w
    diff %= w

print(result)
