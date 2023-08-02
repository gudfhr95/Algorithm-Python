N = int(input())
slimes = [*map(int, input().split())]
slimes = sorted(slimes, reverse=True)

result = 0
slime = slimes[0]
for i in range(1, N):
    result += slime * slimes[i]
    slime += slimes[i]

print(result)
