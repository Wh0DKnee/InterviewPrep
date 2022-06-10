from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        row_size = len(matrix[0])
        while right >= left:
            middle = left + ((right - left) // 2)
            r, c = self.indexToIndices(middle, row_size)
            if matrix[r][c] == target:
                return True
            if target > matrix[r][c]:
                left = middle + 1
            else:
                right = middle - 1
        return False

    def indexToIndices(self, i, row_size):
        row = i // row_size
        col = i % row_size
        return row, col
