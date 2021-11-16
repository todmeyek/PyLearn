# import random
# guess = 0
# num = random.randint(1, 9)
# while guess != num:
#     guess = int(input('Guess the number from 1 to 9: '))
#     if guess != num:
#         print('sorry you are wrong, try again: ')
#     else:
#         print('You are right')

# better way below        
import random
guess = 0
num = random.randint(1, 9)
while guess != num:
    guess = int(input('Guess the number from 1 to 9: '))
print('you are right')
