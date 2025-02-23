class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Edge case: If k is equal to the length of num, return "0"
        if len(num) == k:
            return "0"
        
        stack = []  # Monotonic stack to store the final digits
        
        for digit in num:
            # Remove elements from the stack if they are larger than the current digit
            # and we still need to remove more digits (k > 0)
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            # Append the current digit to the stack
            stack.append(digit)
        
        # If there are still digits to remove, remove from the end
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        # Convert stack to string and remove leading zeros
        result = "".join(stack).lstrip('0')
        
        # If result is empty, return "0"
        return result if result else "0"
