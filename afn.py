"""
Universidad del Valle de Guatemala
CC----
thompson.py
Proposito: AFN ya establecido
"""

class AFN:
    def __init__(self, start, end):
        self.start = start
        self.end = end # start and end states
        end.is_end = True
    
    #Recursion                          \      afn n veces /
    #state-set es como un stack -->      \       afn1     /
    #                                     \______afn0____/ 
    def addstate(self, state, state_set): # add state + recursively add epsilon transitions
        if state in state_set:
            return
        state_set.add(state)
        for eps in state.epsilon:
            self.addstate(eps, state_set)
    
    