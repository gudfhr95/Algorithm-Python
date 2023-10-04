class Solution:
    def isFascinating(self, n: int) -> bool:
        result = str(n) + str(n * 2) + str(n * 3)

        count = [0] * 10
        for c in result:
            count[ord(c) - ord('0')] += 1

        if count[0] > 0:
            return False

        for i in range(1, 10):
            if count[i] != 1:
                return False

        return True
