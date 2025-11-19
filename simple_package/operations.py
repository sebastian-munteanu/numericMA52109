###
## simple_package - Module operations.py
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def trigonometric_sine(x):
    """Calculate the sine of x (x in radians)."""
    import math
    return math.sin(x)

def trigonometric_cosine(x):
    """Calculate the cosine of x (x in radians)."""
    import math
    return math.cos(x)

def logarithm(x, base=10):
    """Calculate the logarithm of x with given base."""
    import math
    return math.log(x, base)

def interface():
    print("Welcome to the calculator!")
    print("Choose calculator type:")
    print("1 - Simple Calculator (includes basic operations)")
    print("2 - Advanced Calculator (includes trigonometric functions and logarithms)")
    
    while True:
        try:
            calculator_type = input("Enter 1 or 2: ")
            
            if calculator_type == '1':
                simple_interface()
                break
            elif calculator_type == '2':
                advanced_interface()
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")

def simple_interface():
    print("Welcome to the simple calculator!")
    print("Enter 'exit' to quit.")
    
    while True:
        try:
            user_input = input("Enter operation (add, subtract, multiply, divide) and two numbers: ")
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Invalid input format. Please enter an operation and two numbers.")
            
            operation, num1, num2 = parts
            num1 = float(num1)
            num2 = float(num2)
            
            if operation == 'add':
                result = add(num1, num2)
            elif operation == 'subtract':
                result = subtract(num1, num2)
            elif operation == 'multiply':
                result = multiply(num1, num2)
            elif operation == 'divide':
                result = divide(num1, num2)
            else:
                raise ValueError("Unknown operation. Please use add, subtract, multiply, or divide.")
            
            print(f"The result is: {result}")
        
        except Exception as e:
            print(f"Error: {e}. Please try again.") 

def advanced_interface():
    print("Welcome to the advanced calculator!")
    print("Enter 'exit' to quit.")
    
    while True:
        try:
            user_input = input("Enter operation (log, sin, cos) and a number: ")
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            
            parts = user_input.split()
            if len(parts) != 2:
                raise ValueError("Invalid input format. Please enter an operation and a number.")
            
            operation, num1 = parts
            num1 = float(num1)
            
            if operation == 'log':
                result = logarithm(num1)
            elif operation == 'sin':
                result = trigonometric_sine(num1)
            elif operation == 'cos':
                result = trigonometric_cosine(num1)
            else:
                raise ValueError("Unknown operation. Please use add, subtract, multiply, or divide.")
            
            print(f"The result is: {result}")
        
        except Exception as e:
            print(f"Error: {e}. Please try again.") 
