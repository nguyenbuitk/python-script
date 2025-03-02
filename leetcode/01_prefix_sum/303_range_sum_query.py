class NumArray:
    def __init__(self, nums):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i-1]
    def sumRange(self, left, right):
        if not left: return self.nums[right]
        return self.nums[right] - self.nums[left - 1]