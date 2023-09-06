# Create variables john_salary and marta_salary of some type (floating point). Assign the created variables
# the values you want. Print the values of both variables to the console using the print method.
john_salary = 1000.99
marta_salary = 1500.75

print(john_salary)
print(marta_salary)

# Create variables john_age and marta_age of integer type. Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.
john_age = 25
marta_age = 35

print(john_age)
print(marta_age)

# Create string type variables john_name and marta_name. Assign the created variables the values you want.
# Print the values of both variables to the console using the print method.
john_name = "John Newman"
marta_name = "Marta Silva"

print(john_name)
print(marta_name)

# Create boolean variables john_gender and marta_gender. Let john be false and Marta be true.
# Print the values of both variables to the console using the print method.
john_gender = False
marta_gender = True

print(john_gender)
print(marta_gender)

if john_gender:
    print("Hello John")
if marta_gender:
    print("Hello Marta")

# Create variables john_friends and marta_friends. Assign lists to variables.
# Each list must contain the names of friends. John has his list of friends and Martha has hers.
# Friends (friend's name) can be the usual strings "James", "Peter", etc.
john_friends = ["Viktoria", "Vlad", "Andrii"]
marta_friends = ["Maria", 'Dasha', "Alina"]

print(john_friends)
print(marta_friends)

# Create a list with people's names, some names should be repeated in it.
# Turn a list of duplicate names into a list of unique names using sets.
people_names = ["Viktor", "Kate", "Irina", "Yuliia", "Viktor", "Irina"]
new_people_names = set(people_names)
print(new_people_names)
