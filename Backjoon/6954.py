highCards = {
    "jack": 1,
    "queen": 2,
    "king": 3,
    "ace": 4
}
players = {
    0: 'A',
    1: 'B'
}

cards = [input() for _ in range(52)]

score = {
    'A': 0,
    'B': 0
}

for i, card in enumerate(cards):
    if card in highCards:
        if i + highCards[card] > 51:
            continue

        scored = True
        for j in range(i + 1, i + 1 + highCards[card]):
            if cards[j] in highCards:
                scored = False

        if scored:
            print("Player %s scores %s point(s)." % (players[i % 2], highCards[card]))
            score[players[i % 2]] += highCards[card]

for k, v in score.items():
    print("Player %s: %d point(s)." % (k, v))
