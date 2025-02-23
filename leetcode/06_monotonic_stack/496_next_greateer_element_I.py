def nextGreaterElement(nums1, nums2):
    # nums3 stores the next greater element for each number in nums2
    nums3 = [-1]*len(nums2)
    
    res = [-1]*len(nums1)
    
    # dict store the index of each number in nums2 for quick look
    dict = {}
    stack = []
    
    # Iterate nums2 from right to left to determine the next greater element
    for i in range(len(nums2) - 1, -1, -1):
        dict[nums2[i]] = i
        
        # Pop smaller elements from the stack since they cannot be the next greater element
        while stack and stack[-1] < nums2[i]:
            stack.pop()
            
        # If stack is not empty, the top of the stack is the next greater element of nums2[i]
        if stack:
            nums3[i] = stack[-1]
        stack.append(nums2[i])
        
    # Iterate through nums1 and retrieve the next greater element from nums3
    for i in range(len(nums1)):
        res[i] = nums3[dict[nums1[i]]]
    return res

print(nextGreaterElement([4,1,2], [1,3,4,2]))