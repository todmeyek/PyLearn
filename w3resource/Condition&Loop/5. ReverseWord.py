# 1. my own method
# word = input("Enter a word: ")
# word = word[::-1]
# print("you entered:", word)

#2. site Method
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")
