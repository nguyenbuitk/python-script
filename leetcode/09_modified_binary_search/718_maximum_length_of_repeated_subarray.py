from typing import List

# 12345
# 345
def findLength(nums1: List[int], nums2: List[int]) -> int:
    def isSubList(lst, subLst):
        print(f"list: {lst}")
        print(f"sublist: {subLst}")
        for i in range(len(lst) - len(subLst) + 1):
            if lst[i:i+len(subLst)] == subLst:
                return True
        return False

    l, r = 0, 0
    count = 0
    while r < len(nums1):
        print(f"\nl: {l} {nums1[l]}, r: {r} {nums1[r]}")
        print(f"count: {count}")
        if isSubList(nums2, nums1[l:r+1]):
            print("test")
            count += 1
            r += 1
            continue
        else:
            l += 1
            r += 1
    return count
            
print(findLength([0,0,0,0,0], [0,0,0,0,0]))