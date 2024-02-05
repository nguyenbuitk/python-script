try:
    # Get input from the user
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    # Attempt to divide the numbers
    result = numerator / denominator
    
    # Print the result if no exception occurs
    print("Result is:", result)
except ZeroDivisionError:
    # This will catch any division by zero attempt and print an error message
    print("Error! You can't divide by zero.")
