class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        if s is None:
            return False
        slow = 0
        fast = 0
        while fast < len(s):
            slow += 1
            fast += 2
        
        x = s[:slow]
        y = s[slow:]
        print (x,y)

        count1, count2 = 0, 0
        for val in x:
            if val in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                count1 += 1
        for val in y:
            if val in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                count2 += 1
        
        return count1 == count2




        