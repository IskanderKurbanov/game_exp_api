import os

from creatures import Creature

os.system('clear')
print('game run')


npc = Creature('Ivan')

npc.say()
npc.say('Who I am?')
