class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = [0]

        left = right = 0
        for c in s:
            if c == 'I':
                right += 1
                result.append(right)
            else:
                left -= 1
                result.append(left)

        return [e - left for e in result]
