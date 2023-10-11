from bisect import bisect_left


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        count = {}
        for start, end in flowers:
            if start not in count:
                count[start] = 0

            if end + 1 not in count:
                count[end + 1] = 0

            count[start] += 1
            count[end + 1] -= 1

        prefixSumIndex = []
        prefixSumValue = []
        for k, v in sorted(list(count.items())):
            prefixSumIndex.append(k)

            if len(prefixSumIndex) == 0 or len(prefixSumValue) == 0:
                prefixSumValue.append(v)
            else:
                prefixSumValue.append(prefixSumValue[-1] + v)

        result = []
        for p in people:
            index = bisect_left(prefixSumIndex, p)

            if index >= len(prefixSumIndex):
                result.append(0)
                continue

            if prefixSumIndex[index] != p:
                index -= 1

            if index < 0:
                result.append(0)
                continue

            result.append(prefixSumValue[index])

        return result
