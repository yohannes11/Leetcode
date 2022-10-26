class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = {}
        
        
        def dfs(num):
            if  tuple(num) in memo:
                return memo[tuple(num)]
            n = len(num)    
            res = 0
            for i in range(n-1):
                for j in range(i+1,n):
                    num2 = num.copy()
                    num2.remove(num[i])
                    num2.remove(num[j])
                    temp = (n//2)*math.gcd(num[i],num[j])+dfs(num2)    
                    res = max(res,temp)
            memo[tuple(num)] = res
            return res
        return dfs(nums)

            