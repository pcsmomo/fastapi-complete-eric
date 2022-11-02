"""
Boolean and Operators
"""

like_coffee = True
like_tea = False

favorite_food = "Pizza"
favorite_number = 32
print(type(like_coffee))
print(type(favorite_food))
print(type(favorite_number))

# Comparison Operators
print(f'1 == 2 : ' + str(1 == 2))
print(f'1 != 2 : ' + str(1 != 2))
print(f'1 > 2 : ' + str(1 > 2))
print(f'1 < 2 : ' + str(1 < 2))
print(f'1 >= 1 : ' + str(1 >= 1))
print(f'1 <= 2 : ' + str(1 <= 2))


# Logical Operators
print(1 > 3 and 5 < 7)
print(1 > 3 or 5 < 7)
print(not (1 == 1))
