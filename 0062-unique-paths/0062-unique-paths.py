class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        
        1 1 1 1
        1 2 3 4
        1 3 6 10
        
        """
        grid =[[0]*n for _ in range(m)]
        print(grid)
        for i in range(n):
            grid[0][i] = 1
        for i in range(m):
            grid[i][0] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]
        