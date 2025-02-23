def removeKdigits( nums, k):
    # Edge case
    if len(nums) == k:
        return "0"
    
    len_stack = len(nums) - k
    n = len(nums)
    stack = []
    for i in range(len(nums)):
        # Remove all element from the stack if they larger than current
        # and make sure the len of the rest nums can fill the stack to len_stack
        while stack and stack[-1] > nums[i] and len(stack) + (n-i-1) >=  len_stack:
            stack.pop()
        
        # append if stack is not fill    
        if len(stack) < len_stack:
            stack.append(nums[i])
    
    # remove leading zero
    output = "".join(stack).lstrip('0')
    
    return output if output else "0"
print(removeKdigits("112",1))