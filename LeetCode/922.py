class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        result = []
        odd_index = 0
        even_index = 0
        while odd_index < len(odd) and even_index < len(even):
            result.append(even[even_index])
            result.append(odd[odd_index])

            odd_index += 1
            even_index += 1

        return result
