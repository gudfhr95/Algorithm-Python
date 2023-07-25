class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = [0]

        # right는 I(단조 증가), left는 D(단조 감소) 하는 값을 저장
        left = right = 0
        for c in s:
            if c == 'I':
                right += 1
                result.append(right)
            else:
                left -= 1
                result.append(left)
        # 그래프를 최소 값만큼 평행 이동
        return [e - left for e in result]
