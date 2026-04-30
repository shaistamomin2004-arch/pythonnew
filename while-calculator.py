number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
print("choose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
operation = input("select the operation (1/2/3/4/5): ")

while operation != '5':
    if operation == '1':
     print(f"number1 + number2: {number1 + number2}")
    elif operation == '2':
     print(f"numer1 - number2 : {number1 - number2}")
    elif operation == '3':
     print(f"number1 * number2 : {number1 * number2}")
    elif operation == '4':
     print(f"number1 / number2 : {number1 / number2}")
    elif operation == '5':
     print(f"exit")
    else:
     print ("wrong choice")
    operation = input("select the operation (1/2/3/4/5): ")
else:   print("you have exited the calculator")