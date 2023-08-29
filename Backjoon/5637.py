import sys

result = ""
maxLength = 0

cur = ""
for line in sys.stdin:
    for c in line:
        if not (c.isalpha() or c == '-'):
            if len(cur) > maxLength:
                result = cur
                maxLength = len(cur)
            cur = ""
        else:
            if c.isalpha():
                cur += c.lower()
            else:
                cur += c

print(result)
