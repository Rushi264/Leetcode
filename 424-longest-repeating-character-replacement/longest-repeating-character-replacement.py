class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFreq = 0
        res = 0

        for r, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            maxFreq = max(maxFreq, count[ch])

            # If we need more than k replacements, shrink window
            while (r - l + 1) - maxFreq > k:
                left_char = s[l]
                count[left_char] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
                


        