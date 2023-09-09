def play(seq, t):
    cur = seq
    next = []
    while len(cur) > 2:
        left = 0
        right = len(cur) - 1

        while left <= right:
            next.append(cur[left] + cur[right])
            left += 1
            right -= 1

        cur = next
        next = []

    winner = "Alice" if cur[0] > cur[1] else "Bob"

    print("Case #%d: %s" % (t, winner))


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    seq = [*map(int, input().split())]
    play(seq, t)
