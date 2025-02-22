class Solution:
    def containsNearbyDuplicate(self, nums, k):
        num_map = {}  # Dictionary để lưu index của các phần tử đã gặp

        for i, num in enumerate(nums):
            if num in num_map:
                return True  # Tìm thấy phần tử trùng trong phạm vi k
            
            num_map[num] = i  # Cập nhật index của phần tử hiện tại
            
            if i >= k:  # Xóa phần tử ngoài phạm vi k
                num_map.pop(nums[i - k])

        return False
 
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
            
            
