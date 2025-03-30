# typecasting = changing the data type of a value


text_number = "100"

print("TypeCasting")

# print(type(text_number))
# print(type(int(text_number))) # turn the string into an int


print(type(float("3.1416"))) # turns the string into a float
print(type(int(3.1416)))

print(bool(3))
print(bool(0)) # the only numerical value that equals to False is zero even 
print(bool(-1)) # negative numbers equal to True


print(bool("")) # empty string equals to false
print(bool(" ")) # the space is counted as a character so in this case even is the string is "empty" this would return True
print(bool("hello"))

#print(int("hello how are you")) can't turn these characters into numbers, only string numbers "123" this dont return NaN it just throws an Error


print(int(4.7)) # eliminates the numbers after the point so it would return 4 is not doing any rounding operations
