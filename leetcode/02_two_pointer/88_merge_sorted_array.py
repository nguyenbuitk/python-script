class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:  
                nums1[p] = nums1[p1]
                nums1[p1] = 0
                p1 -= 1
            else:
                nums1[p] = nums2[p2]  
                nums2[p2] = 0
                p2 -= 1
                
            p -= 1

        # Nếu vẫn còn phần tử trong nums2 chưa được thêm vào nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

solution = Solution()
solution.merge([1, 2, 3, 0, 0, 0], 3, [2,5,6], 3)

