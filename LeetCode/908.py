import math


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        median = (max(nums) + min(nums)) / 2
        median_ceil = math.ceil(median)
        median_floor = math.floor(median)

        result = 0
        temp = []
        for i, num in enumerate(nums):
            if num > median_ceil:
                temp.append(max(median_ceil, num - k))
            elif num < median_ceil:
                temp.append(min(median_ceil, num + k))
            else:
                temp.append(num)

        result = max(temp) - min(temp)

        temp = []
        for i, num in enumerate(nums):
            if num > median_floor:
                temp.append(max(median_floor, num - k))
            elif num < median_floor:
                temp.append(min(median_floor, num + k))
            else:
                temp.append(num)

        result = min(result, max(temp) - min(temp))

        return result
