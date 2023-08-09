def isVowelMoreThanConsonant(s):
    vowel = 0
    consonent = 0

    for c in s:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowel += 1
        else:
            consonent += 1

    if vowel > consonent:
        return 1
    else:
        return 0


N = int(input())
for _ in range(N):
    s = input()
    print(s)
    print(isVowelMoreThanConsonant(s))
