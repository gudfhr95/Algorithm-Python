class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)

        diff = (alice_total - bob_total) // 2

        alice_set = set(aliceSizes)
        bob_set = set(bobSizes)

        for e in alice_set:
            if e - diff in bob_set:
                return [e, e - diff]

        return [-1, -1]
