class Solution(object):
    '''
    1,2,3,4,5
    
    
    '''
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        memo[0] , memo[1] = 1, 1
        def dp(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = dp(i-2)+ dp(i-1)
                return memo[i]
        return dp(n)
        