def divide(x, y):
    try:
        result = x/y
        print("Success, result is {result}")
        
    except ZeroDivisionError:
        print("Sorry, you are dividing by zero")
        
def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
    except ValueError:
        print("Sorry, the value you entered is not a valid number")
        
        
if __name__ == "__main__":
    main()