print("==========for loop==========" )
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color) # prints each color in the list


numbers = [1, 4, 5, 7]
for number in numbers:
    print(number +2) # prints each number in the list plus 2
print(f"numbers: {numbers}") # prints the original list of numbers, showing that it has not been modified by the for loop


names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name.upper()) # prints each name in uppercase


print("=========string-=========")
for char in "Hello":
    print(char) # prints each character in the string "Hello" on a new line

print("=========range-=========")
for i in range(5): #range(5) generates a sequence of numbers from 0 to 4
    print(i) # prints the numbers from 0 to 4, as range(5) generates a sequence of numbers starting from 0 up to, but not including, 5

print("=========range with starting value-=========")
for i in range(2, 7): # range(2, 7) generates a sequence of numbers from 2 to 6
    print(i) # prints the numbers from 2 to 6

print("=========range with starting value and increment-=========")
for i in range(0, 10, 2): # range(0, 10, 2) generates a sequence of numbers from 0 to 8, incrementing by 2
    print(i) # prints the even numbers from 0 to 8

print("=========nested for loop-=========")
for i in range(1, 4): # outer loop iterates over the numbers 1 to 3
    for j in range(1, 4): # inner loop iterates over the numbers 1 to 3
        print(f"{i} * {j} = {i * j}") # prints the product of i and j for each iteration of the inner loop


print("===========nested loop : break statement==========")
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2: # checks if both i and j are equal to 2
            break # breaks out of the inner loop when the condition is met
        print(f"{i} * {j} = {i * j}") # prints the product of i and j for each iteration of the inner loop, except when i and j are both 2