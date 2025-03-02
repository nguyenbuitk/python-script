
class Solution:
    def validPath(self, n: int, edges, source: int, destiation: int) -> bool:
        if source == destiation: return True

        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])

        visited = set()
        stack = [source]
          
        while stack:
            temp = stack.pop()
            visited.add(temp)
            if destiation == temp:
                return True
            for vert in graph[temp]:
                if vert not in visited:
                    stack.append(vert)
            
        return False

solution = Solution()
print(solution.validPath(3, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5,9))
            