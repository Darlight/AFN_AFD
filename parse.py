"""
Universidad del Valle de Guatemala
parse.py
Proposito: Orden y consumo de los inputs
"""
from regex import W
from lexer import Lexer
from tokenTypes import typeToken
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.Next()

    def Next(self):
        try:
            self.curr_token = next(self.tokens)
        except StopIteration:
            self.curr_token = None
    
    def newSymbol(self):
        token = self.curr_token

        if token.type == typeToken.L_PAREN:
            self.Next()
            res = self.Expression()

            if self.curr_token.type != typeToken.R_PAREN:
                raise Exception('No right Parenthesis for expression!')
            
            self.Next()
            return res
        elif token.type == typeToken.LETTER:
            self.Next()
            return Letter(token.value)
    def newOperator(self):
        res = self.newSymbol()

        while self.curr_token != None and \
        (
                self.curr_token.type == typeToken.KLEENE or
                self.curr_token.type == typeToken.PLUS or
                self.curr_token.type == typeToken.QUESTION
        ):
            if self.curr_token.type == typeToken.KLEENE:
                self.Next(
                    res = Kleene(res)
                )
            elif self.curr_token.type == typeToken.PLUS:
                self.next(
                    res = Plus(res)
                )
            else:
                self.Next()
                res = Question(res)
        return res
    def expression(self):
        res = self.newOperator()
        
        while self.curr_token != None and \
            (
                self.curr_token.type == typeToken.APPEND or
                self.curr_token.type == typeToken.OR
            ):
            if self.curr_token.type == typeToken.OR:
                self.Next()
                res = Or(res, self.newOperator())

    def parse(self):
        print("missin")
    """
    def parse(self):
        self.exp()
        return self.tokens
    
    def consume(self, name):
        if self.next_token.name == name:
            self.next_token = self.lexer.get_token()
        elif self.next_token.name != name:
            pass
    #orden de jerarquia, los parentesis son priorirdad #1
    def primary(self):
        if self.next_token.name == 'LEFT':
            self.consume('LEFT')
            self.exp()
            self.consume('RIGHT')
        elif self.next_token.name == 'CHAR':
            self.tokens.append(self.next_token)
            self.consume('CHAR')
    #Esto permite que vaya leyendo la expresion desde el primer parentesis
    # ademas, 
    def term(self):
        self.factor()
        if self.next_token.value not in ')|':
            self.term()
            self.tokens.append(Token('CONCAT', '\x08'))
        
    def exp(self):
        self.term()
        if self.next_token.name == 'ALT':
            t = self.next_token # t = token
            self.consume('ALT')
            self.exp()
            self.tokens.append(t)

    
    def factor(self):
        self.primary()
        # Las divisiones para cada AFN se clasifican desde aqui
        if self.next_token.name in ['STAR', 'PLUS', 'QMARK']:
            self.tokens.append(self.next_token)
            self.consume(self.next_token.name)
"""
    