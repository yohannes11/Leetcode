class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == j:
                return 1
            if s[i] == s[j]:
                if i+1 == j:
                    memo[(i,j)] = 2
                else:
                    memo[(i,j)] = 2+dp(i+1,j-1)
            else:
                memo[(i,j)] = max(dp(i,j-1),dp(i+1,j))
            return memo[(i,j)]
        
        return dp(0,len(s)-1)