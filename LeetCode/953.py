class Solution:
    order_dict = {}

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # order_dict를 만든다
        for i, c in enumerate(order):
            self.order_dict[c] = i

        # words를 순회하면서 words[i] < words[i+1]를 만족하는지 비교
        for i in range(len(words) - 1):
            if not self.isBigger(words[i], words[i + 1]):
                return False

        return True

    def isBigger(self, a: str, b: str) -> bool:
        if a == b:
            return True

        # order_dict를 고려하여 a와 b의 순서를 비교
        min_length = min(len(a), len(b))
        for i in range(min_length):
            if a[i] != b[i]:
                return self.order_dict[a[i]] < self.order_dict[b[i]]

        # character가 모두 같은 경우 len이 작은 것이 더 큰 것
        return len(a) < len(b)
