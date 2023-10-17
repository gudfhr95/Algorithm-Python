from collections import deque


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        degree = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                degree[leftChild[i]] += 1
            if rightChild[i] != -1:
                degree[rightChild[i]] += 1

        start = 0
        for i in range(n):
            if degree[i] == 0:
                start = i
                break

        q = deque()
        visited = [False] * n

        q.append(start)
        visited[start] = True

        while len(q) > 0:
            cur = q.popleft()

            if leftChild[cur] != -1:
                if visited[leftChild[cur]]:
                    return False

                q.append(leftChild[cur])
                visited[leftChild[cur]] = True

            if rightChild[cur] != -1:
                if visited[rightChild[cur]]:
                    return False

                q.append(rightChild[cur])
                visited[rightChild[cur]] = True

        for v in visited:
            if not v:
                return False

        return True
