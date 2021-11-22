# Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output:
# Number of even numbers: 5
# Number of odd numbers: 4

num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
od = 0
for i in num:
    if not i % 2:
        even += 1
    else:
        od += 1
print(even)
print(od)
