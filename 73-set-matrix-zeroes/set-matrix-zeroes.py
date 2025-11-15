from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        rows, cols = len(matrix), len(matrix[0])

        # 1) Find all cells that are 0 and store their positions
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    temp.append((i, j))

        # 2) For each zero position, set its entire row and column to 0
        for i, j in temp:
            # set entire row i to 0
            for c in range(cols):
                matrix[i][c] = 0

            # set entire column j to 0
            for r in range(rows):
                matrix[r][j] = 0
