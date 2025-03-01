from typing import List

class Solution:
    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print("")
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, cols = len(board), len(board[0])
        
        self.print_matrix(board)
        for i in range(rows):
            for j in range(cols):
                # print("i, j: ", i, j)
                k = 0
                m, n = i, j
                if board[m][n] == word[k]:
                    print("===================")
                    print(f"Start position: board[{m}][{n}] = {board[m][n]}")
                    if k == len(word) - 1:
                        return True
                    visited = set()
                    
                    # stack for DFS: (position, path taken)
                    stack = [((m,n), [])]
                    while stack:
                        # print(stack)
                        print(f"Current position: board[{m}][{n}] = {board[m][n]}")
                        m, n = stack[-1][0]
                        visited.add((m,n))

                        found_next_word = False
                        
                        # Explore all 4 possible direction
                        for dr, dc in directions:
                            new_row, new_col = m + dr, n + dc
                            
                            # Check boundaries, character match, and ensure cell is not revisited
                            if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == word[k+1] and (new_row, new_col) not in visited and (dr, dc) not in stack[-1][1]:
                                
                                # Move to next character in word
                                k += 1
                                print(f"Next position: board[{new_row}][{new_col}] = {board[new_row][new_col]}")
                                print("")
                                stack[-1][1].append((dr, dc))
                                stack.append(((new_row, new_col), []))
                                visited.add((new_row, new_col))
                                print(f"Visited: ", visited)
                                if k == len(word) - 1:
                                    return True
                                
                                # Update current position
                                m = new_row
                                n = new_col
                                found_next_word = True
                                break
                        # If no next valid character found, backtrack
                        if not found_next_word:
                            stack.pop()             # remove last position from stack
                            visited.remove((m,n))   # Unmark visited
                            k -= 1
                            
        return False
    
solution = Solution()
# print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
# print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
# print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(solution.exist([[["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB"))
# print(solution.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(solution.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa"))


['a', 'a', 'a', 'a']
['a', 'a', 'a', 'a']
['a', 'a', 'a', 'a']