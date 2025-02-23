def dailyTemperatures(temperatures):
    stack = []      # Monotoic stack to store (temperature, index)
    res = [0]*len(temperatures)     # Result array initialized with 0
    for i in range(len(temperatures) -1, -1, -1):
        # Remove all the element < tempratures[i]
        while stack and stack[-1][0] < temperatures[i]:
            stack.pop()
            
        # If stack is not empty, calculate the waiting day
        if stack:
            res[i] = stack[-1][1] - i
        
        # Push current temperature and its index to the stack
        stack.append([temperatures[i], i])
    return res

print(dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))