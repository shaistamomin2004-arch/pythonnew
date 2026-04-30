number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("choose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("select the operation (1/2/3/4): ")

if operation == '1':
    print(f"number1 + number2: {number1 + number2}")
elif operation == '2':
    print(f"numer1 - number2 : {number1 - number2}")
elif operation == '3':
    print(f"number1 * number2 : {number1 * number2}")
elif operation == '4':
    print(f"number1 / number2 : {number1 / number2}")
else:
    print ("wrong choice")


if number1 > number2:
    pass
else:
    print(f"{number1} <= {number2}")