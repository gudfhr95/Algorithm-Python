class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0

            count[num] += 1

        result = []
        for k, v in count.items():
            if v > len(nums) // 3:
                result.append(k)

        return result
