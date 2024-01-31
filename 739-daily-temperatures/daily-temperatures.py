from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result array with 0's since some days might not have a warmer temperature.
        res = [0] * len(temperatures)
        # Stack to keep indices of temperatures
        stack = []

        for i, temp in enumerate(temperatures):
            # Pop until the current temperature is not warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index  # Calculate the difference in days
            stack.append(i)

        return res
