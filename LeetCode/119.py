from math import comb


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for i in range(rowIndex + 1):
            result.append(comb(rowIndex, i))

        return result
