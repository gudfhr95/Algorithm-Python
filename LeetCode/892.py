from collections import deque


class Solution:
    dx = [0, 1, 0, -1, 0, 0]
    dy = [-1, 0, 1, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    n = 0
    shape = []
    visited = []
    queue = deque()

    def surfaceArea(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.shape = [[[0 for _ in range(50)] for _ in range(self.n)] for _ in range(self.n)]

        for y in range(self.n):
            for x in range(self.n):
                for z in range(grid[y][x]):
                    self.shape[y][x][z] = 1

        self.visited = [[[False for _ in range(50)] for _ in range(self.n)] for _ in range(self.n)]

        result = 0
        for y in range(self.n):
            for x in range(self.n):
                for z in range(grid[y][x]):
                    if self.visited[y][x][z]:
                        continue

                    result += self.bfs(x, y, z)

        return result

    def bfs(self, x: int, y: int, z: int) -> int:
        result = 0

        self.queue.append((x, y, z))
        self.visited[y][x][z] = True

        while len(self.queue) > 0:
            cur = self.queue.pop()

            for k in range(6):
                xn = cur[0] + self.dx[k]
                yn = cur[1] + self.dy[k]
                zn = cur[2] + self.dz[k]

                if xn < 0 or yn < 0 or zn < 0 or xn >= self.n or yn >= self.n or zn >= 50:
                    result += 1
                    continue

                if self.shape[yn][xn][zn] == 0:
                    result += 1
                    continue

                if self.visited[yn][xn][zn]:
                    continue

                self.queue.append((xn, yn, zn))
                self.visited[yn][xn][zn] = True

        return result
