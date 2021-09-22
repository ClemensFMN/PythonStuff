#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:00:50 2021

@author: clnovak
"""

from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from LabeledExprVisitor import LabeledExprVisitor
from antlr4 import *



class MyVisitor(LabeledExprVisitor):
    
    vars = {}
    
    def visitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        val = self.visit(ctx.expr())
        print("visitPrintExpr: {}".format(val))
    
    def visitInt(self, ctx:LabeledExprParser.IntContext):
        val = ctx.INT()
        # print("visitInt: {}".format(val))
        return(val)

    def visitId(self, ctx:LabeledExprParser.IdContext):
        id = ctx.ID().getText()
        #print("visitId: id = {}".format(id))
        val = self.vars[id]
        print("visitId: id = {} => {}".format(id, val))
        #print(type(val))
        return(val)

    def visitAssign(self, ctx:LabeledExprParser.AssignContext):
        id = ctx.ID().getText()
        val = self.visit(ctx.expr()) #.getText()
        self.vars[id] = val
        print("visitAssign: {} = {}".format(id, val))
        # print("self.vars = {}".format(self.vars))
        
    
    def visitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        left = self.visit(ctx.expr(0)).getText()
        right = self.visit(ctx.expr(1)).getText()
        #op = ctx.op.type
        #print("visitMulDiv left: {}".format(left))
        #print("visitMulDiv right: {}".format(right))
        #print("visitMulDiv op: {}".format(op))
        if(ctx.op.type == LabeledExprParser.MUL):
            res = int(left) * int(right)
        else:
            res = int(left) / int(right)
        return res
        

    def visitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        left = self.visit(ctx.expr(0)).getText()
        right = self.visit(ctx.expr(1)).getText()
        #op = ctx.op.type
        #print("visitAddSub left: {}".format(left))
        #print("visitAddSub right: {}".format(right))
        #print("visitAddSub op: {}".format(op))
        if(ctx.op.type == LabeledExprParser.ADD):
            res = int(left) + int(right)
        else:
            res = int(left) - int(right)
        return res
                
    def visitShow(self, ctx:LabeledExprParser.ShowContext):
        print("All variables in scope:")
        for nm, vl in self.vars.items():
            print('{} => {}'.format(nm, vl))

    

def main():
    input_stream = FileStream('inp.txt')
    lexer = LabeledExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(stream)
    tree = parser.prog()
    print(tree.toStringTree())
    
    
    mv = MyVisitor()
    mv.visit(tree)

if __name__ == '__main__':
    main()


