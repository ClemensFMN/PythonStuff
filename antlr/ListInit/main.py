import sys
from antlr4 import *
from ListInitLexer import ListInitLexer
from ListInitParser import ListInitParser
from ListInitListener import ListInitListener
from ListInitVisitor import ListInitVisitor

class MyListener(ListInitListener):
    def exitOneInt(self, ctx:ListInitParser.OneIntContext):
        print(ctx.INT())

    def exitTwoInt(self, ctx:ListInitParser.TwoIntContext):
        print(ctx.INT(0))
        print(ctx.INT(1))


class MyVisitor(ListInitVisitor):
    def visitOneInt(self, ctx:ListInitParser.OneIntContext):
       print(ctx.INT())
       return self.visitChildren(ctx)

    def visitTwoInt(self, ctx:ListInitParser.TwoIntContext):
        print(ctx.INT(0))
        print(ctx.INT(1))
        return self.visitChildren(ctx)



def main():
    input_stream = FileStream('inp.txt')
    lexer = ListInitLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ListInitParser(stream)
    tree = parser.stat()
    # print(tree.toStringTree())
    
    # option 1: using a listener
    ml = MyListener()
    pwt = ParseTreeWalker()
    pwt.walk(ml, tree)
    
    #option 2: using a visitor
    mv = MyVisitor()
    mv.visit(tree)

if __name__ == '__main__':
    main()


