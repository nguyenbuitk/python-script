from typing import List

def find132pattern(nums: List[int]) -> bool:
    # Step 1: Find the smallest element to the left for each element
    leftSmallest = [None]*len(nums)
    stack = []
    for i in range(len(nums)):
        print(f"i: {i}, Stack before pop: {stack}")
        
        # Maintain a monotonically increasing stack
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        
        # Store the smallest element to the left
        if stack:
            leftSmallest[i] = stack[0]
            
        # Push current element onto the stack
        stack.append(nums[i])
        print(f"Stack after append: {stack}")
    print(f"leftSmallest: {leftSmallest}")
    # Step 2: Find the largest element in list right smaller
    # biggest number in those right smaller
    # with example [1,3,5,0,3,4]
    # if 3 is 132 pattern => 5 is 132 pattern => just examine 5
    rightSmaller = [None]*len(nums)
    stack = []
    second = None
    for i in range(len(nums) - 1, -1, -1):
        print(f"i= {i}, Stack before pop: {stack}")
        while stack and stack[-1] < nums[i]:
            second = stack.pop()
        if second:
            rightSmaller[i] = second
            second = None
        stack.append(nums[i])
        print(f"Stack after append: {stack}")
    print(f"rightSmaller: {rightSmaller}")
    
    # Step 3: Check if there exists an index i where left < right, forming a 132 pattern
    for i in range(len(nums)):
        if rightSmaller[i] != None and leftSmallest[i] != None and leftSmallest[i] < rightSmaller[i]:
            return True
    return False
print(find132pattern([1,3,5,0,3,4]))