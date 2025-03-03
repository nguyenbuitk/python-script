def pivotArray(nums, pivot):
    res1, res2, count_pivot = [], [], 0
    for num in nums:
        if num < pivot:
            res1.append(num)
        elif num >  pivot:
            res2.append(num)
        else: count_pivot +=1
    return res1 + [pivot]*count_pivot + res2
print(pivotArray([9,12,5,10,14,3,10], 10))
