print("===========set method ==========")
# we can create a set by using curly braces
colors = {'red', 'green', 'blue'}
color1 = {'purple', 'orange'}
print(f" colors are: {colors}")
print(f" color1 are: {color1}")

allcolors = colors.union(color1)  # we can combine two sets by using union method
print(f" all colors are: {allcolors}")

allcolors2 = colors | color1  # we can also combine two sets by using | operator
print(f" all colors are: {allcolors2}")

colors.update(color1)  # we can also combine two sets by using update method
print(f" colors are: {colors}")



print("============intersection of sets===========")
# we can get the common elements of two sets by using intersection method
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = set1.intersection(set2)  # we can get the common elements of two sets by using intersection method
print(f" common elements are: {common}")

common2 = set1 & set2  # we can also get the common elements of two sets by using & operator
print(f" common elements are: {common2}")

set1.intersection_update(set2)  # we can also get the common elements of two sets by using intersection_update method
print(f" set1 is updated to common elements: {set1}")

print(f" set2 is not changed: {set2}")  # we can check that set2 is not changed by using print function

set1 &= set2  # we can also get the common elements of two sets by using &= operator
print(f" set1 is updated to common elements: {set1}")  # we can check that set1 is updated by using print function
print(f" set2 is not changed: {set2}")  # we can check that set2 is not changed by using print function