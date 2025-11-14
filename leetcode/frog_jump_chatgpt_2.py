## 100ms run time
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if not stones:
            return False

        # Dictionary to hold the positions of stones for quick access
        stone_positions = {stone: index for index, stone in enumerate(stones)}
        
        # Memoization dictionary to store results of subproblems
        memo = {}

        def can_reach(current_position, last_jump):
            if (current_position, last_jump) in memo:
                return memo[(current_position, last_jump)]

            # Base case: if the current position is the last stone
            if current_position == stones[-1]:
                return True

            for jump in (last_jump - 1, last_jump, last_jump + 1):
                if jump > 0 and (current_position + jump) in stone_positions:
                    if can_reach(current_position + jump, jump):
                        memo[(current_position, last_jump)] = True
                        return True

            memo[(current_position, last_jump)] = False
            return False

        # The first jump is always 1 unit
        return can_reach(stones[0], 0)