class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = [0 for _ in range(26)]

        for c in licensePlate:
            if (c.isalpha()):
                count[ord(c.lower()) - ord('a')] += 1

        result = " " * 1001
        for word in words:
            if self.isSatisfying(word, count.copy()) and len(word) < len(result):
                result = word

        return result

    def isSatisfying(self, word: str, count: List[int]) -> bool:
        for c in word:
            count[ord(c.lower()) - ord('a')] -= 1

        for c in count:
            if c > 0:
                return False

        return True
