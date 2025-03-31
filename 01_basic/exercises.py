###
# exercises.py
# Exercises to practice the concepts learned in the lessons.
###

from os import system
if system("clear") != 0: system("cls")

print("\nExercise 1: Print messages")
print("Write a program that prints your name and your city on separate lines.")

### Completed
name = str(input("What's your name: "))
city = str(input("City where you live: "))
print(f"Name: {name}")
print(f"City: {city}")

print("--------------")

print("\nExercise 2: Display the data types of the following variables:")
print("Use the 'type()' command to determine the data type of each variable.")
a = 15
b = 3.14159
c = "Hello world"
d = True
e = None

### Completed
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nExercise 3: Type casting")
print("Convert the string \"12345\" to an integer and then to a float.")
print("Convert the float 3.99 to an integer. What happens?")

# Completed
string = "12345"
to_int = int(string)
to_float = float(to_int)

my_float = 3.99
my_int = int(my_float)# deletes the values after the dot so it turns into a 3
print(my_int) 


print("--------------")

print("\nExercise 4: Variables")
print("Create variables for your name, age, and height.")
print("Use f-strings to print an introduction.")

name = "cl0b3r"
age = 700
height = 1.82

print(f"Hello my name is {name}, im {age} years old and my height is {height}")

### Complete here

print("--------------")

print("\nExercise 5: Numbers")
print("1. Create a variable with the number PI (without assigning it manually).")
print("2. Round the number using round().")
print("3. Perform integer division between the result and the number 2.")
print("4. The result should be 1.")


result = round(3.1416) // 2 # result = round(3.1416) / 2 would return 1.5 because round rounds to the nearest int in this case 3 3/2 = 1.5
print(result)