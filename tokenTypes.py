"""
Universidad del Valle de Guatemala
tokenTypes.py
Proposito: Token
Mario Perdomo 18029
"""

from enum import Enum

# ===== Classifier Class =====
class typeToken(Enum):
    LETTER = 0
    APPEND = 1
    OR = 2
    KLEENE = 3
    PLUS = 4
    QUESTION = 5
    L_PAREN = 6
    R_PAREN = 7
 
# ====== Token =====
class Token:
    def __init__(self, type: typeToken, value = None):
        self.type = type
        self.value = value
        self.precedence = type.value

    def __repr__(self):
        return f'{self.type.name}: {self.value}'