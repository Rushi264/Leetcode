class Solution:
    def closeStrings(self, str1: str, str2: str) -> bool:
        # Check if both strings contain the same characters
        if set(str1) != set(str2):
            return False

        # Check if the frequency of each character is the same in both strings
        char_freq_str1 = {char: str1.count(char) for char in set(str1)}
        char_freq_str2 = {char: str2.count(char) for char in set(str2)}

        # Comparing the frequency of each character in both strings
        return sorted(char_freq_str1.values()) == sorted(char_freq_str2.values())
