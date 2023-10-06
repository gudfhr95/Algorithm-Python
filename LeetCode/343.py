from functools import cache


class Solution:
    @cache
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1

        result = 0
        for i in range(1, n):
            result = max(result, i * self.integerBreak(n - i), i * (n - i))

        return result
