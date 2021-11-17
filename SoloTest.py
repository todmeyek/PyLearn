# Sum of all numbers
# N = int(input("Enter number for sum: "))
# sum = 0

# for n in range (0, N+1, 1):
#     sum = sum + n
# print("Sum of all numbers is: ", sum)


# Search Word in text

text = input("Enter Text: ")
word = input("Enter keyword: ")


def search(text, word):
    if word in text:
        print("Word found")
    else:
        print("Word not found")


search(text, word)
#Test2
