from typing import List

def minEatingSpeed(piles: List[int], h: int) -> int:
    # find min k:
    # sum((piles[i] // k) + 1) == h

    
    average_hour = h // len(piles) # = 2
    # min banana per hour to eat all of them. Nó phải ăn hết đống ít nhất trong vòng min_k_posible hours, thì may ra mới có cơ hội ăn hết các đống còn lại
    if min(piles) % average_hour != 0:
        min_k_posible = (min(piles) // average_hour) + 1
        print(min_k_posible)
    else: min_k_posible =  min(piles) // average_hour
    print(min_k_posible)
    if max(piles) % average_hour != 0:
        max_k_possible = (max(piles) // average_hour) + 1
    else: max_k_possible = max(piles) // average_hour
    
    for i in range(min_k_posible, max_k_possible+1):
        print(f"i: {i}, min_k: {min_k_posible}, max_k: {max_k_possible}")
        total_hour_needed = 0
        for j in range(len(piles)):
            if piles[j] % i != 0:
                total_hour_needed += (piles[j] // i ) + 1
                print(f"total hour need: {total_hour_needed}")

            else: 
                total_hour_needed += piles[j] // i
                print(f"total hour need: {total_hour_needed}")
        print(f"total hour need: {total_hour_needed}")
        if total_hour_needed <= h:
            return i
    return -1    
# print(minEatingSpeed([3,6,7,11], 8))
# print(minEatingSpeed([30,11,23,4,20], 5))
# print(minEatingSpeed([30,11,23,4,20], 6))

print(minEatingSpeed([2,2], 2))