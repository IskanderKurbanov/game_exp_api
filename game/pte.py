import random
import os
from .creature import Human


class Pte:
    #This class my mistake(rewrite this class later)
    
    def __init__(self):
        os.system('clear')
        self.logs = 'Game begin'
        self.stop_game = False
    
    
    def parse(self, command: str) -> list:
       #parse recieved strings to list
       cmd = command.split(' ')
       return cmd


    def cmd_parser(self, cmd: list):
        if 'exit' in cmd or 'q' in cmd:
            os.system('clear')
            exit()
        if 'attack' in cmd or 'a' in cmd:
            self.fight_action()
        if 'heal' in cmd or 'h' in cmd:
            self.drink_posion('heal_posion')
    
    
    def create_enemy(self):
        #this method create some person lol
        max_lvl = self.player.lvl
        i = random.randint(self.player.lvl, max_lvl+5)
        self.person = Human(f'knight#{i}', 'knight', i, 100)
        
    
    def create_player(self):
        name = input('==Create your hero==\nenter your name: ')
        self.player = Human(name, 'hero', 1, 100)
        self.player.up_lvl(4)
        os.system('clear')
        
        
    def fight_action(self):
        ya = self.player.get_damage()
        ea = self.person.get_damage()
        self.person.hp -= ya
        self.player.hp -= ea
        self.logs = f'your attack: {ya}\n {self.person.name} attacked you to {ea}'
        
    
    def drink_posion(self, posion: str):
        if self.inventory[posion] > 0:
            self.inventory[posion] -= 1
            self.logs = f'you drink {posion}'
            if posion == 'heal_posion':
                self.player.hp += 20
        else:
            self.logs = f'Oh no, you dont have {posion}'
    
    
    def get_info(self):
        self.person.info()
        print(f'====commands:====\n(q)exit: close game\n(a)attack: fight with aponent\n(h)heal: drink heal posion')
        self.player.info()
        
    
    def print_logs(self):
        print('\n',self.logs,'\n')


    def run_game(self):
        self.create_player()
        self.create_enemy()
        self.game_loop()
            
    
    def game_loop(self):
        while  not self.stop_game:
            print('this game is not work now(((')
            if self.player.hp <= 0:
                self.game_over('lose')
            if self.person.hp <= 0:
                self.logs=f'{self.person.name} is dead'
                self.player.lvl = self.player.up_lvl(1)
                self.create_enemy()
            self.get_info()
            self.print_logs()
            command = input('>> ')
            cmd = self.parse(command)
            self.cmd_parser(cmd)
            os.system('clear')
    

    def game_over(self, stat):
        print('lol you died')
        exit()

        


