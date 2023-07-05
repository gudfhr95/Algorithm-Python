class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {}
        changes[5] = changes[10] = 0

        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] == 0:
                    return False

                changes[5] -= 1
                changes[10] += 1
            elif bill == 20:
                if changes[10] > 0 and changes[5] > 0:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False

        return True
