class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        maxCost = 1_000_000 * len(cost)

        d = [[maxCost for _ in range(len(cost) + 1)] for _ in range(len(cost))]

        for i in range(len(cost)):
            d[i][0] = 0

        for i in range(len(cost)):
            for j in range(1, len(cost) + 1):
                if j - (time[i] + 1) < 0:
                    d[i][j] = min(d[i][j], d[i - 1][j], cost[i])
                else:
                    d[i][j] = min(d[i][j], d[i - 1][j], cost[i] + d[i - 1][j - (time[i] + 1)])

        return d[-1][-1]
