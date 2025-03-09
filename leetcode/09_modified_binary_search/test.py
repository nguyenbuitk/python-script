def is_sublist(lst, sublst):
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i+len(sublst)] == sublst:
            return True
    return False

nums1 = [1]
nums2 = [3, 4,2,1]

print(is_sublist(nums1, nums2))  # Output: True
