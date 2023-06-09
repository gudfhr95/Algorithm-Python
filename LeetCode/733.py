from collections import deque


class Solution:
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        value = image[sr][sc]

        q = deque()
        visited = [[False for i in range(len(image[0]))] for i in range(len(image))]

        image[sr][sc] = color
        q.append((sc, sr))
        visited[sr][sc] = True

        while len(q) > 0:
            x, y = q.popleft()

            for k in range(4):
                xn = x + self.dx[k]
                yn = y + self.dy[k]

                if xn < 0 or xn >= len(image[0]) or yn < 0 or yn >= len(image):
                    continue

                if visited[yn][xn]:
                    continue

                if image[yn][xn] != value:
                    continue

                image[yn][xn] = color
                q.append((xn, yn))
                visited[yn][xn] = True

        return image
