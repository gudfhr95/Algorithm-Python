import sys

name = input()

if name[0].isupper() or name[0] == '_':
    print("Error!")
    sys.exit()

if name[-1] == '_':
    print("Error!")
    sys.exit()

result = ""

isJava = not '_' in name
if isJava:
    for i in range(len(name)):
        if name[i].isupper():
            result += '_'
        result += name[i].lower()
else:
    toUpper = False
    for i in range(len(name)):
        if name[i].isupper():
            print("Error!")
            sys.exit()

        if name[i] == '_':
            if toUpper:
                print("Error!")
                sys.exit()

            toUpper = True
            continue

        if toUpper:
            result += name[i].upper()
        else:
            result += name[i]
        toUpper = False

print(result)
