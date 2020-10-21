'''
Taken this example from https://stackoverflow.com/questions/30976962/nested-boolean-expression-parser-using-antlr
'''
from antlr4 import CommonTokenStream, ParseTreeWalker

from gen.SimpleBooleanVisitor import SimpleBooleanVisitor
from gen.SimpleBooleanParser import SimpleBooleanParser
from gen.SimpleBooleanLexer import SimpleBooleanLexer
from gen.SimpleBooleanListener import SimpleBooleanListener
from antlr4.InputStream import InputStream

class CustomVisitor(SimpleBooleanVisitor):

    def __init__(self):
        pass

    def visitBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        print("boolean")
        print(ctx)

    def visitDecimalExpression(self, ctx:SimpleBooleanParser.DecimalExpressionContext):
        print('Decimal')
        print(ctx)


class CustomListener(SimpleBooleanListener):
    def enterBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        print('binary expr')

    def enterComparatorExpression(self, ctx:SimpleBooleanParser.ComparatorExpressionContext):
        print('comparation expr')

    def enterIdentifierExpression(self, ctx:SimpleBooleanParser.IdentifierExpressionContext):
        print('identifier')



if __name__ == '__main__':
    variables = {
        'a',True,
        'A',True,
    }
    exprs = [
        'A > 2'
        '1 >= 1.0'
    ]

    for expr in exprs:
        expr_stream = InputStream(expr)
        lexer = SimpleBooleanLexer(expr_stream)
        stream = CommonTokenStream(lexer)
        parser = SimpleBooleanParser(stream)

        tree = parser.parse()
        #printer = CustomVisitor()
        #printer.visit(tree)
        walker = ParseTreeWalker()
        walker.walk(CustomListener(), tree)

