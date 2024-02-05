class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(int)

        for i in s:
            hashmap[i] += 1 

        for i ,val in enumerate(s):
            if hashmap[val] == 1:
                return i

        return -1

        