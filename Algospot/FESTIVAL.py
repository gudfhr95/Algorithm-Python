import sys


def minimum_average_price(l, prices):
    prefix_sum = [0]
    for price in prices:
        prefix_sum.append(prefix_sum[-1] + price)

    result = sys.float_info.max
    for i in range(len(prefix_sum)):
        for j in range(i + l, len(prefix_sum)):
            result = min(result, (prefix_sum[j] - prefix_sum[i]) / float(j - i))

    return result


C = int(input())

for _ in range(C):
    _, L = map(int, input().split())
    prices = list(map(int, input().split()))

    print(minimum_average_price(L, prices))
