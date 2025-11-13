class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            #check if newInterval -> 5 is less than intervals -> 1 if yes then no intersection
            #just append it to res and return the result by appending the reamining intervals.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            #if newintervals -> 2 is greater than intervals -> 5 If yes then then add that 
            # old interval to res and continue.
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
            #if the intervals are colliding then take the minimum for start interval from
            #both of them and maximum from end interval from both of them which is merge them>
            #and dont just add it to the res, since it migh collide with the next interval.
        res.append(newInterval)
        #if the above else condition is for the last interval and we are out of for loop, 
        #then we need to add our new interval at the end of the res array and then return the
        #result.
        return res