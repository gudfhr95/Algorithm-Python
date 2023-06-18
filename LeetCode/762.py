class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        result = 0
        for i in range(left, right + 1):
            if self.isPrime(self.getSetBits(i)):
                result += 1

        return result

    def getSetBits(self, n: int) -> int:
        result = 0

        while n > 0:
            result += n % 2
            n //= 2

        return result

    def isPrime(self, n: int) -> bool:
        if n == 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True
