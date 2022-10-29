class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        numjobs = len(jobDifficulty)
        memo = {}
        if numjobs < d:
            return -1
        def dp(day, cut):
            if ((day,cut) in memo):
                return memo[(day,cut)]
            if day == 1:
                return max(jobDifficulty[cut:])
            
            maxsofar = 0
            answer = float('inf')
            for j in range(cut, numjobs -day +1):
                maxsofar = max(jobDifficulty[cut:j+1])
                answer = min(answer, maxsofar+dp(day-1,j+1))
            memo[(day,cut)] = answer
            return answer
        return dp(d,0)
                
            
                
                