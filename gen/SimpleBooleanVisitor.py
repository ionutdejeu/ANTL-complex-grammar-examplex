# Generated from C:/Projects/Tech/Python/ANTL-complex-grammar-examplex/grammars\SimpleBoolean.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleBooleanParser import SimpleBooleanParser
else:
    from SimpleBooleanParser import SimpleBooleanParser

# This class defines a complete generic visitor for a parse tree produced by SimpleBooleanParser.

class SimpleBooleanVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleBooleanParser#parse.
    def visitParse(self, ctx:SimpleBooleanParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#binaryExpression.
    def visitBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#decimalExpression.
    def visitDecimalExpression(self, ctx:SimpleBooleanParser.DecimalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#boolExpression.
    def visitBoolExpression(self, ctx:SimpleBooleanParser.BoolExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SimpleBooleanParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#notExpression.
    def visitNotExpression(self, ctx:SimpleBooleanParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#parenExpression.
    def visitParenExpression(self, ctx:SimpleBooleanParser.ParenExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#comparatorExpression.
    def visitComparatorExpression(self, ctx:SimpleBooleanParser.ComparatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#comparator.
    def visitComparator(self, ctx:SimpleBooleanParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#binary.
    def visitBinary(self, ctx:SimpleBooleanParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleBooleanParser#boolean_r.
    def visitBoolean_r(self, ctx:SimpleBooleanParser.Boolean_rContext):
        return self.visitChildren(ctx)



del SimpleBooleanParser