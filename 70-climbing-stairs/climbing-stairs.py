class Solution:
    def climbStairs(self, n: int) -> int:

        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array for dynamic programming
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2

        # Fill the array with the number of ways to climb to each step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
        