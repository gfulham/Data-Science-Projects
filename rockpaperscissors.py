from random import randint

#create a list of play options
t = ['Rock', 'Paper', 'Scissors']

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
# set player to True
    player = input('Choose Rock, Paper or Scissors:\n')
    if player == computer:
        print('Draw')
    elif player == 'Rock':
        if computer == 'Paper':
            print(computer "covers" player. 'You Lose!')
        else:
            print(player 'smashes' computer. 'You Win!')
    elif player == 'Paper':
        if computer == 'Scissors':
            print(computer 'cuts' player. 'You Lose!')
        else:
            print(player 'covers' computer. 'You Win!')
    elif player == 'Scissors':
        if computer == 'Rock':
            print(computer 'Smashes' Player. 'You Lose!')
        else:
            print(player 'cuts' Computer. 'You Win!')
    else:
        print('That is not a valid play. Check your spelling and try again')

# set player value back to False to restart the loop

player = False

computer = t[randint(0,2)]


