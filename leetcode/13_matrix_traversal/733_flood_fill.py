from typing import List

class Solution:
    def floodFill(self, images: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_val = images[sr][sc]
        rows = len(images)
        cols = len(images[0])
        stack = []
        visited = []
        stack.append([sr,sc])
        while stack:
            i, j = stack.pop()
            if images[i][j] == initial_val:
                images[i][j] = color
            if i - 1 >= 0 and images[i-1][j] == initial_val and [i-1,j] not in visited:
                stack.append([i-1,j])
            if i + 1 < rows and images[i+1][j] == initial_val and [i+1,j] not in visited:
                stack.append([i+1,j])
            if j - 1 >= 0 and images[i][j-1] == initial_val and [i,j-1] not in visited:
                stack.append([i,j-1])
            if j + 1 < cols and images[i][j+1] == initial_val and [i,j + 1] not in visited:
                stack.append([i,j+1])
            visited.append([i,j])
            
        return(images)

images = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
    ]
images2 =  [[0,0,0],[0,0,0]]
image3 = [
    [0, 0, 0],
    [0, 1, 1]
]
solution = Solution()
print(solution.floodFill(images, 1, 1,  2))
print(solution.floodFill(images2, 0,0,0))
print(solution.floodFill(image3, 1,1,2))