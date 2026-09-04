def calculate_expression(expression):
    # Replace 'x' with '*' for multiplication
    expression = expression.replace('x', '*')
    # Replace ':' with '/' for division
    expression = expression.replace(':', '/')
    try:
        # Evaluate the modified expression and return the result
        return eval(expression)
    except ZeroDivisionError:
        return "Error: Oh noes! Division by zero!! :("
    except:
        return "Error: Oh noes! Invalid expression... D:"

if __name__ == "__main__":
    print("Welcome to EZ-Calculator! :D")
    while True:
        expression = input("Enter an expression or 'q' to quit: ").strip()
        if expression.lower() == "q":
            print("Exiting the calculator.")
            break
        expression = expression.rstrip("=")  # Automatically strip the '=' if present
        result = calculate_expression(expression)
        print("Result:", result)
 
