class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        y_len = len(matrix)
        x_len = len(matrix[0])
        result = [[0 for _ in range(y_len)] for _ in range(x_len)]

        print(y_len, x_len)

        index = 0
        for x in range(x_len):
            for y in range(y_len):
                x_pos = index % y_len
                y_pos = index // y_len

                result[y_pos][x_pos] = matrix[y][x]

                index += 1

        return result
