class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_val(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s) - 1 
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            
            else:
                # one deletion allowed: skip left OR skip right
                return is_val(l + 1,r) or is_val(l, r - 1)
        
        return True
            



        
        


        