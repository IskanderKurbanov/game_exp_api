print(__name__)

class Creature:

    def __init__(self, name:str='', lvl:int=1):
        self.name = name
        self.lvl = lvl


    def say(self, text:str='aaa'):
        print(text)

