grammar recursive;

class Pascal;

prog:   INT
        (   RANGE INT
            { System.out.println("INT .. INT"); }
        |   EOF
            { System.out.println("plain old INT"); }
        )
    |   REAL { System.out.println("token REAL"); }
    ;

lexclass LexPascal;

WS  :   (' '
    |   '\t'
    |   '\n'
    |   '\r')
        { $setType(Token.SKIP); }
    ;

protected
INT :   ('0'..'9')+
    ;

protected
REAL:   INT '.' INT
    ;

RANGE
    :   ".."
    ;

RANGE_OR_INT
    :   ( INT ".." ) => INT  { $setType(INT); }
    |   ( INT '.' )  => REAL { $setType(REAL); }
    |   INT                  { $setType(INT); }
    ;