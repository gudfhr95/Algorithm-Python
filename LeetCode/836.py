class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] >= rec2[0] and rec1[0] >= rec2[2]:
            return False

        if rec1[2] <= rec2[0] and rec1[2] <= rec2[2]:
            return False

        if rec1[1] >= rec2[1] and rec1[1] >= rec2[3]:
            return False

        if rec1[3] <= rec2[1] and rec1[3] <= rec2[3]:
            return False

        return True
