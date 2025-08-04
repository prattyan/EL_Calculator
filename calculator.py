# Build an Advanced Calculator CLI App

import math
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Cannot calculate square root of negative number"

def percentage(x, y):
    return (x / 100) * y

def factorial(x):
    if x < 0:
        return "Error: Factorial not defined for negative numbers"
    if x != int(x):
        return "Error: Factorial only defined for integers"
    return math.factorial(int(x))

def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

def logarithm(x, base=math.e):
    if x <= 0:
        return "Error: Logarithm not defined for non-positive numbers"
    if base == math.e:
        return math.log(x)
    elif base == 10:
        return math.log10(x)
    else:
        return math.log(x, base)

def get_number_input(prompt, allow_negative=True):
    while True:
        try:
            value = float(input(prompt))
            if not allow_negative and value < 0:
                print("Error: Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def display_menu():
    print("\n" + "-"*50)
    print("         CLI CALCULATOR ")
    print("-"*50)
    print("Basic Operations:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Power (x^y)")
    print("  6. Square Root")
    print("  7. Percentage (x% of y)")
    print("  8. Factorial")
    print("  9. Sine")
    print("  10. Cosine")
    print("  11. Tangent")
    print("  12. Natural Logarithm (ln)")
    print("  13. Common Logarithm (log10)")
    print("  14. Custom Base Logarithm")
    print("  15. Calculator History")
    print("  16. Clear History")
    print("  17. Exit")
    print("-"*50)

def format_result(result):
    if isinstance(result, str):  # Error message
        return result
    elif isinstance(result, float):
        if result.is_integer():
            return str(int(result))
        else:
            return f"{result:.6f}".rstrip('0').rstrip('.')
    return str(result)
def main():
    calculation_history = []  
    print("Welcome to the CLI Calculator!")
    print("Type 'help' at any prompt for assistance.")
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-17): ").strip()
            if choice == '17':
                print("\n Thank you for using the CLI Calculator!")
                print("Have a great day! ")
                break
            elif choice in ['1', '2', '3', '4', '5', '7', '14']:
                if choice == '14':
                    num1 = get_number_input("Enter the number: ", allow_negative=False)
                    base = get_number_input("Enter the base: ", allow_negative=False)
                    if base <= 0 or base == 1:
                        print("Error: Base must be positive and not equal to 1.")
                        continue
                    result = logarithm(num1, base)
                    operation = f"log_{base}({num1})"
                else:
                    num1 = get_number_input("Enter first number: ")
                    num2 = get_number_input("Enter second number: ")
                    
                    if choice == '1':
                        result = add(num1, num2)
                        operation = f"{num1} + {num2}"
                    elif choice == '2':
                        result = subtract(num1, num2)
                        operation = f"{num1} - {num2}"
                    elif choice == '3':
                        result = multiply(num1, num2)
                        operation = f"{num1} × {num2}"
                    elif choice == '4':
                        result = divide(num1, num2)
                        operation = f"{num1} ÷ {num2}"
                    elif choice == '5':
                        result = power(num1, num2)
                        operation = f"{num1}^{num2}"
                    elif choice == '7':
                        result = percentage(num1, num2)
                        operation = f"{num1}% of {num2}"
            elif choice in ['6', '8', '9', '10', '11', '12', '13']:
                if choice == '6':
                    num1 = get_number_input("Enter number: ", allow_negative=False)
                    result = square_root(num1)
                    operation = f"√{num1}"
                elif choice == '8':
                    num1 = get_number_input("Enter a non-negative integer: ", allow_negative=False)
                    result = factorial(num1)
                    operation = f"{num1}!"
                elif choice == '9':
                    num1 = get_number_input("Enter angle in degrees: ")
                    result = sin_deg(num1)
                    operation = f"sin({num1}°)"
                elif choice == '10':
                    num1 = get_number_input("Enter angle in degrees: ")
                    result = cos_deg(num1)
                    operation = f"cos({num1}°)"
                elif choice == '11':
                    num1 = get_number_input("Enter angle in degrees: ")
                    result = tan_deg(num1)
                    operation = f"tan({num1}°)"
                elif choice == '12':
                    num1 = get_number_input("Enter number: ", allow_negative=False)
                    result = logarithm(num1)
                    operation = f"ln({num1})"
                elif choice == '13':
                    num1 = get_number_input("Enter number: ", allow_negative=False)
                    result = logarithm(num1, 10)
                    operation = f"log₁₀({num1})"
            elif choice == '15':
                if calculation_history:
                    print("\n CALCULATION HISTORY:")
                    print("-" * 40)
                    for i, (op, res) in enumerate(calculation_history, 1):
                        print(f"{i:2d}. {op} = {res}")
                    print("-" * 40)
                    print(f"Total calculations: {len(calculation_history)}")
                else:
                    print("\n No calculations in history yet.")
                continue

            elif choice == '16':
                calculation_history.clear()
                print("\n  History cleared successfully!")
                continue

            else:
                print(" Invalid choice! Please enter a number between 1 and 17.")
                continue
            if 'result' in locals():
                formatted_result = format_result(result)
                print(f"\nResult: {operation} = {formatted_result}")
                if not isinstance(result, str) or not result.startswith("Error"):
                    calculation_history.append((operation, formatted_result))
                del result
        except KeyboardInterrupt:
            print("\n\n👋 Calculator interrupted. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n An unexpected error occurred: {e}")
            print("Please try again.")
if __name__ == "__main__":
    main()
