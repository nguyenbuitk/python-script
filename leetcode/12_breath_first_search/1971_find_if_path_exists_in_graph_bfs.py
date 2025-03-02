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
        dq = deque([source])
        
        while dq:
            temp = dq.popleft()
            visited.add(temp)
            if destiation == temp:
                return True
            
            for vert in graph[temp]:
                if vert not in visited:
                    dq.append(vert)
            
        return False

solution = Solution()
print(solution.validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5,9))
            