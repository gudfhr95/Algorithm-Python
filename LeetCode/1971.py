class Solution:
    parent = []

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.parent = [i for i in range(n)]

        for u, v in edges:
            self.union(u, v)

        return self.find(source) == self.find(destination)

    def find(self, x):
        if self.parent[x] == x:
            return x

        return self.find(self.parent[x])

    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)

        if xParent < yParent:
            self.parent[yParent] = xParent
        else:
            self.parent[xParent] = yParent
