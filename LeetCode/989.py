class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        added = k
        for i, e in enumerate(num[::-1]):
            added += e * (10 ** i)

        result = []
        while added > 0:
            result.append(added % 10)
            added //= 10

        result.reverse()

        return result
