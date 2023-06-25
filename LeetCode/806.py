class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        curPixel = 0
        curLen = 1
        curWidth = 0
        for c in s:
            curWidth = widths[ord(c) - ord('a')]
            curPixel += curWidth

            if curPixel > 100:
                curPixel = curWidth
                curLen += 1

        if curPixel > 100:
            curPixel %= curWidth
            curLen += 1

        return [curLen, curPixel]
