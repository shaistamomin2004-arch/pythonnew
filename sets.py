print("============sets===========")
seasons = {'spring', 'summer', 'autumn', 'winter'} # we can create a set by using curly braces
print(f" seasons are: {seasons}")
print(f" season type is : {type(seasons)}")  # we can check the type of the set by using type function

numbers = {1, 2, 3, 4, 5 ,4} # we can create a set with different data types
print(f" numbers are: {numbers}") # we can see that the duplicate element is removed in the set

chaos = {"shaixx" , 20 , 5.5 , True}  # we can create a set with different data types
print(f" chaos is: {chaos}")

# 1. Sets are unordered: The print order depends on internal hashing, not insertion order.
# 2. True == 1: In Python, True and 1 are considered equal. 
# Since sets do not allow duplicates, only one of them will be stored.
chaos = {"shaixx" , True, 1 , 5.5 }  
print(f" chaos is: {chaos}") 

chaos = {"shaixx" ,True, 1 , 5.5 }  # we can create a set with different data types
print(f" chaos is: {chaos}")

chaos = {"shaixx" , 1 ,True , 5.5 }  # we can create a set with different data types
print(f" chaos is: {chaos}")

chaos = {"shaixx" ,False, 0 , 5.5 }  # we can create a set with different data types
print(f" chaos is: {chaos}")

print(f"lentgh of chaos is: {len(chaos)}") # we can get the length of the set by using len function

names = {'John', 'Doe', 'Smith'}  # we can create a set by using curly braces
print(f" names are: {names}")
print(f"smith is not in names: {'Smith' not in names}") # we can check if an element is not in the set by using not in operator
print(f"Smith is in names: {'Smith' in names}") # we can check if an element is in the set by using in operator

print("============add elements in set===========")


# we can add new elements to the set by using add method
colors = {'red', 'green', 'blue'}
print(f" colors are: {colors}")
colors.add('yellow')
print(f" colors are: {colors}")

colors2 = {'purple', 'orange'}
colors.update(colors2) # we can add multiple elements to the set by using update method
print(f" colors are: {colors}")

numberlist = {1, 2, 3, 4, 5}
colors.update(numberlist) # we can add multiple elements to the set by using update method
print(f" colors are: {colors}")



print("============remove elements from set===========")
# we can remove an element from the set by using remove method
colors.remove('yellow')
print(f" colors are: {colors}")

# we can remove an element from the set by using discard method
colors.discard('red')
print(f" colors are: {colors}")

# we can remove the any element from the set by using pop method
last_color = colors.pop()
print(f"color removed: {last_color}")
print(f" colors are: {colors}")

# we can remove all elements from the set by using clear method
colors.clear()
print(f" colors are: {colors}")

# we can delete the set by using del keyword
del colors
