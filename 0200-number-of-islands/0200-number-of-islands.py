class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        count = 0
        
        def dfs(i,j):
            if i < 0 or i >= row:
                return
            if j < 0 or j >= col:
                return
            if (i,j) in visited:
                return
            if grid[i][j]!='1':
                return
            visited.add((i,j))       
            for direction in directions:
                    dfs(i+direction[0],j+direction[1])
            
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and grid[i][j] =='1':
                    count+=1
                    dfs(i,j)
        return count
        
        
                    
                    