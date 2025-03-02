from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = [1] * len(nums)
        for i in range(1, len(nums)):
            subproblems = []
            for k in range(i):
                if nums[k] < nums[i]:
                    subproblems.append(L[k])
            L[i] = 1 + max(subproblems, default=0)
        return max(L)
            
    
def test_result():
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    expected_output = 4
    assert solution.lengthOfLIS(nums) == expected_output, f"Test failed for input {nums}"
    
    nums = [0, 1, 0, 3, 2, 3]
    expected_output = 4
    assert solution.lengthOfLIS(nums) == expected_output, f"Test failed for input {nums}"
    
    nums = [7, 7, 7, 7, 7, 7, 7]
    expected_output = 1
    assert solution.lengthOfLIS(nums) == expected_output, f"Test failed for input {nums}"
    
    print("All test cases passed!")

if __name__ == "__main__":

    test_result()