class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for y in image:
            y.reverse()

            for i, x in enumerate(y):
                y[i] = 1 - x

        return image
