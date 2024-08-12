import os
import sys
import time

def move_cursor_to_bottom_left(text):
    # Get the terminal size
    rows, columns = os.popen('stty size', 'r').read().split()
    rows, columns = int(rows), int(columns)
    
    # Move cursor to the bottom left corner
    sys.stdout.write(f"\033[{rows};1H{text}")
    sys.stdout.flush()
print("hello world")
user_input = input("enter something")
# Example usage
move_cursor_to_bottom_left(f"Progress: %")
print("\nDone!")
