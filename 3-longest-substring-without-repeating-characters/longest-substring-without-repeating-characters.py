class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store characters in the current sliding window
        charSet = set()
        
        # Left pointer of the sliding window
        l = 0
        
        # Stores the maximum length found so far
        res = 0

        # Right pointer moves through the string
        for r in range(len(s)):
            
            # If current character is already in the set,
            # shrink the window from the left until the duplicate is removed
            while s[r] in charSet:
                charSet.remove(s[l])  # remove leftmost character
                l += 1               # move left pointer forward
            
            # Add the current character to the set
            charSet.add(s[r])
            
            # Update the maximum length of substring without repeating characters
            res = max(res, r - l + 1)
        
        # Return the maximum length found
        return res
