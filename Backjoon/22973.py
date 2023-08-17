import sys

K = abs(int(input()))

if K == 0:
    print(0)
    sys.exit()

if K % 2 == 0:
    print(-1)
    sys.exit()

for i in range(1, 41):
    if K <= (2 ** i - 1):
        print(i)
        sys.exit()
