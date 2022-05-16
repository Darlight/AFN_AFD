"""
Universidad del Valle de Guatemala
nodes.py
Proposito: Representaciones de simbolos
Mario Perdomo 18029
"""

#  A diferencia de la primera entrega, se establecio utilizar nodos en vez de strings en los estados de aceptacion
class Letter():
    def __init__(self, value) -> None:
        self.value = value
    def __repr__(self) -> str:
        return f'{self.value}'


class Append():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f'({self.a}.{self.b})'
        
class Or():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f'({self.a}|{self.b})'
        
class Kleene():
    def __init__(self, a) -> None:
        self.a = a
    def __repr__(self) -> str:
        return f'{self.a}*'

class Plus():
    def __init__(self, a) -> None:
        self.a = a
    def __repr__(self) -> str:
        return f'{self.a}+'

class Question():
    def __init__(self, a) -> None:
        self.a = a
    def __repr__(self) -> str:
        return f'{self.a}'

class Expression():
    def __init__(self, a, b=None) -> None:
        self.a = a
        self.b = b
    def __repr__(self) -> str:
        if self.b != None:
            return f'{self.a}{self.b}'
        return f'{self.a}'