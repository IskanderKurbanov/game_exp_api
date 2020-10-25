print(__name__)

class Creature:
    '''
    This class parent of all creatures
    '''

    def info(self):
        print(f'name {self.name} \nlvl {self.lvl}')


class Human(Creature):
    
    def __init__(self, name:str='', lvl:int=1, hp:int=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    