season = ('spring', 'summer', 'autumn', 'winter')  # we can create a tuple by using parentheses
print(f" seasons are: {season}")
print(f" season type is : {type(season)}")  # we can check the type of the tuple by using type function

print("============tuple==========")
name = ('John', 'Doe', 'Smith')  # we can create a tuple by using parentheses
print(f" name is: {name}")


chaos = ("shaixx" , 20 , 5.5 , True)  # we can create a tuple with different data types
print(f" chaos is: {chaos}")

# we can also create a tuple without using parentheses
colors = 'red', 'green', 'blue'  # we can create a tuple without using parentheses
print(f" colors are: {colors}")
print(f"the count of colors is: {len(colors)}")  # we can get the count of the tuple by using len function
print(f"the first color is: {colors[0]}")  # we can access the elements of the tuple by using index
print(f"the last color is: {colors[-1]}")  # we can access the last element of the tuple by using negative index
print(f"the colors from index 1 to 2 are: {colors[1:3]}")  # we can access a range of elements in the tuple by using slicing



print("============edit tuple==========")
# we cannot change the elements of a tuple because tuples are immutable
# but we can create a new tuple by concatenating two tuples
chaoslist = list(chaos)  # we can convert a tuple to a list by using list function
print(f" chaoslist is: {chaoslist}")
print(f" chaoslist type is: {type(chaoslist)}")  # we can check the type of the list by using type function
chaoslist[0] = "namo"  # we can change the elements
chaoslist.append("asho")  # we can add new elements to the list by using append function
chaos = tuple(chaoslist)  # we can convert the list back to a tuple by using tuple function
print(f" chaos is: {chaos}")
print(f" chaoslist is: {chaoslist}")
print(f" chaoslist type is: {type(chaoslist)}")  # we can check the type of the list by using type function
chaoslist = tuple(chaos)  # we can convert the list back to a tuple by using tuple function
print(f" chaoslist is: {type(chaoslist)}")





print("============tuple methods==========")
# we can use the count method to count the number of occurrences of an element in the tuple
numbers = (1, 2, 3, 4, 5, 1, 2, 1)
print(f" numbers are: {numbers}")
print(f" the count of 1 in numbers is: {numbers.count(1)}")  # we can use the count method to count the number of occurrences of an element in the tuple
print(f" the index of 3 in numbers is: {numbers.index(3)}")  # we can use the index method to get the index of an element in the tuple



print("============tuple operators==========")
# we can use the + operator to concatenate two tuples ---------  + operator is used to concatenate two tuples
name1 = ('John', 'Doe')
name2 = ('Smith', 'Johnson')
all_names = name1 + name2  # we can concatenate two tuples by using + operator
print(f" all names are: {all_names}")
print(name1 + name2)  # we can also concatenate two tuples by using + operator directly


name3 = name1 * 2  # we can repeat a tuple by using * operator
print(f" name3 is: {name3}")
print(name1 * 2)  # we can also repeat a tuple by using * operator directly
print(f"name1 is name3: {name1 is name3}")  # we can check if two tuples are the same by using is operator
print(f"name1 is not name3: {name1 is not name3}")  # we can check if two tuples are not the same by using is not operator
print(f"'Smith' in name2: {'Smith' in name2}")  # we can check if an element is in a tuple by using in operator
print(f"'Smith' not in name2: {'Smith' not in name2}")  # we can check if an element is not in a tuple by using not in operator
