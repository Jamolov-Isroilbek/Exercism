import random
import string

class Robot:
    NAMES = set()
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.name = self._name_generate()

        while self.name in Robot.NAMES:
            self.name = self._name_generate()
        Robot.NAMES.add(self.name)

    def _name_generate(self):
        name = []
        
        for _ in range(2):
            name.append( random.choice(string.ascii_uppercase))
        
        for _ in range(3):
            name.append( str( random.randint(0, 9) ) )

        return "".join(name)
