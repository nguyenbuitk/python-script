from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        listJump = [set() for _ in range(len(stones))]
        listJump[0].add(1)
        for n in range(1, len(stones)):
            for i in range(n):
                distance = stones[n] - stones[i]
                if distance in listJump[i]:
                    listJump[n].update([distance-1, distance, distance+1])
        if not listJump[len(stones) - 1]:
            return False
        return True
        

solution = Solution()
solution.canCross([0,1,3,5,6])

        