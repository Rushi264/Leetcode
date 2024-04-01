class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip()
        count = 0 

        last = -1
        
        for w in  s[::last]:
            if w == " ":
                return count
            count += 1
            last -= 1 
        return len(s)
            