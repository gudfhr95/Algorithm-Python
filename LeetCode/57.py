import heapq


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pq = []
        for interval in intervals:
            heapq.heappush(pq, interval)
        heapq.heappush(pq, newInterval)

        result = []
        overlapped = heapq.heappop(pq)
        while len(pq) > 0:
            cur = heapq.heappop(pq)

            if overlapped[1] < cur[0] or cur[1] < overlapped[0]:
                result.append(overlapped)
                overlapped = cur
                continue

            overlapped[0] = min(overlapped[0], cur[0])
            overlapped[1] = max(overlapped[1], cur[1])
        result.append(overlapped)

        return result
