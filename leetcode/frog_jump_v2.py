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
        setJump = {}
        for stone in stones:
            setJump[stone] = set()
        print(setJump)
        setJump[0].add(1)
        for n, stone in enumerate(stones):
            print("n = ", n)
           
            for jump in setJump[stone]:
                print("jump = ", jump)
                new_postition = stone + jump
                if new_postition in stones:
                    if jump > 1:
                        setJump[new_postition].add(jump-1)
                    setJump[new_postition].update([jump, jump+1])
            print(setJump)
        if not setJump[stones[len(stones)-1]]:
            return False
        return True
        
solution = Solution()
print(solution.canCross([0,1,3,5,6]))
print(solution.canCross([0,1,3,5,6,8,12,17]))

## 1450ms run time
