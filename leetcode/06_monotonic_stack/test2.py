# find right closest greater by traverser from end and from begin
def test(nums):
    # find right closest greater
    stack = []
    res = [-1]*len(nums)
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            stack.pop()
        if stack:
            res[i] = nums[stack[-1]]
        stack.append(i)
    print(nums)
    print(res)

def test2(nums):
    # find right closest greater
    stack = []
    res = [-1]*len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            res[index] = nums[i]
        stack.append(i)
    print(nums)
    print(res)
test([1,5,4,7])
test2([1,5,4,7])

