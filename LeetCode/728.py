class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            if self.isSelfDividingNumber(i):
                result.append(i)

        return result

    def isSelfDividingNumber(self, number: int) -> bool:
        cur = number
        while cur > 0:
            mod = cur % 10

            if mod == 0 or number % mod != 0:
                return False

            cur = cur // 10

        return Tru
