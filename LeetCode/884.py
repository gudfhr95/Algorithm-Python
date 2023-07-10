class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1 = {}
        for word in s1.split(" "):
            if word not in c1:
                c1[word] = 0

            c1[word] += 1

        c2 = {}
        for word in s2.split(" "):
            if word not in c2:
                c2[word] = 0

            c2[word] += 1

        result = []
        for key in c1:
            if c1[key] >= 2:
                continue

            if key in c2:
                continue

            result.append(key)

        for key in c2:
            if c2[key] >= 2:
                continue

            if key in c1:
                continue

            result.append(key)

        return result
