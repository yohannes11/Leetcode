class Solution(object):
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        memo = {}
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
                
            if i==j:
                return True
            else: 
                if s[i] == s[j]:
                    if i+1 == j:
                        return True
                    if (i+1,j-1) not in memo:
                        memo[(i+1,j-1)] = dp(i+1,j-1)
                    if memo[(i+1,j-1)] and s[i+1] == s[j-1]:
                        memo[(i,j)] = True
                    else:
                        memo[(i,j)] = False

                else:
                    memo[(i,j)] = False
                return memo[(i,j)]

        for i in range(len(s)):
            for j in range(i,len(s)):
                if(dp(i,j)):
                    count+=1
        return count
                
            
        
            

                
            
                
            