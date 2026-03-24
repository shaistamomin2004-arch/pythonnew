season = ["summer", "winter", "rain", "spring" ]
print(season)
print(len(season))

name =["shaista" , 20 , 3.5, "student"]
print(name)
print(name[1])
print(name[3])
print(name[-1]) #negative index start from back
print(f" the ans is : {name[-4]}")
print(name[0:3])  # range of index
print(name[0:])
print(name[:3])  
print(name[-3:-1]) 
name[2] = "graduate"  # we can change the word from the list
print(name)
name[-1] = "bachlor" # we can change the word from the list even in negative
print(name)
name[0:2] = "shaixx" , "21"    # we can change the word from the list even in range
print(name)
name[0:1] = "shaixx" 
print(name)




days = list(("mon", "tues","wed", "fri","sat"))
print(days)