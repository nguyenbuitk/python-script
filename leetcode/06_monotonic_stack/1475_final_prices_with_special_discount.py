class Solution:
    # find the closest smaller element in the right
    def finalPrices(self, prices):
        res = [0] * len(prices)
        stack = []
        for i in range(len(prices)-1, -1, -1):
            # remove all larger element
            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            if stack: res[i] = prices[i] - stack[-1]
            else: res[i] = prices[i]
            if stack and stack[-1] == prices[i]:
                continue
            stack.append(prices[i])
        return res
        
solution = Solution()
print(solution.finalPrices([4,7,1,9,4,8,8,9,4]))