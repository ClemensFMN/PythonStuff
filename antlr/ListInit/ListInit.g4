grammar ListInit;

stat: expr NEWLINE
    | NEWLINE
    ;

expr: '[' INT ']'          # OneInt
    | '[' INT ',' INT ']'  # TwoInt
    ;

INT     : [0-9]+ ;
NEWLINE : '\r'? '\n';
WS      : [ \t]+ -> skip;

