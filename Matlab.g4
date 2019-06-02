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
    leftbracket return_name (COMMA return_name)* rightbracket
    | leftbracket rightbracket ;

leftbracket : LEFTBRACKET ;

rightbracket : RIGHTBRACKET ;

return_name : NAME|NOT ;

name : NAME;

definemark : DEFINEMARK ;

typedef : definemark cate name (COMMA name)* | definemark cate nameplus ;

ruledef : definemark name ;

nameplus : NAMEPLUS ;

cate : NAME | NAME NAME;

digit : DIGIT ;

null_assign : NULL_ASSIGN ;

expr:
        unary_operation expr                     # unary_operaExpr
        | LEFTPAREN expr RIGHTPAREN              # parensExpr
        | expr multiplicative_operation expr     # multiExpr
        | expr additive_operation expr           # addExpr
        | expr relational_operation expr         # relatExpr
        | expr andor_operation expr              # andorExpr
        | expr logical_operation expr            # logicExpr
        | digit                                  # digitExpr
        | truth_value                            # truthExpr
        | name (DOT name)*                           # nameExpr
        | leftbracket name COMMA name COMMA name rightbracket  # regExpr
        | function_call                          # funcallExpr
        | element                                # elemExpr
        | null_assign                            # nullExpr
        | (QUOTE name QUOTE | DOUBLEQUOTE name DOUBLEQUOTE | QUOTE QUOTE | DOUBLEQUOTE DOUBLEQUOTE)  # strExpr
         ;

unary_operation : SUB|NOT ;
multiplicative_operation : MUL|DIV ;
additive_operation : ADD|SUB ;
relational_operation : EQUAL|UNEQUAL|LESS|LESS_EQUAL|GREATER|GREATER_EQUAL ;
andor_operation : AND|OR ;
logical_operation : LOGICAL_AND|LOGICAL_OR ;
truth_value : TRUE_VALUE|FALSE_VALUE ;

location_name : COLON|expr ;

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
    | typedef SEMICOLON
    | ruledef
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
        IF expr (com_statement)* (elseif_state)* (else_state)? END ;

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
DEFINEMARK : '%' ;

NAME : LETTER(CHARACTER)* ;
NAMEPLUS : NAME LEFTBRACKET NAME RIGHTBRACKET | NAME LEFTBRACKET NAME RIGHTBRACKET LEFTBRACKET NAME RIGHTBRACKET ;
DIGIT : (NUMBER)+ ;
NULL_ASSIGN : LEFTBRACKET RIGHTBRACKET ;

fragment LETTER : [*_a-zA-Z] ;
fragment NO_ZERO_NUMBER : [1-9] ;
fragment NUMBER : '0' | NO_ZERO_NUMBER ;
fragment CHARACTER : LETTER | NUMBER ;

WS : [ \t\n\r]+ -> skip ;
