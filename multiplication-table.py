print("===========for loop : multiplication table==========")
for i in range(1, 11): # outer loop iterates over the numbers 1 to 10
    row = "" # initializes an empty string to build the row of the multiplication table
    for j in range(1, 11): # inner loop iterates over the numbers 1 to 10
        row += f"{i * j}\t" # appends the product of i and j to the row string
    print(row) # prints the row of the multiplication table



print("===========while loop : multiplication table===========")
x = 1
while x <= 10: # outer loop iterates while x is less than or equal to 10
    row = "" # initializes an empty string to build the row of the multiplication table
    y = 1
    while y <= 10: # inner loop iterates while y is less than or equal to 10
        row += f"{x * y}\t" # appends the product of x and y to the row string
        y += 1 # increments y by 1 for the next iteration of the inner loop
    print(row) # prints the row of the multiplication table
    x += 1 # increments x by 1 for the next iteration of the outer loop