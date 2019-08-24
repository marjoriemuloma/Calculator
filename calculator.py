# This program is a simple calculator
# We shall develop it further as we go on with the project



name = str(input("What is your name?: "))

operation = str(
    input(
        """
        Type add for addition sub for
        subtraction mul for multiplication
        and div fordivision: 
        """
    )
)

if operation == 'add':
    print("Welcome to the calculator " + name)
    print("This is a simple calculator that adds two integers... enjoy!")

    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

    result = num1 + num2

    print("The answer is " + str(result))

elif operation == 'sub':
    print("Welcome to the calculator " + name)
    print("This is a simple calculator that subtracts two integers... enjoy!")

    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter another integer: "))

    result = num1 - num2

    print("The answer is " + str(result))


elif operation == 'mul':
        print("Welcome to the calculator " + name)
        print("This is a simple calculator that multiplies two integers... enjoy!")

        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter another integer: "))

        result = num1 * num2

        print("The answer is " + str(result))


elif operation == 'div':
        print("Welcome to the calculator " + name)
        print("This is a simple calculator that divides two integers... enjoy!")

        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter another integer: "))

        result = num1 / num2

        print("The answer is " + str(result))


else:
    print("The operation does not exist... Try again.")
