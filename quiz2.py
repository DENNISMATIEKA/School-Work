import re

try:
    # Step 1: Prompt the user for input
    expression = input("Enter a mathematical expression: ")

    # Step 5: Validate the expression
    if not re.match(r"^[\d+\-*/()%^ ]+$", expression):
        raise ValueError("Invalid characters in expression. Please use only numbers and operators.")

    # Step 2 & 4: Evaluate and print the result
    result = eval(expression)
    print(f'The result of your expression "{expression}" is: {result}')

except (SyntaxError, ZeroDivisionError) as e:
    # Step 3: Handle specific errors
    print(f"Error: {str(e)}")

except ValueError as ve:
    # Handle validation errors
    print(f"Error: {ve}")
