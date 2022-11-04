"""
Dictionaries
"""


user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

user_dictionary["married"] = True

for x, y in user_dictionary.items():
    print(x, y)

print()
user_dictionary2 = user_dictionary.copy()
user_dictionary2["name"] = "Noah"
print(user_dictionary)
print(user_dictionary2)
user_dictionary2.pop("age")
print(user_dictionary2)

print()
user_dictionary3 = user_dictionary.copy()
user_dictionary3["name"] = "Noah"
print(user_dictionary)
print(user_dictionary3)

print()
user_dictionary.clear()
print(user_dictionary)

print()
del user_dictionary
print(user_dictionary)
