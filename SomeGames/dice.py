import random

user_input = 'none'
while user_input != 'TAIP' or user_input != 'T':
    user_input = (input('Ridenti Kauliuka?(T, N):')).upper()

    if user_input == 'T':
        outcome = random.randint(1,6)
        print('Isridenote',(outcome))
        continue
    else:
        print('Aciu uz zaidima')
        break