class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = [987654321 for _ in range(len(s))]

        for i in range(len(s)):
            if s[i] == c:
                result[i] = 0
                continue

            if i - 1 >= 0:
                result[i] = min(result[i], result[i - 1] + 1)

            if i + 1 < len(s):
                result[i] = min(result[i], result[i + 1] + 1)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                result[i] = 0
                continue

            if i - 1 >= 0:
                result[i] = min(result[i], result[i - 1] + 1)

            if i + 1 < len(s):
                result[i] = min(result[i], result[i + 1] + 1)

        return resul
