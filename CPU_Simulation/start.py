# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:06:26 2012

@author: cnovak
"""

# simple one register machine
# has an accumulator a
#     a data section (pointed to by a datapointer data_ptr)
#     a program counter pc


# Command Set:
# LA value -> load value into accumulator
# IA -> increment accu
# DA -> decrement accu
# ID -> increase data pointer
# DD -> decrease data pointer
# ST -> store accu @ data pointer location
# LD -> load accu from data pointer location
# JN relative position -> if accu != 0, increase/decrease pc by relative 
#                         position; otherwise continue with next command
# JZ relative position -> if accu = 0, increase/decrease pc by relative 
#                         position; otherwise continue with next command
# JP relative position -> unconditional jump by increase/decrease of pc by 
#                         relative position
# JEQ relative position val -> if acc = val, unconditional jump by increase/
#                              decrease of pc by relative position; otherwise 
#                              continue with next command
# JL relative position val -> if acc < val perform unconditional jump
# XX -> stop execution


def debug_print():
    print "PC = ", pc, "A = ", a, "DATA_PTR = ", data_ptr
    print "Data:", data

# the accumulator
a = 0
# initialize the data section
data = [0] * 10
# intialize the data pointer
data_ptr = 0
# initialize the program counter
pc = 0


f = open("test5.cmd", "r")
file_lines = f.readlines()

while(True):
    # get next command and split into parts
    s = file_lines[pc]
    s = s.split()
    # the command itself
    cmd = s[0]
    debug_print()
    print "******************************"
    print s

    if cmd == "LA":
        a = int(s[1])
        pc = pc + 1

    if cmd == "IA":
        a = a + 1
        pc = pc + 1

    if cmd == "DA":
        a = a - 1
        pc = pc + 1

    if cmd == "ID":
        data_ptr =  data_ptr + 1
        pc = pc + 1

    if cmd == "DD":
        data_ptr =  data_ptr - 1
        pc = pc + 1

    if cmd == "ST":
        data[data_ptr] = a
        pc = pc + 1

    if cmd == "LD":
        a = data[data_ptr]
        pc = pc + 1

    if cmd == "JP":
        offset = int(s[1])
        pc = pc + offset

    if cmd == "JN":
        offset = int(s[1])
        if a != 0:
            pc = pc + offset
        else:
	  pc = pc + 1    

    if cmd == "JZ":
        offset = int(s[1])
        if a == 0:
            pc = pc + offset
        else:
	  pc = pc + 1    

    if cmd == "JEQ":
        offset = int(s[1])
        val = int(s[2])
        if a == val:
            pc = pc + offset
        else:
	  pc = pc + 1    

    if cmd == "JL":
        offset = int(s[1])
        val = int(s[2])
        if a < val:
            pc = pc + offset
        else:
	  pc = pc + 1

    if cmd == "XX":
        break

print "finished"
