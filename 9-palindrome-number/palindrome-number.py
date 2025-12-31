class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x
        reverse = 0

        while x > 0:
            digit = x % 10 #get last digit

            reverse = reverse * 10 + digit
            x //= 10 # remove last digit
        
        return original == reverse


        