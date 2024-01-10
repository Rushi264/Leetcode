class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):

            last_interval = merged[-1]

            current_interval = intervals[i]

            if current_interval[0] <= last_interval[1]:
                merged[-1] = [last_interval[0], max(last_interval[1], current_interval[1])]
            else:
                merged.append(current_interval)

        return merged