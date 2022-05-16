"""
Universidad del Valle de Guatemala
checkInput.py
Proposito: Checks the user's input for expressions
Mario Perdomo 18029
"""
from tokenTypes import *

RAW_LETTERS = 'abcdefghijklmnopqrstuvwxyz0123456789'

class Checker:
    def __init__(self, string: str) -> None:
        self.string = iter(string.replace(' ', ''))
        self.input = set()
        self.Next()
    
    def Next(self):
        try:
            self.curr_char = next(self.string)
        except StopIteration:
            self.curr_char = None
    
    def createTokens(self):
        while self.curr_char != None:
            if self.curr_char in RAW_LETTERS:
                self.input.add(self.curr_char)
                yield Token(typeToken.L_PAREN, '(')
                yield Token(typeToken.LETTER, self.curr_char)

                self.Next()

                add_paren = False
                while self.curr_char != None and \
                    (self.curr_char in RAW_LETTERS or self.curr_char in '*+?'):

                    if self.curr_char == '*':
                        yield Token(typeToken.KLEENE, '*')
                        yield Token(typeToken.R_PAREN, ')')
                        add_paren = True
                    elif self.curr_char == '+':
                        yield Token(typeToken.PLUS, '+')
                        yield Token(typeToken.R_PAREN, ')')
                        add_paren = True
                    elif self.curr_char == '?':
                        yield Token(typeToken.QUESTION, '*')
                        yield Token(typeToken.R_PAREN, ')')
                        add_paren = True
                    elif self.curr_char in RAW_LETTERS:
                        self.input.add(self.curr_char)
                        yield Token(typeToken.APPEND)
                        yield Token(typeToken.LETTER, self.curr_char)
                        add_paren = True
                    self.Next()
                    
                    if self.curr_char != None and self.curr_char == '(' and add_paren:
                        yield Token(typeToken.APPEND)

                if self.curr_char != None and self.curr_char == '(' and not add_paren:
                    yield Token(typeToken.R_PAREN, ')')
                    yield Token(typeToken.APPEND)

                elif not add_paren:
                    yield Token(typeToken.R_PAREN, ')')    
                    
            elif self.curr_char == '|':
                self.Next()
                yield Token(typeToken.OR, '|')   

            elif self.curr_char == '(':
                self.Next()
                yield Token(typeToken.L_PAREN)

            elif self.curr_char in (')*+?'):

                if self.curr_char == ')':
                    self.Next()
                    yield Token(typeToken.R_PAREN)
                elif self.curr_char == '*':
                    self.Next()
                    yield Token(typeToken.KLEENE)
                elif self.curr_char == '+':
                    self.Next()
                    yield Token(typeToken.PLUS)
                elif self.curr_char == '?':
                    self.Next()
                    yield Token(typeToken.QUESTION)
                
                if self.curr_char != None and \
                    (self.curr_char in RAW_LETTERS or self.curr_char == '('):
                    yield Token(typeToken.APPEND, '.')
            else: 
                raise Exception(f'Invalid entry: {self.curr_char}. Please check your expression. ')
            
    def getSymbols(self):
        #Shows all the symbols to the checker right now
        return self.input
         
                    
