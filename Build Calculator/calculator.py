num1 = float(input("enter your first number : "))
operation = input("Enter the required operation : ")
num2 = float(input("enter your second number : "))


if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("error")
