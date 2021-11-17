
# https://tinyurl.com/h9q2cpc 
def hangman(word): 
    wrong = 0 
    stages = ["", "________ ", "| ", "| | ", "| 0 ", "| /|\ ", "| / \ ", "| " ] 
    rletters = list(word) 
    board = ["__"] * len(word) 
    win = False 
    print("Welcome to Hangman") 
    while wrong < len(stages) - 1: print("\n") 
    msg = "Guess a letter" 
    char = input(msg) 
    if char in rletters: 
        cind = rletters \
             .index(char) board[cind] = char rletters[cind] = '
