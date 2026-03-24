message = "   Hello every body "
print(f"message before any methods: \"{message}\"")

result = message.capitalize()
print(f"message after any capitalize: \"{result}\"")

result = message.upper()
print(f"message after any upper: \"{result}\"")

result = message.casefold()
print(f"message after any casefold: \"{result}\"")

result = message.lower()
print(f"message after any lower: \"{result}\"")

result = message.title()
print(f"message after any title: \"{result}\"")

position  = message.find("Hello")
print(f"position of \"hello\"inside message is:\"{position}\"")


position  = message.find("bye")
print(f"position of \"bye\"inside message is:\"{position}\"")

position  = message.find("Hello",6,10)
print(f"position of \"hello\"inside message is:\"{position}\"")

#using index method
position  = message.index("Hello")
print(f"position of \"hello\"inside message is:\"{position}\"")

position  = message.index("Hello",0,10)
print(f"position of \"hello\"inside message is:\"{position}\"")


#strip--------------------
result = message.strip()
print(f"message after strip:\"{result}\"")

result = message.rstrip()
print(f"message after rstrip:\"{result}\"")

result = message.lstrip()
print(f"message after lstrip:\"{result}\"")

#------------replace---------------
result = message.replace("Hello","hi")
print(f"message after replace:\"{result}\"")

#---------new msg-----------
message2 = " hi hi everbody hi to you"
result2 = message2.replace("hi","hello",2)
print(f"message after replace:\"{result2}\"")

message3 = " hi, everybody , how are you, bye"
result3 = message3.split(",")
print(result3)

result3 = message3.split(",",2)
print(result3)