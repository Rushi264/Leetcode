class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # first for loop is for column and 2 for loop is for rows.

        for i in range(len(text1) - 1, -1, -1):
        #we are iterating thorugh rows in reverse order since it bottom up approach
            for j in range(len(text2) - 1, -1, -1):
            #we are iterating thorugh columns in reverse order since it bottom up approach
                if text1[i] == text2[j]:
                    #if 2 values matches then we just add 1 in the bottom diagonal grid and
                    #store it in our current value
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
                     #if 2 values doesn't matches then we will take the maximum of 
                     # right grid and the bottom grid and store it in current grid.
        return dp[0][0]
        