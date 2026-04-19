season = ["summer" , "winter" ]
print(season)
season.append("rain")  # we can add the word in the end of list by using append
print(season)

season.insert(2 , "spring")  # we can add the word at a specific index by using insert)
print(season)
season.extend(["autumn" , "monsoon"])  # we can add the word in the end of list by using extend
print(season)


cold = ["rain","snow"]
print(cold)
cold.extend(season)  # we can add the word of one list to another list by using extend
print(cold)
