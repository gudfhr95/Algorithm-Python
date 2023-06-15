class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for _ in range(len(nums2))]

        for i, n1 in enumerate(nums1):
            for j, n2 in enumerate(nums2):
                if n1 == n2:
                    result[i] = j

        return result
