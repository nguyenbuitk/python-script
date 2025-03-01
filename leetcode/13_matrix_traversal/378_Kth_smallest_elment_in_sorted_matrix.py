from typing import List
from collections import deque

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    dq = deque([])
    n = len(matrix)
    dq.append((0,0))
    kTh = 0
    visited = {(0,0)}
    while dq:
        i, j = dq.popleft()

        kTh += 1
        if kTh == k:
            return matrix[i][j]
        pos_left = i + 1
        pos_right = j + 1
        if 0 <= pos_left < n and (pos_left, j) not in visited:
            print("")
            index = 0
            while index < len(dq) and matrix[dq[index][0]][dq[index][1]] < matrix[pos_left][j]:
                index +=1
            dq.insert(index, (pos_left, j))
            visited.add((pos_left, j))

        
        if 0 <= pos_right < n and (i, pos_right) not in visited:
            index = 0
            while index < len(dq) and matrix[dq[index][0]][dq[index][1]] < matrix[i][pos_right]:
                index += 1
            dq.insert(index, (i, pos_right))
            visited.add((i, pos_right))
    return False
        
"""
[1,2,3,7],
[5,10,14,16]
[8,10,18,19]
[9,12,22,24]
"""
kthSmallest([[1,2,3,7],[5,10,14,16],[8,10,18,19],[9,12,22,24]],14)
