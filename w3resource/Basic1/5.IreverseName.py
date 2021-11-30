# 1 Method
# name = input("Your name?")
# vorname = input("your vorname?")
# print( "Hello Mr. " + vorname + " " + name)

# 2 Method
# namevorname = input("Your Name and vorname: ")
# namevornamelist = namevorname.split(" ")
# revlist = reversed(namevornamelist)
# print(list(revlist))

# 3 Method
# x = input("Your Name and vorname: ")
# y = x.split(" ")
# for item in reversed(y):
#     print (item)

# 4 Method
# x = input("Your Name and vorname: ")
# y = x.split(' ')
# y.reverse()
# print(" ".join(y))

# 5 Method
x = input("Your Name and vorname: ")
print(" ".join(x.split(' ')[::-1]))
