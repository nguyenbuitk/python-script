class Solution:
    def findClosestElements(self, arr, k, x):
        res = []
        for i in range(len(arr)):
            if arr[i] > x:
                break
        
        l, r = i-1, i
        while k > 0:
            if l >= 0 and r <= len(arr) - 1:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
            elif l < 0:
                res.append(arr[r])
                r += 1
            elif r > len(arr) - 1:
                res.append(arr[l])
                l -= 1
            k -= 1
                            
        return sorted(res)
solution = Solution()
print(solution.findClosetElements([1,2,3,4,5], 4, 3))