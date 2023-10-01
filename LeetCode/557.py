class Solution:
    def reverseWords(self, s: str) -> str:
        result = []

        for w in s.split():
            result.append(w[::-1])

        return " ".join(result)
