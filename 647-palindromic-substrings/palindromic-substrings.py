class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        # helper to expand around center
        def expand(l, r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd-length palindromes (center at i)
            expand(i, i)
            # even-length palindromes (center between i and i+1)
            expand(i, i + 1)

        return count
    
    #this is quite simple version of Palindromic Substrings we used same logic but this time weed need total number of
    # palidrome exist in the string. so there are two cases 1st is for odd length palindrome and 2nd is for even 
    # and we created a helper function to write our main lgoic which constists of if its palindrome or not and if it
    # is then just increment our count.
