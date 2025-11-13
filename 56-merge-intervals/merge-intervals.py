class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1️⃣: Sort the intervals based on their start time.
        # This ensures overlapping intervals come next to each other.
        # Example: [[5,7],[1,3],[2,4]] -> [[1,3],[2,4],[5,7]]
        intervals.sort(key=lambda i: i[0])

        # Step 2️⃣: Initialize the result list with the first interval.
        # We’ll compare all upcoming intervals with the last one inside 'res'.
        res = [intervals[0]]

        # Step 3️⃣: Iterate through all remaining intervals (starting from the 2nd one)
        for start, end in intervals[1:]:
            # Get the END value of the last merged interval in 'res'
            LastEnd = res[-1][1]

            # Case 1️⃣: Overlapping intervals
            # If the current interval's start is less than or equal to the last interval's end,
            # it means they overlap. Example: [1,3] and [2,6] -> they overlap.
            if start <= LastEnd:
                # Merge them by updating the end time of the last interval.
                # Take the maximum of both ends to cover the entire range.
                res[-1][1] = max(LastEnd, end)

            # Case 2️⃣: Non-overlapping intervals
            # If the current interval starts after the last one ends,
            # simply add it to the result list as a new interval.
            else:
                res.append([start, end])

        # Step 4️⃣: Return the merged list of intervals
        return res
