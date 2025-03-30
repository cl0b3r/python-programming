# variables save data in memory and give them a "name" 
# python is a dynamically typed language

# asign a variable 
user_name = "cl0b3r"
# print(user_name)

age = 20
print(age)

# reasingning the value
age = 32
print(age)

# Dynamic typing: the data type is determined in execution time
# doesn't have to be explicitly declared can change data type any time
# name = "alexander"
# print(type(name))

# name = 32
# print(type(name))

# f-string, since python v3.6
print(f"hello my name is {user_name}, im {age} years old")

# not recommended way to assing variables
name, age , city = "Vincent", 25, "Ontario"

# variable naming conventions
my_name = "ok" # snake_case
name = "ok"

# not recommended
MiVariableName = "not ok" # PascalCase
mivariablename = "not ok" # all lowercase

mi_variable_name_123 = "ok"

CONSTANT = 3.1416 # all uppercase indicates a constant, but python doesn't have constants

user_active: bool = True # type anotation, value can still change tho basically clickbait it serves more as a "documentation" kinda
print(user_active)

user_active = 22 # this wouldn't cause troubles 