'''
When we want to map each stone position to the possible jump distances that can reach it, using a list directly isn't suitable because list indices must be continuous integers starting from 0. 
However, stone positions might not follow this pattern, so we use a dictionary (also known as a hashmap) in Python.
Suppose we have the stone positions: stones = [0, 1, 3, 5, 6].


E.g. withs stones = [0,1,3,5,6]
    listJump[0] = set()
    listJump[1] = set()
    listJump[3] = set()
    listJump[5] = set()
    listJump[6] = set()

=> list in python can't do that, we must use dictionary (aka hashmap) in python
Using a list in Python, we can only create mappings for continuous indices:
    listJump[0] = set()
    listJump[1] = set()
    listJump[2] = set()
    listJump[3] = set()
    listJump[4] = set()
'''
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_positions = {stone: set() for stone in stones}
        stone_positions[0].add(1)
        for stone in stones:
            for jump in stone_positions[stone]:
                next_position = stone + jump
                if next_position == stones[-1]:
                    return True
                
                # if next_position in stones:           # complexity O(n)
                if next_position in stone_positions:    # complexity O(1) 
                    if jump > 1:
                        stone_positions[next_position].add(jump-1)
                    stone_positions[next_position].update([jump, jump+1])
        return False
        
solution = Solution()
print(solution.canCross([0,1,3,5,6]))
print(solution.canCross([0,1,3,5,6,8,12,17]))

## 1450ms run time
