for i in range(4):
    for j in range(4):
        if (i,j) == (1,1):
            print(i,j)
            break
    else: # Nếu for j gặp break, nó cũng sẽ break for i
        continue
    break