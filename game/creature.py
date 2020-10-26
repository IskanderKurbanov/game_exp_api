import random

class Creature:
    '''
    This class parent of all creatures
    '''
    
    def __init__(self):
        #self.alive = True
        pass


    def info(self):
        print('======enemy======')
        print(f'name: {self.name}\nlvl: {self.lvl}\nhp: {self.hp}')


class Human(Creature):
    pass


class Knight(Human):
    
    def __init__(self, name:str='knight', lvl:int=1, hp:int=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        
    
    def attack(self):
        attack = random.randint(1, self.lvl*2)
        return attack
        
    