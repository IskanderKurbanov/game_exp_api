import random

class Creature:
    '''
    This class parent of all creatures
    '''
    
    def __init__(self):
        #self.alive = True
        pass


    def info(self):
        print(f'===={self.name}====')
        print(f'lvl: {self.lvl}')
        print(f'hp: {self.hp}')
        print(f'~skills:{self.skills}')
        print(f'~inventory:{self.inventory}')


class Human(Creature):

    
    def __init__(self, name:str='knight', fate:str = 'man', lvl:int=1, hp:int=100):
        self.name = name
        self.fate = fate
        self.lvl = lvl
        self.hp = hp # human attr
        self.skills = {
            'strenght': 1,
            'intellect': 1,
            'luck':1,
            }
        self.inventory = { # human attr
            'heal_posion': 5,
            'berserk_posion': 2
            }
        
    
    def get_damage(self) -> int:
        attack = random.randint(1, self.lvl*self.skills['strenght'])
        return attack
    
    
    def up_lvl(self, number_of_lvl:int) -> int:
        self.lvl += number_of_lvl
        for i in range(number_of_lvl):
            print(f'====choise skill({i+1})===')
            for j in self.skills:
                print(f'({j[:1]}) {j}')
            next_lvl = input('>>')
            for k in self.skills:
                if next_lvl == k[:1]:
                    self.skills[k]+=1
                    
                    