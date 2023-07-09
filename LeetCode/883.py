class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        w = len(grid[0])
        h = len(grid)

        result = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    continue

                result += 1

        for y in range(h):
            m = 0
            for x in range(w):
                m = max(m, grid[y][x])

            result += m

        for x in range(w):
            m = 0
            for y in range(h):
                m = max(m, grid[y][x])

            result += m

        return result
