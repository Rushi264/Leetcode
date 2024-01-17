from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Use Counter to count occurrences of each element in arr
        occurrence_count = Counter(arr)

        # Initialize an empty set to track unique occurrence counts
        unique_counts = set()

        # Iterate over the values (occurrences) in occurrence_count
        for count in occurrence_count.values():
            # If the count is already in unique_counts, return False
            if count in unique_counts:
                return False
            # Add the count to the set of unique_counts
            unique_counts.add(count)

        # If all counts are unique, return True
        return True
