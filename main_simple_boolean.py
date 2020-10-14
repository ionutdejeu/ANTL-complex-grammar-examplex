'''
Taken this example from https://stackoverflow.com/questions/30976962/nested-boolean-expression-parser-using-antlr
'''
from antlr4 import CommonTokenStream, ParseTreeWalker

from gen.SimpleBooleanVisitor import SimpleBooleanVisitor
from gen.SimpleBooleanParser import SimpleBooleanParser
from gen.SimpleBooleanLexer import SimpleBooleanLexer
from gen.SimpleBooleanListener import SimpleBooleanListener
from antlr4.InputStream import InputStream

class EvalListener(SimpleBooleanListener):

    variables:dict = {}
    def __init__(self,variables:dict):
        self.variables = variables

    def exitBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        super().exitBinaryExpression(ctx)

class CustomVisitor(SimpleBooleanVisitor):
    def visitBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        super().visitBinaryExpression(ctx)

if __name__ == '__main__':
    variables = {
        'a',True,
        'A',True,
    }
    exprs = [
        '1 > 2'
        '1 >= 1.0'
    ]

    for expr in exprs:
        expr_stream = InputStream(expr)
        lexer = SimpleBooleanLexer(expr_stream)
        stream = CommonTokenStream(lexer)
        parser = SimpleBooleanParser(stream)
        tree = parser.parse()
        printer = CustomVisitor()
        printer.visit(tree)
        #walker = ParseTreeWalker()
        #walker.walk(printer, tree)

