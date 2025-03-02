from typing import List

def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    res, n1, n2 = [], 0, 0
    while n1 < len(nums1) and n2 < len(nums2):
        if nums1[n1][0] == nums2[n2][0]:
            res.append([nums1[n1][0], nums1[n1][1] + nums2[n2][1]])
            n1 += 1
            n2 += 1
        elif nums1[n1][0] < nums2[n2][0]:
            res.append([nums1[n1][0], nums1[n1][1]])
            n1 += 1
        else:
            res.append([nums2[n2][0], nums2[n2][1]])
            n2 += 1
    res.extend(nums1[n1:])
    res.extend(nums2[n2:])