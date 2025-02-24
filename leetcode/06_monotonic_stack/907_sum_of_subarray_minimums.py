class Solution:
    def sumSubarrayMins(self, arr):
        res = 0
        MOD = 10**9 + 7
        RLT = [len(arr)] * len(arr)
        LLT = [-1] * len(arr)
        stack = []
        for i in range(len(arr) -1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                RLT[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                LLT[i] = stack[-1]
            stack.append(i)

        for i in range(len(arr)):
            countLeft = i - LLT[i]
            countRight = RLT[i] - i
            res = res + countLeft*countRight*arr[i] % MOD
        
        return res%MOD
    
solution = Solution()
print(solution.sumSubarrayMins([7,5,8,5]))
