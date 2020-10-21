# Generated from C:/Projects/Tech/Python/ANTL-complex-grammar-examplex/grammars\SimpleBoolean.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("/\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\32\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3$\n\3\f\3\16\3\'\13")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\2\3\4\7\2\4\6\b\n\2\5\3")
        buf.write("\2\b\f\3\2\3\4\3\2\6\7\2/\2\f\3\2\2\2\4\31\3\2\2\2\6(")
        buf.write("\3\2\2\2\b*\3\2\2\2\n,\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2")
        buf.write("\3\16\3\3\2\2\2\17\20\b\3\1\2\20\21\7\r\2\2\21\22\5\4")
        buf.write("\3\2\22\23\7\16\2\2\23\32\3\2\2\2\24\25\7\5\2\2\25\32")
        buf.write("\5\4\3\b\26\32\5\n\6\2\27\32\7\20\2\2\30\32\7\17\2\2\31")
        buf.write("\17\3\2\2\2\31\24\3\2\2\2\31\26\3\2\2\2\31\27\3\2\2\2")
        buf.write("\31\30\3\2\2\2\32%\3\2\2\2\33\34\f\7\2\2\34\35\5\6\4\2")
        buf.write("\35\36\5\4\3\b\36$\3\2\2\2\37 \f\6\2\2 !\5\b\5\2!\"\5")
        buf.write("\4\3\7\"$\3\2\2\2#\33\3\2\2\2#\37\3\2\2\2$\'\3\2\2\2%")
        buf.write("#\3\2\2\2%&\3\2\2\2&\5\3\2\2\2\'%\3\2\2\2()\t\2\2\2)\7")
        buf.write("\3\2\2\2*+\t\3\2\2+\t\3\2\2\2,-\t\4\2\2-\13\3\2\2\2\5")
        buf.write("\31#%")
        return buf.getvalue()


class SimpleBooleanParser ( Parser ):

    grammarFileName = "SimpleBoolean.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'AND'", "'OR'", "'NOT'", "'TRUE'", "'FALSE'", 
                     "'>'", "'>='", "'<'", "'<='", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "TRUE", "FALSE", 
                      "GT", "GE", "LT", "LE", "EQ", "LPAREN", "RPAREN", 
                      "DECIMAL", "IDENTIFIER", "WS" ]

    RULE_parse = 0
    RULE_expression = 1
    RULE_comparator = 2
    RULE_binary = 3
    RULE_boolean_r = 4

    ruleNames =  [ "parse", "expression", "comparator", "binary", "boolean_r" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    TRUE=4
    FALSE=5
    GT=6
    GE=7
    LT=8
    LE=9
    EQ=10
    LPAREN=11
    RPAREN=12
    DECIMAL=13
    IDENTIFIER=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleBooleanParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(SimpleBooleanParser.EOF, 0)

        def getRuleIndex(self):
            return SimpleBooleanParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = SimpleBooleanParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expression(0)
            self.state = 11
            self.match(SimpleBooleanParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleBooleanParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BinaryExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # BinaryContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleBooleanParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleBooleanParser.ExpressionContext,i)

        def binary(self):
            return self.getTypedRuleContext(SimpleBooleanParser.BinaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpression" ):
                listener.enterBinaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpression" ):
                listener.exitBinaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpression" ):
                return visitor.visitBinaryExpression(self)
            else:
                return visitor.visitChildren(self)


    class DecimalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(SimpleBooleanParser.DECIMAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecimalExpression" ):
                listener.enterDecimalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecimalExpression" ):
                listener.exitDecimalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecimalExpression" ):
                return visitor.visitDecimalExpression(self)
            else:
                return visitor.visitChildren(self)


    class BoolExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean_r(self):
            return self.getTypedRuleContext(SimpleBooleanParser.Boolean_rContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpression" ):
                listener.enterBoolExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpression" ):
                listener.exitBoolExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpression" ):
                return visitor.visitBoolExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(SimpleBooleanParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SimpleBooleanParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(SimpleBooleanParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SimpleBooleanParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(SimpleBooleanParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(SimpleBooleanParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpression" ):
                listener.enterParenExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpression" ):
                listener.exitParenExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpression" ):
                return visitor.visitParenExpression(self)
            else:
                return visitor.visitChildren(self)


    class ComparatorExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleBooleanParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.op = None # ComparatorContext
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleBooleanParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleBooleanParser.ExpressionContext,i)

        def comparator(self):
            return self.getTypedRuleContext(SimpleBooleanParser.ComparatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparatorExpression" ):
                listener.enterComparatorExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparatorExpression" ):
                listener.exitComparatorExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparatorExpression" ):
                return visitor.visitComparatorExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleBooleanParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleBooleanParser.LPAREN]:
                localctx = SimpleBooleanParser.ParenExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.match(SimpleBooleanParser.LPAREN)
                self.state = 15
                self.expression(0)
                self.state = 16
                self.match(SimpleBooleanParser.RPAREN)
                pass
            elif token in [SimpleBooleanParser.NOT]:
                localctx = SimpleBooleanParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(SimpleBooleanParser.NOT)
                self.state = 19
                self.expression(6)
                pass
            elif token in [SimpleBooleanParser.TRUE, SimpleBooleanParser.FALSE]:
                localctx = SimpleBooleanParser.BoolExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.boolean_r()
                pass
            elif token in [SimpleBooleanParser.IDENTIFIER]:
                localctx = SimpleBooleanParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(SimpleBooleanParser.IDENTIFIER)
                pass
            elif token in [SimpleBooleanParser.DECIMAL]:
                localctx = SimpleBooleanParser.DecimalExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(SimpleBooleanParser.DECIMAL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = SimpleBooleanParser.ComparatorExpressionContext(self, SimpleBooleanParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 25
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 26
                        localctx.op = self.comparator()
                        self.state = 27
                        localctx.right = self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SimpleBooleanParser.BinaryExpressionContext(self, SimpleBooleanParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        localctx.op = self.binary()
                        self.state = 31
                        localctx.right = self.expression(5)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(SimpleBooleanParser.GT, 0)

        def GE(self):
            return self.getToken(SimpleBooleanParser.GE, 0)

        def LT(self):
            return self.getToken(SimpleBooleanParser.LT, 0)

        def LE(self):
            return self.getToken(SimpleBooleanParser.LE, 0)

        def EQ(self):
            return self.getToken(SimpleBooleanParser.EQ, 0)

        def getRuleIndex(self):
            return SimpleBooleanParser.RULE_comparator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparator" ):
                listener.enterComparator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparator" ):
                listener.exitComparator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = SimpleBooleanParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleBooleanParser.GT) | (1 << SimpleBooleanParser.GE) | (1 << SimpleBooleanParser.LT) | (1 << SimpleBooleanParser.LE) | (1 << SimpleBooleanParser.EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(SimpleBooleanParser.AND, 0)

        def OR(self):
            return self.getToken(SimpleBooleanParser.OR, 0)

        def getRuleIndex(self):
            return SimpleBooleanParser.RULE_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary" ):
                listener.enterBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary" ):
                listener.exitBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary" ):
                return visitor.visitBinary(self)
            else:
                return visitor.visitChildren(self)




    def binary(self):

        localctx = SimpleBooleanParser.BinaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_binary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==SimpleBooleanParser.AND or _la==SimpleBooleanParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_rContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(SimpleBooleanParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(SimpleBooleanParser.FALSE, 0)

        def getRuleIndex(self):
            return SimpleBooleanParser.RULE_boolean_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_r" ):
                listener.enterBoolean_r(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_r" ):
                listener.exitBoolean_r(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_r" ):
                return visitor.visitBoolean_r(self)
            else:
                return visitor.visitChildren(self)




    def boolean_r(self):

        localctx = SimpleBooleanParser.Boolean_rContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_boolean_r)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            _la = self._input.LA(1)
            if not(_la==SimpleBooleanParser.TRUE or _la==SimpleBooleanParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




