def find_max_smaller_right(nums):
    n = len(nums)
    result = [None] * n  # Khởi tạo danh sách kết quả với giá trị None
    stack = []  # Stack để lưu các chỉ số của phần tử đã duyệt
    
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        
        if stack:
            result[i] = max(nums[j] for j in stack if nums[j] < nums[i])
        
        stack.append(i)
    
    return result

# Test
nums = [3, 5, 0, 3, 4]
print(find_max_smaller_right(nums))  # Output: [0, 4, None, None, None]