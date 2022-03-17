#  {a, b, ε}
class State:
    def __init__(self, name):
        self.epsilon = [] #estados vacios
        #Transiciones del input y haciua el siguiuente estado
        self.transitions = {} 
        self.name = name
        self.is_end = False # True --> estado final