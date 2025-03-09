from typing import List

def find132pattern(nums: List[int]) -> bool:
    # closest smaller in left:
    # smaller and smallest in left
    # Tạo danh sách index
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
    leftClosestSmaller = [None]*len(nums)
    stack = []
    for i in range(len(nums)):
        print(f"i: {i}, Stack before pop: {stack}")
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        if stack:
            leftClosestSmaller[i] = stack[0]
        stack.append(nums[i])
        print(f"Stack after append: {stack}")
    print(f"leftClosestSmaller: {leftClosestSmaller}")
    
    # biggest number in list right smaller
    rightClosestSmaller = [None]*len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        print(f"i= {i}, Stack before pop: {stack}")
        while stack and stack[-1] >= nums[i]:
            stack.pop()
        if stack:
            rightClosestSmaller[i] = stack[-1]
        stack.append(nums[i])
        print(f"Stack after append: {stack}")
    print(f"rightClosestSmaller: {rightClosestSmaller}")
    for i in range(len(nums)):
        if rightClosestSmaller[i] != None and leftClosestSmaller[i] != None and leftClosestSmaller[i] < rightClosestSmaller[i]:
            return True
    return False
print(find132pattern([1,3,5,0,3,4]))