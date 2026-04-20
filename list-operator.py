warmseason = ['spring', 'summer']
coldseason = ['autumn', 'winter']
print(f" seasons are: {warmseason} + {coldseason}")

warmseason.extend(coldseason)  # we can extend the list by using extend method
print(warmseason)



#====================membership operator=========================
print('summer' in warmseason)  # we can check if an item is in the list by using in operator
print('monsoon' in warmseason)  # we can check if an item is in the list by using in operator
print('monsoon' not in warmseason)  # we can check if an item is not in the list by using not in operator


#====================identity operator=========================
print(warmseason is coldseason)  # we can check if two lists are the same object by using is operator
print(warmseason is not coldseason)  # we can check if two lists are not the same object by using is not operator

season = warmseason + coldseason  # we can concatenate two lists by using + operator
print(season)
season2 = season # we can assign one list to another variable, but they will point to the same object
print(season2 is season)  # season and season2 are the same object
print(season2 is season)  # season2 is a different object than season
print(season2 == season)  # season2 has the same content as season
print(season2 is not season) # season2 is not the same object as season, but they have the same content

