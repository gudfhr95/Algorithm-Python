class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left = 0
        right = 1
        result = 0

        while left < len(s) and right < len(s):
            if s[left] == s[right]:
                left += 1
                right += 1
                continue

            result += 1

            tempL = left - 1
            tempR = right + 1
            while tempL >= 0 and tempR < len(s):
                if s[tempL] != s[left] or s[tempR] != s[right]:
                    break

                result += 1
                tempL -= 1
                tempR += 1

            left += 1
            right += 1

        return result
