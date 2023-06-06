class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0:
            return False

        if len(bits) == 1 and bits[0] == 0:
            return True

        if bits[0] == 0:
            return self.isOneBitCharacter(bits[1:])
        else:
            return self.isOneBitCharacter(bits[2:])
