class Solution:
    def sortedArray(self, nums):
        n = len(nums)
        
        RightGreaterThan = [n]*len(nums)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            if stack:
                RightGreaterThan[i] = stack[-1]
            stack.append(i)
        
        LeftLessThan = [-1]*len(nums)
        stack =[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                LeftLessThan[i] = stack[-1]
            stack.append(i)
        
        start = float('inf')
        end = float('-inf')
        
        for i in range(len(nums)):
            if LeftLessThan[i] != i - 1:
                start = min(start,  LeftLessThan[i]  + 1)
                end = max(end, i + 1)
        print("Right greater than ========")
        print('\t'.join(map(str, RightGreaterThan)))
        print('\t'.join(map(str, nums)))

        print('\t'.join(map(str, LeftLessThan)))
        print("Left less than =========")
        
        print("start, end = ", start, end)
        if start > end:
            return 0
        return end - start

solution = Solution()
print(solution.sortedArray([2, 6, 4, 10, 18, 9, 15, 19]))
print("=============================================")
print(solution.sortedArray([2, 3,4,5,6,7,8,9]))
print("=============================================")
print(solution.sortedArray([2,3,3,2,4]))