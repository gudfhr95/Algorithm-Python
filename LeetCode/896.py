class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        is_increasing = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                is_increasing = True
                break
            elif nums[i] > nums[i + 1]:
                is_increasing = False
                break

        for i in range(1, len(nums)):
            if is_increasing:
                if nums[i - 1] > nums[i]:
                    return False
            else:
                if nums[i - 1] < nums[i]:
                    return False

        return True
