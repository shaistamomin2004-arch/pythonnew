firstname = "shaixx"
lastname = "momin"
age = 20
#printing two string at the same time
print(firstname+" "+lastname)
print(firstname+" "+lastname+ " is "+ str(age) +  " years old ")

print(f"{firstname} {lastname} is {age} years old") #f-string
print(f"{firstname} {lastname} \nis {age} years old")
print(f"{firstname} {lastname} \tis \"{age}\" years old")
#\' \\ \n \r \t \b


#casting to number
length = "20"
print(f"type of string is : {type(length)}")
lengthnumber = int(length)
print(f"type of lengthnumber is : {type(lengthnumber)}")
lengthnumber = float(length)
print(f"type of lengthnumber is : {type(lengthnumber)}")

#slice string
msg="hello every body"
hello=msg[0:11]
print(hello)

greet="hello to me"
print(greet[0:8])