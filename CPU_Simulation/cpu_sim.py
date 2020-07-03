# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 09:09:41 2015

@author: clnovak
"""

class Memory():
    """ class for modelling memory
    a bit simplified, as we can write data of arbitrary size on one address
    so a command as e.g. LA 5 is stored on one address
    as is a command like IA"""
    def __init__(self):
        """initialze the memory"""
        # memory size
        self.N = 20
        self.storage = self.N*[0]
        # a symbol table storing symbol name -> address
        self.symboltable = {}

    def read(self, addr):
        """read value from memory addr"""
        return self.storage[addr]
    
    def write(self, addr, val):
        """write value to memory addr"""
        self.storage[addr] = val

    def load(self, filename):
        """load instructions / data from file
        labels are removed, in call commands the label is replaced by an address
        from the symbol table"""
        f = open(filename, "r")
        file_lines = f.readlines()
        
        for (addr, line) in enumerate(file_lines):
            # remove labels
            if(line.startswith("@")):
                s = line.split()
                self.write(addr, "".join(s[1:]))
            # in call commands, replace the label with the address
            elif(line.startswith("CALL")):
                s = line.split()
                # lookup symbol and convert to address
                s[1] = str(self.symboltable[s[1]])
                # build the new command together
                s = " ".join(s)
                # and write into memory
                self.write(addr, s)
            else:
                # default behaviour is to simply write the string into memory
                self.write(addr, line)

    def fill_symbol_table(self, filename):
        """the new shiny version with 2 pass parsing"""
        f = open(filename, "r")
        file_lines = f.readlines()

        # go through the file and fill the symbol table
        for (addr, line) in enumerate(file_lines):
            if(line.startswith("@")):
                s = line.split()
                self.symboltable[s[0]] = addr

    def dump(self):
        """dump the complete memory for debugging purposes"""
        print self.symboltable
        for (addr, val) in enumerate(self.storage):
            print addr, val


class CPU():
    """CPU model; simple CPU with accumulator, program counter and data pointer"""
    def __init__(self, mem):
        # initialze acc, pc and assign memory
        self.acc = 0
        self.dp = 0
        self.pc = 0
        self.sp = mem.N-1
        self.memory = mem

    def execute(self):
        """execute one command; i.e. fetch command from memory, decode and execute"""
        # load memory from address pc points to
        s = self.memory.read(self.pc)
        print(s)
        # execute current command
        s = s.split()
        # the command itself
        cmd = s[0]
    
        if cmd == "XX":
            return False

        if cmd == "SA":
            # set accumulator
            self.acc = int(s[1])
            self.pc = self.pc + 1

        if cmd == "IA":
            # increase accumulator
            self.acc = self.acc + 1
            self.pc = self.pc + 1

        if cmd == "DA":
            # decrease accumulator
            self.acc = self.acc - 1
            self.pc = self.pc + 1

        if cmd == "SD":
            # set data pointer
            self.dp = int(s[1])
            self.pc = self.pc + 1

        if cmd == "ID":
            # increase data pointer
            self.dp = self.dp + 1
            self.pc = self.pc + 1

        if cmd == "DD":
            # decrease data pointer
            self.dp = self.dp - 1
            self.pc = self.pc + 1

        if cmd == "ST":
            # store accu @ location dp points to
            self.memory.write(self.dp, self.acc)
            self.pc = self.pc + 1

        if cmd == "LD":
            # load accu from location dp points to
            self.acc = self.memory.read(self.dp)
            self.pc = self.pc + 1

        if cmd == "JP":
            # unconditional jump
            offset = int(s[1])
            self.pc = self.pc + offset

        if cmd == "JZ":
            # conditional jump if acc == 0
            offset = int(s[1])
            if self.acc == 0:
                self.pc = self.pc + offset
            else:
                self.pc = self.pc + 1

        if cmd == "CALL":
            """call subroutine"""
            # store current pc on stack
            self.memory.write(self.sp, self.pc)
            # decrease stack pointer
            self.sp = self.sp - 1
            # and prepare jump
            self.pc = int(s[1])

        if cmd == "RET":
            """return from subroutine"""
            # decrease stack pointer            
            self.sp = self.sp + 1
            # and prepare jump by loading the stored pc and increase by 1 => upon
            # return from the subroutine, the CPU continues with the next statement
            # i.e. the one after the call instruction.
            self.pc = self.memory.read(self.sp) + 1

        return True

    def run(self):
        """run the cpu till the halt execution is reached"""
        while(self.execute()):
            self.dump()

    def dump(self):
        """dump CPU registers"""
        print "A = ", self.acc, "DP = ", self.dp , "PC = ", self.pc, "SP = ", self.sp
        #print self.memory.dump()



m = Memory()
# m.load("prog_02.cmd")
m.fill_symbol_table("prog_03.cmd")
m.load("prog_03.cmd")
m.dump()

c = CPU(m)
c.run()
m.dump()
