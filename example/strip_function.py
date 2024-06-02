'''
The strip() function in Python is used to remove leading and trailing characters (default is whitespace) from a string. It can be very handy when you need to clean up user input or data.
'''

text = "    hello, world!    "

left_cleaned_text = text.lstrip()
right_cleaned_text = text.rstrip()

print(f"Original: '{text}'")
print(f"Original: '{left_cleaned_text}'")
print(f"Original: '{right_cleaned_text}'")
