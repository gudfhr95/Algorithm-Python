import heapq


class RecentCounter:
    pq = []

    def __init__(self):
        self.pq = []

    def ping(self, t: int) -> int:
        while len(self.pq) > 0 and self.pq[0] < t - 3000:
            heapq.heappop(self.pq)

        heapq.heappush(self.pq, t)
        return len(self.pq)
