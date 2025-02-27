class Solution:
    def generateMatrix(self, n):
        res = [[0]*n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1,0)]
        row, col = 0, 0
        visited = {(row, col)}
        res[row][col] = 1
        current_val = 1
        
        while len(visited) < n*n:
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                while 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    current_val += 1
                    visited.add((new_row, new_col))
                    print(new_row, new_col)
                    res[new_row][new_col] = current_val
                    new_row += dr
                    new_col += dc
                row, col = new_row - dr, new_col - dc
        return res
        

solution = Solution()
print(solution.generateMatrix(3))
        