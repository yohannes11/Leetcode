class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        pac_res, atl_res = set(), set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for i in range(row):
            pacific.add((i,0))
            atlantic.add((i,col-1))
            
        for i in range(col):
            pacific.add((0,i))
            atlantic.add((row-1, i))
            
        def dfs(i,j, visited):
            if (i >=0 and i < row) and (j >=0 and j < col):
                if (i,j) not in visited:
                    visited.add((i,j))
                for direction in directions:
                    new_r = i+direction[0]
                    new_c = j+direction[1]
                    if (new_r >=0 and new_r < row) and (new_c >=0 and new_c < col):
                        if heights[new_r][new_c] >= heights[i][j] and (new_r,new_c) not in visited:
                                dfs(new_r,new_c,visited)
                            
        for r, c in pacific:
            dfs(r,c,pac_res)
        
        for r, c in atlantic:
            dfs(r,c,atl_res)
        
        return pac_res & atl_res
                            
        
        
        
        
        
        