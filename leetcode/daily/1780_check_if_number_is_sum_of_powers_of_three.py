def checkPowerOfThree(n: int):
    res = []
    x = 0
    while 3**x <= n:
        res.append(3**x)
        x += 1
    res.reverse()
    print(res)
    def subSum(nums, target):
        # print(f"Current check nums: {nums} || target: {target} ")
        if target in nums:
            return True
        if len(nums) < 1:
            return False
        return subSum(nums[1:], target - nums[0]) or subSum(nums[1:], target)
    return subSum(res, n)
print(checkPowerOfThree(3678852))
        