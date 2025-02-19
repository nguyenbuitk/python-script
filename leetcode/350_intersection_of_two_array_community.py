# Time complexity: O(n)
class Solution:
    def intersection(self, nums1, nums2):
        res = []
        if len(nums1) > len(nums2):
            return self.intersection(nums2,nums1)
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)
        return res