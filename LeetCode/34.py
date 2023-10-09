from bisect import bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left = bisect_right(nums, target - 1)
        right = bisect_right(nums, target) - 1

        if left == -1 or left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, right]
