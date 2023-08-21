def pickRow(row):
    d = [0] * len(row)
    d[0] = row[0]
    if len(row) >= 2:
        d[1] = row[1]
    if len(row) >= 3:
        d[2] = max(row[0] + row[2], row[1])

    for i in range(3, len(row)):
        d[i] = max(row[i] + d[i - 2], row[i] + d[i - 3], d[i - 1])

    return max(d)


def pick(row):
    d = [0] * len(row)
    d[0] = row[0]
    if len(row) >= 2:
        d[1] = row[1]
    if len(row) >= 3:
        d[2] = max(row[0] + row[2], row[1])

    for i in range(3, len(row)):
        d[i] = max(row[i] + d[i - 2], row[i] + d[i - 3], d[i - 1])

    return max(d)


while True:
    M, N = map(int, input().split())

    if M == 0 and N == 0:
        break

    boxes = [[*map(int, input().split())] for _ in range(M)]
    rowMax = [*map(lambda r: pickRow(r), boxes)]
    print(pick(rowMax))
