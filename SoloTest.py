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

# #FizzBuzz
# n = int(input("Enter the number for FizzBuzz: "))
# for x in range(1, n):
#     if x % 2 == 0:
#         continue
#     elif x % 3 == 0 and x % 5 == 0:
#         print("SoloLearn")
#     elif x % 3 == 0:
#         print("Solo")
#     elif x % 5 == 0:
#         print("Learn")
#     else:
#         print(x)
#         continue
########################################################

# Read content from file and then return book codes(First char of title + lenght)
file = open("D:\Mokslai\GitHub\PyLearn\Movies.txt", "r")
# cont = file.read
for line in file:
    line = line.strip("\n")
    ch = len(line)
    print(line[0] + str(ch))
file.close()