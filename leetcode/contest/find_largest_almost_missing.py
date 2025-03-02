from collections import Counter
def largestInger(nums, k):
    count = Counter()
    for i in range(len(nums)-k+1):
        count += Counter(set(nums[i:i+k]))
    print(count)
    values = min(count.values())
    if values > 1:
        return -1
    keys_with_min_val = [k for k, v in count.items() if v == values]
    return max(keys_with_min_val)
# print(largestInger([3,9,2,1,7],3))
print(largestInger([0,0],2))
