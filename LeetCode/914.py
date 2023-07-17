class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}

        for d in deck:
            if d not in count:
                count[d] = 0

            count[d] += 1

        for i in range(2, 10000):
            result = True
            for k, v in count.items():
                if v % i != 0:
                    result = False
                    break

            if result:
                return True

        return False
