class Solution(object):
    '''
    1,2,3,4,5
    
    
    '''
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, current = 1, 2
        if n <= 2: 
            return n
        else:
            for n in range(3, n+1):
                temp = prev+current
                prev = current
                current = temp
        return current
            
            
        