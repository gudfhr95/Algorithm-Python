for _ in range(100):
    samples = [float(input()) for _ in range(5000)]

    count = 0
    for s in samples:
        if s <= 0.05:
            count += 1

    if count >= 180:
        print("A")
    else:
        print("B")
