def findTarget(res, target):
    l, r = 0, len(res) - 1
    while l <= r:
        mid2 = (l+r)//2
        print(f"mid2 = res[{mid2}] = {res[mid2]}, l = res[{l}] = {res[l]}, r = res[{r}] = {res[r]}", end = "\n\n")
        if res[mid2] == target:
            break
        elif res[mid2] < target:
            l = mid2 + 1
        else:
            r = mid2 - 1
    print(f"end: mid2_index = {mid2}, mid2 = {res[mid2]}")
findTarget([1,2,4,5,6,7,8], 3)