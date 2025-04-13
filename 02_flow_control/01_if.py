# conditionals (if, elif, else)
# allows executions of code only if a condition is met

# if
age = 17
if age >= 18:
    print("You are allowed to enter")
else:
    print("Sorry you are not allowed to enter :(")

# elif and else
grade = 5
if grade >= 9:
    print("Excellent")
elif grade >= 7:
    print("Good")
elif grade >= 5:
    print("Enough")
else:
    print("Failed")


# multiple conditionals
age = 22
has_license = True

if age >= 18 and has_license == True:
    print("Can drive")
elif age < 18 and has_license == False:
    print("Can't drive")