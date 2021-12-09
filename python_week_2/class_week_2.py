# List vs. Dictionary

# List
person_one = [ "Rob", 'Y', "Purple", True, 3 ]
# print(person_one[2])

# Dictionaries
person_two = {
    # Key : Value - Key Value Pair
    "name" : "Rob", #String
    "age" : 45,
    "food_truck" : True,
    "items" : ["apple pie", "pumpkin pie", "peach pie"] # List
}

print(person_two["items"][2])
print(person_two['age'])
person_two['loves dogs'] = True
print(person_two)
person_two['food_truck'] = False
print(person_two)
person_two['items'][0] = "apple crisp"
print(person_two)

person_three = {}
person_three['name'] = 'Michael'
print(person_three)

person_one[0] = 'Sebuh'
print(person_one)

person_two = {
    # Key : Value - Key Value Pair
    "name" : "Rob", #String
    "age" : 45,
    "food_truck" : True,
    "items" : ["apple pie", "pumpkin pie", "peach pie"] # List
}

# Removing Values - Pop vs. Del
value_remove = person_two.pop('age') # Pop returns the value that is deleted
print(value_remove)

del person_two['age'] # del does not return anything

# Key of Keys
print(person_two.keys())

# Val of Values
print(person_two.values())

# Keys and Values
print(person_two.items())

# Conditionals

x = 24

if x > 50:
    print("Bigger than 50")
elif x > 40:
    print("Bigger than 40")
elif x > 30:
    print("Bigger than 30")
else:
    print("Less than 50")

birds = {
    "Minnesota" : "Mosquito",
    "Illinois" : "Northern Cardinal",
    "Hawaii" : "Nene",
    "Vermont" : "Hermit Thrush",
    "Tennessee" : "bobwhite quail",
}

for key in birds.keys():
    print(key)

for val in birds.values():
    print(val)

for key, val in birds.items():
    if key == "Minnesota":
        print('Bring BUG Spray')
    # print(key, val)
    print(key, " = ", val)

# Functions

def sum(num):
    num += 1
    return num

print(sum(7))

def function_name():
