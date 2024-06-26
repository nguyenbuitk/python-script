from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 0:
            return False
        
        stone_positions = {stone: set() for stone in stones}
        stone_positions[stones[0]].add(1)

        for stone in stones:
            print(f"{stone}======")
            print(stone_positions)
            for jump in stone_positions[stone]:
                next_position = stone + jump
                if next_position == stones[-1]:
                    return True
                if next_position in stone_positions:
                    if jump > 1:
                        stone_positions[next_position].add(jump - 1)
                    stone_positions[next_position].add(jump)
                    stone_positions[next_position].add(jump + 1)
        
        return False

solution = Solution()
print(solution.canCross([0, 1, 3, 5, 6, 8, 12, 17]))  # Output: True
print(solution.canCross([0, 1, 2, 3, 4, 8, 9, 11]))  # Output: False

## 120 ms run time