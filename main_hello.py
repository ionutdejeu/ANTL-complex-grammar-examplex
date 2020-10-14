
from antlr4 import *
from gen.helloLexer import helloLexer
from gen.helloListener import helloListener
from gen.helloParser import helloParser
import sys

class HelloPrintListener(helloListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = helloLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = helloParser(stream)
    tree = parser.hi()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()