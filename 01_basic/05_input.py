###
# User input 
# the input() function allows us to get user data through the console 
###

name = str(input("What's your name: ")) # if we dont specify the data type of the input it will always return a string
print(f"hello {name} nice meting you")

age = int(input("How old are you: "))
print(f"in 10 years you'll have {age + 10}")