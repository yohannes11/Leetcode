class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
              
        for course, pre_request in prerequisites:
            graph[course].append(pre_request)
        
        def dfs(node, visiting):
            for nei in graph[node]:
                if nei in visiting:
                    return False
                visiting.add(nei)
                if dfs(nei,visiting) == False:
                    return False
            visiting.remove(node)
            graph[node] = []
            return True
        
        for current_node in graph:
            visiting = set()
            visiting.add(current_node)
            if dfs(current_node,visiting) == False:return False
        return True
                
                    
            
        
            
                
        
        
    
        