from typing import List

def numberOfAlter(colors: List[int], k: int) -> int:
    indexes = list(range(len(colors)))
    nums_str = " ".join(str(num).rjust(3) for num in colors)
    indexes_str = " ".join(str(i).rjust(3) for i in indexes)
    
    print(f"Indexes:{indexes_str}")
    print(f"Char:   {nums_str}")
    colors = colors + colors[:k-1]
    right =  1
    res = 0
    number_of_contiguous = 1
    while right < len(colors):
        if colors[right] != colors[right-1]:
            number_of_contiguous += 1
            right += 1
            if number_of_contiguous == k:
                res += 1
                number_of_contiguous -= 1
                
        else:
            right += 1
            number_of_contiguous = 1
        
    return res
print(numberOfAlter([0,1,0,1,0], 3))
print(numberOfAlter([0,1,0,0,1,0,1], 6))
