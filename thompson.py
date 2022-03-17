"""
Universidad del Valle de Guatemala
CC----
thompson.py
Proposito: clase de un estado usando la construccion de thompson
"""
#Thompson's Construction 

#Referencia
SPECIAL = "*|ε+"


#  {a, b, ε}

class State:
    def __init__(self, name):
        self.epsilon = [] #estados vacios
        #Transiciones del input y haciua el siguiuente estado
        self.transitions = {} 
        self.name = name
        self.is_end = False # True --> estado final

class ManejadorEspecial:
    def __init__(self):
        self.manejador = {'CHAR':self.handle_char, 'CONCAT':self.handle_concat,
                         'ALT':self.handle_alt, 'STAR':self.handle_rep,
                         'PLUS':self.handle_rep, 'QMARK':self.handle_qmark}