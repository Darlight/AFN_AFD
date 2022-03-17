"""
Universidad del Valle de Guatemala
CC----
thompson.py
Proposito: clase de un estado usando la construccion de thompson
"""
#Thompson's Construction 
class Thompson:
    def __init__(self):
        self.constructor = {
            'CHAR':self.handle_char, # [a-z]
            'CONCAT':self.handle_concat, #[?]
            'ALT':self.handle_alt, # [|]
            'STAR':self.handle_rep,# [*]
            'PLUS':self.handle_rep,# [+]
            'QMARK':self.handle_qmark }# [?]}

print(" whatever this is:" +  "\x08")

print("\x3F" == "?")