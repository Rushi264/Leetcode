class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count = {}

        # Count characters in s and decrement counts based on t
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1

        # Calculate the total number of excess characters in s
        count = sum(value for value in char_count.values() if value > 0)

        return count
