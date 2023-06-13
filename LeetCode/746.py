class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dist = [987654321 for i in range(len(cost) + 1)]
        dist[0] = 0
        dist[1] = 0

        result = 987654321
        for i, c in enumerate(cost):
            cur = dist[i]

            if (i + 2) >= len(cost):
                result = min(result, cur + cost[i])
            else:
                dist[i + 2] = min(dist[i + 2], cur + cost[i])

            if (i + 1) >= len(cost):
                result = min(result, cur + cost[i])
            else:
                dist[i + 1] = min(dist[i + 1], cur + cost[i])

        return result
