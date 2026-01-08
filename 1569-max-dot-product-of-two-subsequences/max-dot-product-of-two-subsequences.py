from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        NEG = -10**18

        # dp[j] will represent dp[i][j] for current i as we iterate i from n-1..0
        dp = [NEG] * (m + 1)

        for i in range(n - 1, -1, -1):
            new = [NEG] * (m + 1)
            a = nums1[i]
            for j in range(m - 1, -1, -1):
                prod = a * nums2[j]

                # take both i,j and optionally continue with dp[i+1][j+1]
                take = prod
                if dp[j + 1] > 0:
                    take += dp[j + 1]

                # skip nums1[i] (dp[i+1][j]) = dp[j]
                # skip nums2[j] (dp[i][j+1]) = new[j+1]
                new[j] = max(take, dp[j], new[j + 1])

            dp = new

        return dp[0]
