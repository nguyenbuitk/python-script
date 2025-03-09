from typing import List

def find132pattern(nums: List[int]) -> bool:
    stack = []
    second = float('-inf')
    # Tạo danh sách index
    indexes = list(range(len(nums)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in nums)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Nums:   {nums_str}")
    for i in range(len(nums) -1, -1, -1):
        print("")
        if nums[i] < second:
           print(f"132 pattern found! i: {nums[i]}, k: {second}, j: {stack[-1] if stack else 'N/A'}") 
           return True
        print(f"Stack before pop {stack}")
        while stack and stack[-1] < nums[i]:
            second = stack.pop()
            print(f"Updated second (nums[k]): {second}")
        
        stack.append(nums[i])
        print(f"nums[{i}] = {nums[i]}")
        print(f"Stack: {stack}, Second: {second}")
    
    print("No 132 pattern found")
    return False
print(find132pattern([3,7,5,0,3,4]))