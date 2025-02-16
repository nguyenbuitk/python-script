# breadth-first search
# tìm kiếm theo chiều rộng
from collections import deque

class Solution:
    def validPath(self, n: int, edges, source: int, destiation: int) -> bool:
        if source == destiation: 
            return True

        graph = {}
        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        
        def dfs(node):
            if node == destiation:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(source)

solution = Solution()
print(solution.validPath(3, [[0,1],[1,2],[2,0]], 0,2))
            