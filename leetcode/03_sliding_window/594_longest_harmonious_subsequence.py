import collections
class Solution:
    def findLHS(self, nums):
        count = collections.Counter(nums)
        print(count)
        ans = 0
        for x in count:
            if x+1 in count:
                ans = max(ans, count[x] + count[x+1])
        return ans
solution = Solution()
print(solution.findLHS([1,2,3,4]))