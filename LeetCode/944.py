class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0

        # x축을 기준으로 반복
        for x in range(len(strs[0])):
            cur = strs[0][x]  # 이전 값 저장
            is_sorted = True

            # y축을 기준으로 반복
            for y in range(1, len(strs)):
                # 만약 이전 값보다 작다면 sort 되지 않음
                if ord(cur) > ord(strs[y][x]):
                    is_sorted = False
                    break
                cur = strs[y][x]

            if not is_sorted:
                result += 1

        return result
