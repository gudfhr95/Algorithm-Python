class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    print(i, j, k)
                    result = max(result, self.getArea(points[i], points[j], points[k]))

        return result

    def getArea(self, a: List[int], b: List[int], c: List[int]):
        return abs((a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])) / 2
