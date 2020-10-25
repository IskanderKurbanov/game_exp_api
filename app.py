import os

from game import game

os.system('clear')
print('game run')

if __name__ == '__main__':
    finish = False
    while not finish:
        command = input('>> ')
        game.run_game(command)
