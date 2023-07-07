class Solution:
    def binaryGap(self, n: int) -> int:
        result = 0
        prev = -1
        cur = 0

        while n > 0:
            mod = n % 2

            if mod == 1:
                if prev != -1:
                    result = max(result, cur - prev)
                prev = cur

            n //= 2
            cur += 1

        return result
