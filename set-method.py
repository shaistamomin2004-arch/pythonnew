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



print("============difference of sets===========")
# we can get the elements of the first set that are not in the second set by using difference method
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
diff = set3.difference(set4)  # we can get the elements of the first set that are not in the second set by using difference method
print(f" elements in set3 but not in set4 are: {diff}")

diff2 = set3 - set4  # we can also get the elements of the first set that are not in the second set by using - operator
print(f" elements in set3 but not in set4 are: {diff2}")

set3.difference_update(set4)  # we can also get the elements of the first set that are not in the second set by using difference_update method
print(f" set3 is updated to elements that are not in set4: {set3}")  # we can check that set3 is updated by using print function
print(f" set4 is not changed: {set4}")  # we can check that set4 is not changed by using print function

set3 -= set4  # we can also get the elements of the first set that are not in the second set by using -= operator
print(f" set3 is updated to elements that are not in set4: {set3}")  # we can check that set3 is updated by using print function
print(f" set4 is not changed: {set4}")  # we can check that set4 is not changed by using print function

print("============symmetric difference of sets===========")
# we can get the elements that are in either of the sets but not in both sets by using symmetric_difference method
set5 = {1, 2, 3, 4, 5}
set6 = {4, 5, 6, 7, 8}
symdiff = set5.symmetric_difference(set6)  # we can get the elements that are in either of the sets but not in both sets by using symmetric_difference method
print(f" elements that are in either of the sets but not in both sets are: {symdiff}")

symdiff2 = set5 ^ set6  # we can also get the elements that are in either of the sets but not in both sets by using ^ operator
print(f" elements that are in either of the sets but not in both sets are: {symdiff2}")

set5.symmetric_difference_update(set6)  # we can also get the elements that are in either of the sets but not in both sets by using symmetric_difference_update method
print(f" set5 is updated to elements that are in either of the sets but not in both sets: {set5}")  # we can check that set5 is updated by using print function
print(f" set6 is not changed: {set6}")  # we can check that set6 is not changed by using print function



print("=============comparison of sets================")
color4 = {'red', 'green', 'blue'}
color5 = {'yellow'}
color6 = {'red', 'green', 'blue'}
print(f" isdisjoint: {color4 . isdisjoint(color6)}")  # two sets are disjoint if they have no common elements
print(f" issubset: {color4 . issubset(color5)}")  # we can check if a set is contains all element of another set by using issubset method
print(f" issuperset: {color4 . issuperset(color6)}")  # we can check if a set is contains all element of another set by using issuperset method