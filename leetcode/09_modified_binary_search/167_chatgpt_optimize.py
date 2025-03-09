def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        curr_sum = numbers[l] + numbers[r]
        if curr_sum == target:
            return [l+1, r+1]
        elif curr_sum >  target:
            # move right pointer to get smaller sum
            r -= 1
        else:
            l += 1
    