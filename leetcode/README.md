# Dynamic Programming
### Finding relationships among subproblems
What subproblem are needed to solve problem[n]    
e.g.

`problem[4] = 1 + max{ problem[1] + problem[2] + problem[3] }`

### Genelize the relationship
How do we use these subproblem to solve problem[n]
e.g.

`problem[n] = 1 + max{ problem[k] | k < 4, A[k] < A[n] }`

### Implement by solving subproblems in order
```python3
def solving(A):
    L = ...
    ...
    pass
```