class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        # dp0 = ways up to i-2, dp1 = ways up to i-1
        dp0, dp1 = 1, 1

        for i in range(1, len(s)):
            curr = 0

            # single digit
            if s[i] != '0':
                curr += dp1

            # two digits
            two = int(s[i-1:i+1])
            if 10 <= two <= 26:
                curr += dp0

            if curr == 0:  # early fail (e.g., "30", "06")
                return 0

            dp0, dp1 = dp1, curr

        return dp1
    #this is quite tricky question come to this question often for deep understading