from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rs, cs = set(), set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rs.add(r)
                    cs.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rs or c in cs:
                    matrix[r][c] = 0
