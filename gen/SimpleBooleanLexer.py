# Generated from C:/Projects/Tech/Python/ANTL-complex-grammar-examplex/grammars\SimpleBoolean.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\5\16I\n\16\3\16\6\16L\n\16\r")
        buf.write("\16\16\16M\3\16\3\16\6\16R\n\16\r\16\16\16S\5\16V\n\16")
        buf.write("\3\17\3\17\7\17Z\n\17\f\17\16\17]\13\17\3\20\6\20`\n\20")
        buf.write("\r\20\16\20a\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2")
        buf.write("\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17\"")
        buf.write("\"\2j\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5%\3\2\2")
        buf.write("\2\7(\3\2\2\2\t,\3\2\2\2\13\61\3\2\2\2\r\67\3\2\2\2\17")
        buf.write("9\3\2\2\2\21<\3\2\2\2\23>\3\2\2\2\25A\3\2\2\2\27C\3\2")
        buf.write("\2\2\31E\3\2\2\2\33H\3\2\2\2\35W\3\2\2\2\37_\3\2\2\2!")
        buf.write("\"\7C\2\2\"#\7P\2\2#$\7F\2\2$\4\3\2\2\2%&\7Q\2\2&\'\7")
        buf.write("T\2\2\'\6\3\2\2\2()\7P\2\2)*\7Q\2\2*+\7V\2\2+\b\3\2\2")
        buf.write("\2,-\7V\2\2-.\7T\2\2./\7W\2\2/\60\7G\2\2\60\n\3\2\2\2")
        buf.write("\61\62\7H\2\2\62\63\7C\2\2\63\64\7N\2\2\64\65\7U\2\2\65")
        buf.write("\66\7G\2\2\66\f\3\2\2\2\678\7@\2\28\16\3\2\2\29:\7@\2")
        buf.write("\2:;\7?\2\2;\20\3\2\2\2<=\7>\2\2=\22\3\2\2\2>?\7>\2\2")
        buf.write("?@\7?\2\2@\24\3\2\2\2AB\7?\2\2B\26\3\2\2\2CD\7*\2\2D\30")
        buf.write("\3\2\2\2EF\7+\2\2F\32\3\2\2\2GI\7/\2\2HG\3\2\2\2HI\3\2")
        buf.write("\2\2IK\3\2\2\2JL\t\2\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2")
        buf.write("MN\3\2\2\2NU\3\2\2\2OQ\7\60\2\2PR\t\2\2\2QP\3\2\2\2RS")
        buf.write("\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2UO\3\2\2\2UV\3\2")
        buf.write("\2\2V\34\3\2\2\2W[\t\3\2\2XZ\t\4\2\2YX\3\2\2\2Z]\3\2\2")
        buf.write("\2[Y\3\2\2\2[\\\3\2\2\2\\\36\3\2\2\2][\3\2\2\2^`\t\5\2")
        buf.write("\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2bc\3\2\2\2c")
        buf.write("d\b\20\2\2d \3\2\2\2\t\2HMSU[a\3\b\2\2")
        return buf.getvalue()


class SimpleBooleanLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    OR = 2
    NOT = 3
    TRUE = 4
    FALSE = 5
    GT = 6
    GE = 7
    LT = 8
    LE = 9
    EQ = 10
    LPAREN = 11
    RPAREN = 12
    DECIMAL = 13
    IDENTIFIER = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'AND'", "'OR'", "'NOT'", "'TRUE'", "'FALSE'", "'>'", "'>='", 
            "'<'", "'<='", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "OR", "NOT", "TRUE", "FALSE", "GT", "GE", "LT", "LE", 
            "EQ", "LPAREN", "RPAREN", "DECIMAL", "IDENTIFIER", "WS" ]

    ruleNames = [ "AND", "OR", "NOT", "TRUE", "FALSE", "GT", "GE", "LT", 
                  "LE", "EQ", "LPAREN", "RPAREN", "DECIMAL", "IDENTIFIER", 
                  "WS" ]

    grammarFileName = "SimpleBoolean.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


