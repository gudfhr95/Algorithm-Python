import sys
from collections import deque

N, M = map(int, input().split())
doDeck = deque()
suDeck = deque()
for _ in range(N):
    d, s = map(int, input().split())
    doDeck.appendleft(d)
    suDeck.appendleft(s)

doGround = deque()
suGround = deque()
for i in range(M):
    if i % 2 == 0:
        doGround.appendleft(doDeck.popleft())
    else:
        suGround.appendleft(suDeck.popleft())

    if len(doDeck) == 0:
        print("su")
        sys.exit()
    elif len(suDeck) == 0:
        print("do")
        sys.exit()
    elif len(doDeck) == 0 and len(suDeck) == 0:
        print("dosu")
        sys.exit()

    if (len(doGround) > 0 and doGround[0] == 5) or (len(suGround) > 0 and suGround[0] == 5):
        while len(suGround) > 0:
            doDeck.append(suGround.pop())
        while len(doGround) > 0:
            doDeck.append(doGround.pop())
    elif len(doGround) > 0 and len(suGround) > 0 and (doGround[0] + suGround[0] == 5):
        while len(doGround) > 0:
            suDeck.append(doGround.pop())
        while len(suGround) > 0:
            suDeck.append(suGround.pop())

if len(doDeck) > len(suDeck):
    print("do")
elif len(suDeck) > len(doDeck):
    print("su")
else:
    print("dosu")
