import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        if len(nums) == 0:
            return

        sorted_nums = sorted(nums, reverse=True)
        for num in sorted_nums:
            heapq.heappush(self.heap, num)
            if len(self.heap) == self.k:
                break

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)

        return self.heap[0]
