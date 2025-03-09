def peakIndexInMountainArray(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        print(f"l: {l}, r: {r}, mid: {mid}")
        if arr[mid] > arr[mid + 1]:
            print("The high is going down remove left part")
            r = mid # mid still can be peak
        else:
            l = mid + 1 # mid can't be peak, because it going up, so we skip peak
    # l and r are converge
    return l

print(peakIndexInMountainArray([0,3,5,12,2]))
            