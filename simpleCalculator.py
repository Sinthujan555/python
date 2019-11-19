

operation = input("Type in the math operation you would like: + Addition, - Subtraction, * Multiplication,/ Division: ")

number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))

if operation == '+':
    print(number1, " + " ,number2, " = ",number1 + number2)

elif operation == '-':
    print(number1, " - " ,number2, " = ",number1 - number2)

elif operation == '*':
    print(number1, " * " ,number2, " = ",number1 * number2)

elif operation == '/':
    print(number1, " / " ,number2, " = ",number1 / number2)

else:
    print("Type A Valid Operation!")


