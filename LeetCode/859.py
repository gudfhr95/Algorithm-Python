class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(s):
            return True

        char = []
        for i, c in enumerate(s):
            if goal[i] != c:
                char.append((c, goal[i]))

        print(char)

        return len(char) == 2 and char[0][0] == char[1][1] and char[0][1] == char[1][0]
