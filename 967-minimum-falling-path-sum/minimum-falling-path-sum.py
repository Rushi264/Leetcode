class Solution(object):
    def minFallingPathSum(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a copy of the matrix to store the minimum falling path sums
        dp = [[0] * cols for _ in range(rows)]

        # Copy the first row of the matrix to the dp matrix
        for i in range(cols):
            dp[0][i] = matrix[0][i]

        # Iterate through the matrix starting from the second row
        for i in range(1, rows):
            for j in range(cols):
                # Calculate the minimum falling path sum for the current cell
                dp[i][j] = matrix[i][j] + min(
                    dp[i - 1][max(0, j - 1)],
                    dp[i - 1][j],
                    dp[i - 1][min(cols - 1, j + 1)]
                )

        # Return the minimum value in the last row of the dp matrix
        return min(dp[rows - 1])