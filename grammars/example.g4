grammar example;
query
    : unquoted_str+
    | '(' query ')'
    ;

unquoted_str
    : UNQUOTED_STR
    ;

UNQUOTED_STR
    : [A-Za-z_][A-Za-z0-9_-]*
    ;
WS
    :   [ \t\r\n]+ -> skip
    ;

ACTION
    :   '{' ( ACTION | ~'}' )* '}'
    ;

ID : ( 'a'..'z' )+
   ;