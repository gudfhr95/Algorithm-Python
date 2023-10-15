class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        maxDist = min(steps + 1, arrLen)
        d = [[0 for _ in range(maxDist)] for _ in range(steps + 1)]
        d[0][0] = 1

        for s in range(1, steps + 1):
            for i in range(maxDist):
                d[s][i] += d[s - 1][i]
                if i - 1 >= 0:
                    d[s][i] += d[s - 1][i - 1]
                if i + 1 < maxDist:
                    d[s][i] += d[s - 1][i + 1]
                d[s][i] %= 1_000_000_007

        return d[steps][0]
