import re
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
    
        ones_counts = [line.count('1') for line in bank if '1' in line]

        # Calculate the product of '1's count for each adjacent pair
        count = sum(a * b for a, b in zip(ones_counts, ones_counts[1:]))

        return count
          



