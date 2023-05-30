class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = dict()

        for i, num in enumerate(nums):
            if num not in degree:
                degree[num] = list()

            degree[num].append(i)

        degree = sorted(degree.items(), key=lambda item: len(item[1]), reverse=True)

        max_degree = len(degree[0][1])

        result = 987654321
        for key, value in degree:
            if len(value) != max_degree:
                break

            result = min(result, value[-1] - value[0] + 1)

        return result
