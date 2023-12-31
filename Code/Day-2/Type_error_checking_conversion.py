# object of type "int" has no len() function.
#len(12345) => TypeErroe
#Concatination works only for str to str.
num_char=len(input("What is your name ?"))
print(type(num_char))
#converting string to integer and concatinate
new_int_char = str(num_char)
print("your name has" + new_int_char + "charecters.")