class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = {
            'A': 0,
            'B': 0
        }

        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                count[colors[i]] += 1

        if count['A'] > count['B']:
            return True
        else:
            return False
