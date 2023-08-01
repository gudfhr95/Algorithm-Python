class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # count 배열 선언
        count = [0 for _ in range(10001)]

        # count
        for num in nums:
            count[num] += 1

        # n번 반복된 것을 찾는다
        for i, c in enumerate(count):
            if c == len(nums) / 2:
                return i

        return -1
