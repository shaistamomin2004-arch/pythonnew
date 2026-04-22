season = ["summer" , "winter" , "rain" , "spring" , "autumn" , "monsoon"]
print(season)
season.sort()  # we can sort the list in ascending order by using sort
print(season)
season.sort(reverse=True)  # we can sort the list in descending order by using sort with reverse parameter
print(season)


season2 = [1, 5, 3, 2, 4]
print(season2)
season2.sort()  # we can sort the list in ascending order by using sort
print(season2)
season2.sort(reverse=True)  # we can sort the list in descending order by using sort with reverse parameter
print(season2)

#===================copying method=========================
myseason = season
season.pop()  # we can remove the last item from the list by using pop
print(season)
print(myseason)  # myseason also changes because it is a reference to the same list


#==================reversing method=========================
myseason.reverse()  # we can reverse the list by using reverse
print(myseason)


#=================counting method=========================
num = [1, 2, 3, 4, 5, 1, 2, 3]
print(num)
print(num.count(1))  # we can count the occurrences of an item in the list by using count

#=================indexing method=========================
print(num.index(5))  # we can find the index of the first occurrence of an item in the list by using index
