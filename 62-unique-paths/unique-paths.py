class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        # we will use this for our final result of columns stored in this array.

        for i in range(m - 1):
        # this is just to iterate through the columns for m number of rows.
            newRow = [1] * n
            # we are using this for storing our row values temperily in our newRow 
            # so that we can transfer to our main row array.
            for j in range(n - 2, -1, -1):
            #sinceits bottom to up approach we will iterate in reverse order.
                newRow[j] = newRow[j + 1] + row[j]
            #calculating the values by adding right and bottom values in the grid
            row = newRow
            # transfering it to actual row result array.
        return row[0]
        