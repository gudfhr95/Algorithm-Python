class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = 0

        while index < len(letters) and letters[index][0] <= target[0]:
            index += 1

        return letters[index % len(letters)