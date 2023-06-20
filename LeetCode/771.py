class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set()

        for c in jewels:
            s.add(c)

        result = 0
        for c in stones:
            if c in s:
                result += 1

        return result
