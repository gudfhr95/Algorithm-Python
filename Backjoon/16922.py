from itertools import combinations_with_replacement

numbers = [1, 5, 10, 50]

N = int(input())

combination = combinations_with_replacement(numbers, N)

result = set()
for c in combination:
    result.add(sum(c))

print(len(result))
