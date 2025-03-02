# Time complexity: O(mlogm + nlogn)
class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        p1 = len(nums1) - 1
        p2 = len(nums2) - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                p2 -= 1
            else:
                res.append(nums1[p1])
                p1 -= 1
                p2 -= 1
             
        return res

solution = Solution()
solution.intersect([1,2,2,1], [2,2])