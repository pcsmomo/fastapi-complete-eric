"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
print(my_list)
my_list.append(1000)
print(my_list)
my_list.insert(2, 1000)
print(my_list)
my_list.remove(8)
print(my_list)
my_list.pop(0)
print(my_list)
print(my_list.count(1000))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
my_list.extend([10, 20, 30])
print(my_list)
my_list.clear()
print(my_list)

people_list = ["Eric", "Adil", "Jeff"]
print(people_list[0:2])
print(people_list[1:])
print(people_list[:3])
