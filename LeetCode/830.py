class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []

        count = 1
        start = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                if count >= 3:
                    result.append([start, i - 1])
                count = 1
                start = i

        if count >= 3:
            result.append([start, len(s) - 1])

        return result
