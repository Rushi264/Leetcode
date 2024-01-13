class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        hashmap1, hashmap2 = {}, {}

        # Counting characters in s
        for char in s:
            if char in hashmap1:
                hashmap1[char] += 1
            else:
                hashmap1[char] = 1

        # Counting characters in t
        for char in t:
            if char in hashmap2:
                hashmap2[char] += 1
            else:
                hashmap2[char] = 1

        for char in hashmap1:
            if hashmap1[char] > hashmap2.get(char, 0):
                count += hashmap1[char] - hashmap2.get(char, 0)

        return count
