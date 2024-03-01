# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:28:09 2023

@author: 700001473
"""



class TuringMachine:

    def __init__(self, prog):
        self.prg = prog # a dict of tuples (write, MoveTape, nextState)
        
        # the tape is a dict holding the values
        self.tape = {}

        self.curState = 1
        self.curPos = 0

    def oneStep(self):
        # fetch the next instruction based on the current state
        self.curInst = self.prg[self.curState]

        # write to the tape
        self.wr = self.curInst[0]
        self.tape[self.curPos] = self.wr

        # move position
        self.nxtPos = self.curInst[1]
        if self.nxtPos == 'R':
            self.curPos += 1
        else:
            self.curPos -= 1

        # get next state
        self.curState = self.curInst[2]
        if(self.curState == -1):
            return(-1)
        else:
            return(0)

    def run(self, n = 10):
        self.tape_snapshots = []
        for _ in range(n):
            self.res = self.oneStep()
            self.tape_snapshots.append(self.tape.copy())
            if(self.res == -1):
                break
        return(self.tape_snapshots)


# a dict of tuples (write, MoveTape, nextState)
# prg = {1: (1,'R',2), 2: (0,'R',1)}
prg = {1: (1,'R',2), 2: (0,'R',-1)}
tm = TuringMachine(prg)
# tm.oneStep()
ts = tm.run(10)


