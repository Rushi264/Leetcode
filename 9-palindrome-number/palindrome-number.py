class Solution:
    def isPalindrome(self, x: int) -> bool:
        numberStr = str(x)
        l, r = 0, len(numberStr) - 1
        while l<=r:
            if numberStr[l] == numberStr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


        