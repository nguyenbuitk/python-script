class Solution:
    def sortedArray(self, nums):
        n = len(nums)
        print(nums)
        RightGreaterThan = [n]*len(nums)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                stack.pop()
            if stack:
                RightGreaterThan[i] = stack[-1]
            stack.append(i)

        print(RightGreaterThan)
        LeftLessThan = [-1]*len(nums)
        stack =[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            if stack:
                LeftLessThan[i] = stack[-1]
            stack.append(i)
        print(LeftLessThan)


solution = Solution()
solution.sortedArray([6,6,7])
solution.sortedArray([2, 6, 4, 10, 18, 9, 15, 17, 20, 21])
