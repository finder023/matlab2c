/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

grammar Matlab;

/*
 * Parser Rules
 */

function :
    FUCTION function_declare (statement)? END ;

function_declare:
    (returnparas ASSIGN)? name paralist ;

returnparas :
    leftbracket name (COMMA name)* rightbracket
    | leftbracket rightbracket ;

leftbracket : LEFTBRACKET ;

rightbracket : RIGHTBRACKET ;


name : NAME;

// definemark : DEFINEMARK ;

// typedef : definemark cate name (COMMA name)* | definemark cate nameplus ;

// ruledef : definemark name ;

nameplus : NAMEPLUS ;

cate : NAME | NAME NAME;

digit : DIGIT ;

null_assign : NULL_ASSIGN ;

expr:
        unary_operation expr                        # unary_operaExpr
        | expr binary_operation expr                # binaryExpr
        | LEFTPAREN expr RIGHTPAREN                 # parensExpr
        | digit                                     # digitExpr
        | truth_value                               # truthExpr
        | name (DOT name)*                          # nameExpr
        | leftbracket name COMMA name COMMA name rightbracket  # regExpr
        | function_call                             # funcallExpr
        | element                                   # elemExpr
        | null_assign                               # nullExpr
        | (QUOTE name QUOTE | DOUBLEQUOTE name DOUBLEQUOTE | QUOTE QUOTE | DOUBLEQUOTE DOUBLEQUOTE)  # strExpr
         ;

binary_operation: ADD | SUB | MUL | DIV | EQUAL | UNEQUAL | LESS | LESS_EQUAL 
                | GREATER | GREATER_EQUAL | AND | OR | LOGICAL_AND | LOGICAL_OR;
unary_operation : SUB | NOT ;
truth_value : TRUE_VALUE | FALSE_VALUE ;

location_name : COLON | expr ;

location:
     location_name COMMA location_name ;

element:
    name LEFTBRACE location RIGHTBRACE ;

paralist :
    LEFTPAREN expr (COMMA expr)* RIGHTPAREN
    | LEFTPAREN RIGHTPAREN ;

statement:
    global_define_list (com_statement)* ;

global_define_list:
    (GLOBAL name SEMICOLON (GLOBAL name SEMICOLON)*)? ;

com_statement:
    assign_state SEMICOLON
    | function_call SEMICOLON
    | return_state SEMICOLON
    | while_state
    | if_state
    | break_state SEMICOLON
    | continue_state SEMICOLON
    | element_insert_state SEMICOLON
    | element_delete_state SEMICOLON
    | element_ismember_set SEMICOLON
    | element_take SEMICOLON
//    | typedef SEMICOLON
//    | ruledef
    ;
    
assign_state:
    expr ASSIGN expr ;

function_call:
    name paralist ;

return_state:
    RETURN ;
    
while_state:
    WHILE expr (com_statement)* END ;

if_state:
        IF LEFTPAREN? expr RIGHTPAREN? (com_statement)* (elseif_state)* (else_state)? END ;

elseif_state:
        ELSEIF expr (com_statement)* ;

else_state:
        ELSE (com_statement)* ;

break_state:
        BREAK ;

continue_state:
        CONTINUE ;

element_insert_state:
        expr ASSIGN UNION LEFTPAREN expr COMMA name RIGHTPAREN ;

element_delete_state:
        expr ASSIGN SETDIFF LEFTPAREN expr COMMA name RIGHTPAREN ;

element_ismember_set:
        returnparas ASSIGN ISMEMBER LEFTPAREN name COMMA name RIGHTPAREN ;

element_take:
        name ASSIGN LEFTBRACKET element RIGHTBRACKET
        | name ASSIGN LEFTBRACE element RIGHTBRACE ;


/*
 * Lexer Rules
 */
FUCTION : 'function' ;
END : 'end' ;
GLOBAL : 'global' ;
RETURN : 'return' ;
WHILE : 'while' ;
IF : 'if' ;
ELSEIF : 'elseif' ;
ELSE : 'else' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
UNION : 'union' ;
SETDIFF : 'setdiff' ;
ISMEMBER : 'ismember' ;

ADD : '+' ;
SUB : '-' ;
MUL : '*' ;
DIV : '/' ;
AND : '&' ;
OR : '|' ;
NOT : '~' ;
LOGICAL_AND : '&&' ;
LOGICAL_OR : '||' ;
EQUAL : '==' ;
UNEQUAL : '~=' ;
LESS : '<' ;
LESS_EQUAL : '<=' ;
GREATER : '>' ;
GREATER_EQUAL : '>=' ;
TRUE_VALUE : 'true' ;
FALSE_VALUE : 'false' ;

LEFTBRACKET : '[' ;
RIGHTBRACKET : ']' ;
LEFTPAREN : '(' ;
RIGHTPAREN : ')' ;
LEFTBRACE : '{' ;
RIGHTBRACE : '}' ;
COMMA : ',' ;
SEMICOLON : ';' ;
ASSIGN : '=' ;
DOT : '.' ;
COLON : ':' ;
QUOTE : '\'' ;
DOUBLEQUOTE : '"';
NL : ('\r' '\n' | '\r' | '\n') -> channel(HIDDEN);
// DEFINEMARK : '%' ;
COMMENT	: '%' .*? NL -> channel(HIDDEN);

NAME : LETTER(CHARACTER)* ;
NAMEPLUS : NAME LEFTBRACKET NAME RIGHTBRACKET | NAME LEFTBRACKET NAME RIGHTBRACKET LEFTBRACKET NAME RIGHTBRACKET ;
DIGIT : (NUMBER)+ ;
NULL_ASSIGN : LEFTBRACKET RIGHTBRACKET ;

fragment LETTER : [*_a-zA-Z] ;
fragment NO_ZERO_NUMBER : [1-9] ;
fragment NUMBER : '0' | NO_ZERO_NUMBER ;
fragment CHARACTER : LETTER | NUMBER ;

WS : [ \t\n\r]+ -> skip ;
