class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        length = len(goal)
        goal += goal

        for i in range(length):
            substr = goal[i:i + length]

            if substr == s:
                return True

        return False
