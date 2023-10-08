class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        MIN = -(1000 * 1000 * 500)
        d = [[MIN for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]

        result = MIN
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                m = nums1[i - 1] * nums2[j - 1]
                d[i][j] = max(d[i][j], m, d[i - 1][j - 1] + m, d[i - 1][j], d[i][j - 1])
                result = max(result, d[i][j])

        return result
