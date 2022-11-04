"""
For & While Loops
"""

my_list = [1, 2, 3, 4, 5]

for x in my_list:
    print(x)

print()
for x in range(3, 6):
    print(x)

print()
for x in my_list:
    print(x)

print()
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]
for day in my_list:
    print(f"Happy day, {day}")

print()
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print("i is now larger or equal to 5")

print()
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")
