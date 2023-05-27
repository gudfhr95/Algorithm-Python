class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cur = -1
        while (n > 0):
            mod = n % 2
            if (mod == cur):
                return False

            n = n // 2
            cur = mod

        return True
