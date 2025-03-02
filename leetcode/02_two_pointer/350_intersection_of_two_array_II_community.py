# Time complexity: O(m+n)
# Using HasMap to store occurences of elements in the nums1 array
# Iterate x in nums2 array, check if cnt[x] > 0 then append x to our answer and decrease cnt[x] by 1
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        cnt = {}
        res = []
        for num in nums1:
            if num in cnt:
                cnt[num] += 1
            else: cnt[num] = 1
        
        for num in nums2:
            if num in cnt and cnt[num] > 0:
                cnt[num] -= 1
                res.append(num)
        return res