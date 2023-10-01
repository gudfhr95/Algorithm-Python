class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr.sort()

        for i in range(len(arr) - 2):
            if arr[i] - arr[i + 1] != arr[i + 1] - arr[i + 2]:
                return False

        return True
