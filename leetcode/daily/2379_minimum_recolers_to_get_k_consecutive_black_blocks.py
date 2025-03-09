# sliding window
# when to expand? the consecutive black < k
# when to shrink? the consecutive black >= k

def minimumRecolors(blocks: str, k: int) -> int:
    # Tạo danh sách index
    indexes = list(range(len(blocks)))
    
    # In list số theo hàng thẳng
    nums_str = " ".join(str(num).rjust(3) for num in blocks)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)

    print(f"Indexes:{indexes_str}")
    print(f"Char:   {nums_str}")

    left, right = 0, 0
    number_of_consecutive_block = 0
    number_of_operation = 0
    res = float('inf')
    
    while right < len(blocks):
        print("")
        print(f"Left: {left} ({blocks[left]}), Right: {right} ({blocks[right]})")

        # Shrink the windows
        if number_of_consecutive_block == k:
            print("Shrink the window")
            res = min(res, number_of_operation)
            while left < len(blocks) and blocks[left] != 'W':
                number_of_consecutive_block -= 1
                left += 1
            number_of_consecutive_block -= 1
            number_of_operation -= 1
            left += 1
        # Expand the windows
        if blocks[right] == 'W':
            number_of_consecutive_block += 1
            number_of_operation += 1
            right += 1
        else:
            number_of_consecutive_block += 1
            right += 1
        print(f"number of operation:            {number_of_operation}")
        print(f"number of consecutive blocks:   {number_of_consecutive_block}")
        
    if number_of_consecutive_block == k:
        res = min(res, number_of_operation)

    return res
# minimumRecolors("WBBWWBBWBW", 7)
# print(minimumRecolors("WBB", 1))
print(minimumRecolors("BWWWBB", 6))
# Indexes:  0   1   2   3   4   5   6   7   8   9
# Char:     W   B   B   W   W   B   B   W   B   W
