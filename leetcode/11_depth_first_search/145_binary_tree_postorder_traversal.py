def postoderTraversal(root):
    stack, res = [], []
    current = root
    while current or stack:
        ## 
        while current:
            ## xx
            stack.append(current)
            ## xx
            current = current.left
            ## 
        ## xx
        current = stack.pop()
        current = current.right
        ## 
    
    return res
        
            