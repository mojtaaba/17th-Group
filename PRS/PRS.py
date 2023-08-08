import random

player = input('please do your move: ')
computer = random.randint(1, 3)

if computer == 1:
    computer_move = 'paper'
if computer == 2:
    computer_move = 'stone'
if computer == 3 :
    computer_move = 'scissors'

if player == computer_move:
    print(f'player: {player} and computer: {computer_move}')
    print('repeat')

elif player == 'stone' and computer_move == 'scissors':
    print(f'player: {player} and computer: {computer_move}')
    print('Player Won!')

elif player == 'stone' and computer_move == 'paper':
    print(f'player: {player} and computer: {computer_move}')
    print('computer Won!')

elif player == 'paper' and computer_move == 'stone' :
    print(f'player: {player} and computer: {computer_move}')
    print('player Won!')

elif player == 'paper' and computer_move == 'scissors':
    print(f'player: {player} and computer: {computer_move}')
    print('computer won!')

elif player == 'scissors' and computer_move == 'paper':
    print(f'player: {player} and computer: {computer_move}')
    print('player Won!')

elif player == 'scissors' and computer_move == 'stone':
    print(f'player: {player} and computer: {computer_move}')
    print('computer Won!')
else:
    print('wrong!!!!')