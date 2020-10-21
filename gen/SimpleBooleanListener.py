# Generated from C:/Projects/Tech/Python/ANTL-complex-grammar-examplex/grammars\SimpleBoolean.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleBooleanParser import SimpleBooleanParser
else:
    from SimpleBooleanParser import SimpleBooleanParser

# This class defines a complete listener for a parse tree produced by SimpleBooleanParser.
class SimpleBooleanListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleBooleanParser#parse.
    def enterParse(self, ctx:SimpleBooleanParser.ParseContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#parse.
    def exitParse(self, ctx:SimpleBooleanParser.ParseContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#binaryExpression.
    def enterBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#binaryExpression.
    def exitBinaryExpression(self, ctx:SimpleBooleanParser.BinaryExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#decimalExpression.
    def enterDecimalExpression(self, ctx:SimpleBooleanParser.DecimalExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#decimalExpression.
    def exitDecimalExpression(self, ctx:SimpleBooleanParser.DecimalExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#boolExpression.
    def enterBoolExpression(self, ctx:SimpleBooleanParser.BoolExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#boolExpression.
    def exitBoolExpression(self, ctx:SimpleBooleanParser.BoolExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:SimpleBooleanParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:SimpleBooleanParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#notExpression.
    def enterNotExpression(self, ctx:SimpleBooleanParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#notExpression.
    def exitNotExpression(self, ctx:SimpleBooleanParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#parenExpression.
    def enterParenExpression(self, ctx:SimpleBooleanParser.ParenExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#parenExpression.
    def exitParenExpression(self, ctx:SimpleBooleanParser.ParenExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#comparatorExpression.
    def enterComparatorExpression(self, ctx:SimpleBooleanParser.ComparatorExpressionContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#comparatorExpression.
    def exitComparatorExpression(self, ctx:SimpleBooleanParser.ComparatorExpressionContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#comparator.
    def enterComparator(self, ctx:SimpleBooleanParser.ComparatorContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#comparator.
    def exitComparator(self, ctx:SimpleBooleanParser.ComparatorContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#binary.
    def enterBinary(self, ctx:SimpleBooleanParser.BinaryContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#binary.
    def exitBinary(self, ctx:SimpleBooleanParser.BinaryContext):
        pass


    # Enter a parse tree produced by SimpleBooleanParser#boolean_r.
    def enterBoolean_r(self, ctx:SimpleBooleanParser.Boolean_rContext):
        pass

    # Exit a parse tree produced by SimpleBooleanParser#boolean_r.
    def exitBoolean_r(self, ctx:SimpleBooleanParser.Boolean_rContext):
        pass



del SimpleBooleanParser