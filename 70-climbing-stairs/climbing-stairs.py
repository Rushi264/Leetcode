class Solution:
    def climbStairs(self, n: int) -> int:
        
        one_step, two_step = 1, 1
    #we are treating it like a fibonacci series, here we are going with bottom-up approach in DP.
    #just watch the neetcode explaination for more details.
        for i in range(n - 1):
            temp = one_step # to store our value one in order to shift it(to store it in two)
            one_step = one_step + two_step
            two_step = temp
        
        return one_step