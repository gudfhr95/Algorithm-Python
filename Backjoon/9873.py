from bisect import bisect_left, bisect_right

N = int(input())
locations = [int(input()) for _ in range(N)]
locations.sort()

result = 0
for x in range(N):
    for y in range(x + 1, N):
        d = locations[y] - locations[x]

        left = bisect_left(locations, locations[y] + d)
        right = bisect_right(locations, locations[y] + (2 * d))

        result += (right - left)

print(result)
