directions = [1,2,3,4]

while True:
    found_five = False
    for a in directions:
        if a == 5:
            found_five = True
            break
    
    if not found_five:
        break