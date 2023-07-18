class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = ""

        left = 0
        right = len(s) - 1

        while left < len(s):
            if right > 0 and not s[right].isalpha():
                right -= 1
                continue

            if s[left].isalpha():
                result += s[right]
                right -= 1
                left += 1
            else:
                result += s[left]
                left += 1

        return result
