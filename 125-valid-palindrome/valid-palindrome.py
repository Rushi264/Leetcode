class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalstr = ""

        for char in s:
            if char.isalnum():
                finalstr += char.lower()
                
        start, end  = 0, (len(finalstr) - 1)
        while start <= end:
            if finalstr[start] == finalstr[end]:
                start += 1
                end -= 1
            else:
                return False
        return True


        