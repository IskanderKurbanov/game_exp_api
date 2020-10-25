import re
import random
from .creature import Human


class Pte:
    '''
    This class my mistake
    (rewrite this class later)
    '''
    
    def parse(self, command: str) -> list:
       '''
       parse recieved strings to list

       '''
       cmd = command.split(' ')
       #print(cmd, type(cmd))
       return cmd

    def cmd_parser(self, cmd: list):
        if 'info' in cmd:
            self.get_info()
    
    def create_person(self):
        i = random.randint(1,10)
        name = f'boy#{i}'
        self.person = Human(name, 1, 100)
    
    def get_info(self):
        self.person.info()


    def run_game(self, command:str):
        cmd = self.parse(command)
        self.cmd_parser(cmd)
        self.create_person()


