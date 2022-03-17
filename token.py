"""
Universidad del Valle de Guatemala
CC----
thompson.py
Proposito: Lexema/leyenda de los inputs ingresados
"""

class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name + ":" + self.value