class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        p3 = -9876543210
        for num in nums[::-1]:
            if p3 > num:
                return True

            while len(stack) > 0 and stack[-1] < num:
                p3 = stack.pop()

            stack.append(num)

        return False
