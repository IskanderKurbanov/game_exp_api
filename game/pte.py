import re
import random
import os
from .creature import Knight


class Pte:
    #This class my mistake(rewrite this class later)
    
    def __init__(self):
        os.system('clear')
        
        self.logs = 'game begin'
        
        self.stop_game = False
        self.my_hp = 100
        self.inventory = {'heal_posion': 5}
        
        self.create_enemy()
    
    
    def parse(self, command: str) -> list:
       #parse recieved strings to list
       cmd = command.split(' ')
       return cmd


    def cmd_parser(self, cmd: list):
        if 'exit' in cmd:
            os.system('clear')
            exit()
        if 'fight' in cmd:
            self.fight_action()
        if 'heal' in cmd:
            self.drink_posion('heal_posion')
    
    
    def create_enemy(self):
        #this method create some person lol
        i = random.randint(1,10)
        name = f'knight#{i}'
        self.person = Knight(name, i, 100)
        
    
    def create_player(self):
        pass
        
        
    def fight_action(self):
        ya = random.randint(1,10)
        ea = self.person.attack()
        self.person.hp -= ya
        self.my_hp -= ea
        self.logs = f'your attack: {ya}\n {self.person.name} attacked you to {ea}'
        
    
    def drink_posion(self, posion):
        self.logs = f'you drink {posion}'
        self.inventory['heal_posion'] -= 1
        self.my_hp += 20
    
    
    def get_info(self):
        self.person.info()
        print(f'====commands:====\nexit: close game\nfight: fight with aponent')
        print(f'====inventory====\nhp posion: {self.inventory["heal_posion"]}')
        print(f'=================\nmy hp: {self.my_hp}')
        
    
    def print_logs(self):
        print('\n',self.logs,'\n')


    def run_game(self):
        while  not self.stop_game:
            if self.my_hp <= 0:
                self.game_over('lose')
            self.get_info()
            self.print_logs()
            command = input('>> ')
            cmd = self.parse(command)
            self.cmd_parser(cmd)
            os.system('clear')
            
    
    def game_over(self, stat):
        print('lol you died')
        exit()

        


