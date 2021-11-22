# Sum of all numbers
# N = int(input("Enter number for sum: "))
# sum = 0

# for n in range (0, N+1, 1):
#     sum = sum + n
# print("Sum of all numbers is: ", sum)

########################################################


# Search Word in text
# text = input("Enter Text: ")
# word = input("Enter keyword: ")

# def search(text, word):
#     if word in text:
#         print("Word found")
#     else:
#         print("Word not found")

# search(text, word)
########################################################

#FizzBuzz
n = int(input("Enter the number for FizzBuzz: "))
for x in range(1, n):
    n = -1
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
        continue
    