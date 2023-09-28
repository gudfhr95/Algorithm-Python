class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        forwardMap = {}
        backwardMap = {}
        sizeMap = {}

        result = -1
        for i, e in enumerate(arr):
            size = 1

            if (e - 1) in backwardMap:
                prevSize = (e - 1) - backwardMap[e - 1] + 1
                start = backwardMap[e - 1]
                end = e

                forwardMap[start] = end
                backwardMap[end] = start

                del backwardMap[e - 1]
                sizeMap[prevSize] -= 1

                size = end - start + 1
                if size not in sizeMap:
                    sizeMap[size] = 0
                sizeMap[size] += 1

            if (e + 1) in forwardMap:
                prevSize = forwardMap[e + 1] - (e + 1) + 1
                start = e
                end = forwardMap[e + 1]

                forwardMap[start] = end
                backwardMap[end] = start

                del forwardMap[e + 1]
                sizeMap[prevSize] -= 1

                size = end - start + 1
                if size not in sizeMap:
                    sizeMap[size] = 0
                sizeMap[size] += 1

            if e in forwardMap and e in backwardMap:
                prevSize1 = e - backwardMap[e] + 1
                prevSize2 = forwardMap[e] - e + 1
                start = backwardMap[e]
                end = forwardMap[e]

                forwardMap[start] = end
                backwardMap[end] = start

                del forwardMap[e]
                del backwardMap[e]
                sizeMap[prevSize1] -= 1
                sizeMap[prevSize2] -= 1

                size = end - start + 1
                if size not in sizeMap:
                    sizeMap[size] = 0
                sizeMap[size] += 1

            if size == 1:
                forwardMap[e] = e
                backwardMap[e] = e

                if size not in sizeMap:
                    sizeMap[size] = 0
                sizeMap[size] += 1

            if m in sizeMap and sizeMap[m] > 0:
                result = i + 1

        return result
