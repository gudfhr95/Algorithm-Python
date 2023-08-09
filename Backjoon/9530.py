N, G = map(int, input().split())

matches = []
for _ in range(N):
    S, R = map(int, input().split())
    matches.append((S, R))

matches.sort(key=lambda x: x[1] - x[0])

result = 0
for match in matches:
    if match[0] > match[1]:
        result += 3
    elif match[0] == match[1] and G > 0:
        G -= 1
        result += 3
    else:
        if G >= match[1] - match[0] + 1:
            G -= match[1] - match[0] + 1
            result += 3
        elif G == match[1] - match[0]:
            G -= match[1] - match[0]
            result += 1

print(result)
