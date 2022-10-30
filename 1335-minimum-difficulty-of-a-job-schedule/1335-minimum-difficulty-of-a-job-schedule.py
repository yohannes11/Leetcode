import functools
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        numjobs = len(jobDifficulty)
        if numjobs < d:
            return -1
        @functools.lru_cache(None)
        def dp(day, cut):
            if day ==1:
                return max(jobDifficulty[cut:])
            
            maxsofar = 0
            answer = float('inf')
            for j in range(cut,numjobs- day +1):
                maxsofar = max(maxsofar,jobDifficulty[j])
                answer = min(answer, maxsofar+dp(day-1,j+1))
            return answer
        
        return dp(d,0)
            