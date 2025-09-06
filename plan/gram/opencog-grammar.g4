
grammar OpenCogGrammar;

// Lexer Rules
LPAREN          : '(' ;
RPAREN          : ')' ;
LBRACKET        : '[' ;
RBRACKET        : ']' ;
LBRACE          : '{' ;
RBRACE          : '}' ;
DOT             : '.' ;
COMMA           : ',' ;
SEMICOLON       : ';' ;
COLON           : ':' ;
ARROW           : '->' ;
DOUBLE_ARROW    : '=>' ;
PIPE            : '|' ;
AMPERSAND       : '&' ;
EXCLAMATION     : '!' ;
QUESTION        : '?' ;
STAR            : '*' ;
PLUS            : '+' ;
MINUS           : '-' ;
SLASH           : '/' ;
PERCENT         : '%' ;
EQUALS          : '=' ;
NOT_EQUALS      : '!=' ;
LESS_THAN       : '<' ;
GREATER_THAN    : '>' ;
LESS_EQUAL      : '<=' ;
GREATER_EQUAL   : '>=' ;

// Keywords
ATOMSPACE       : 'AtomSpace' ;
ATOM            : 'Atom' ;
NODE            : 'Node' ;
LINK            : 'Link' ;
CONCEPT         : 'Concept' ;
PREDICATE       : 'Predicate' ;
VARIABLE        : 'Variable' ;
INHERITANCE     : 'Inheritance' ;
SIMILARITY      : 'Similarity' ;
EVALUATION      : 'Evaluation' ;
EXECUTION       : 'Execution' ;
IMPLICATION     : 'Implication' ;
EQUIVALENCE     : 'Equivalence' ;
AND             : 'And' ;
OR              : 'Or' ;
NOT             : 'Not' ;
TRUE            : 'True' ;
FALSE           : 'False' ;
BIND            : 'Bind' ;
GET             : 'Get' ;
PUT             : 'Put' ;
DEFINE          : 'define' ;
LAMBDA          : 'lambda' ;
LET             : 'let' ;
IF              : 'if' ;
THEN            : 'then' ;
ELSE            : 'else' ;
COND            : 'cond' ;
CASE            : 'case' ;
WHEN            : 'when' ;
UNLESS          : 'unless' ;
WHILE           : 'while' ;
FOR             : 'for' ;
MAP             : 'map' ;
FILTER          : 'filter' ;
REDUCE          : 'reduce' ;
PATTERN         : 'Pattern' ;
RULE            : 'Rule' ;
SCHEMA          : 'Schema' ;
MODULE          : 'module' ;
IMPORT          : 'import' ;
EXPORT          : 'export' ;

// Literals
NUMBER          : DIGIT+ ('.' DIGIT+)? ([eE] [+-]? DIGIT+)? ;
STRING          : '"' (~[\\"] | '\\' .)* '"' ;
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_-]* ;
VARIABLE_NAME   : '$' [a-zA-Z_][a-zA-Z0-9_-]* ;

// Comments and Whitespace
LINE_COMMENT    : ';' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '#|' .*? '|#' -> skip ;
WHITESPACE      : [ \t\r\n]+ -> skip ;

fragment DIGIT  : [0-9] ;

// Parser Rules

// Top-level program
program
    : (statement | expression)* EOF
    ;

statement
    : atomspaceDecl
    | moduleDecl
    | importDecl
    | exportDecl
    | definition
    ;

// AtomSpace declarations
atomspaceDecl
    : ATOMSPACE IDENTIFIER LBRACE atomDecl* RBRACE
    ;

atomDecl
    : nodeDecl
    | linkDecl
    ;

nodeDecl
    : nodeType LPAREN name=STRING (COMMA truthValue)? RPAREN
    ;

linkDecl
    : linkType LPAREN outgoingList (COMMA truthValue)? RPAREN
    ;

nodeType
    : CONCEPT | PREDICATE | VARIABLE | IDENTIFIER
    ;

linkType
    : INHERITANCE | SIMILARITY | EVALUATION | EXECUTION
    | IMPLICATION | EQUIVALENCE | AND | OR | NOT
    | BIND | GET | PUT | IDENTIFIER
    ;

outgoingList
    : atom (COMMA atom)*
    ;

atom
    : nodeDecl
    | linkDecl
    | atomReference
    ;

atomReference
    : IDENTIFIER
    | VARIABLE_NAME
    | NUMBER
    | STRING
    ;

truthValue
    : LBRACKET strength=NUMBER COMMA confidence=NUMBER RBRACKET
    ;

// Module system
moduleDecl
    : MODULE IDENTIFIER LBRACE moduleBody RBRACE
    ;

moduleBody
    : (statement | expression)*
    ;

importDecl
    : IMPORT moduleName=IDENTIFIER (DOT symbolList)?
    ;

exportDecl
    : EXPORT symbolList
    ;

symbolList
    : LPAREN IDENTIFIER (COMMA IDENTIFIER)* RPAREN
    | IDENTIFIER
    ;

// Definitions
definition
    : DEFINE IDENTIFIER expression
    | DEFINE LPAREN IDENTIFIER parameterList RPAREN expression
    | schemaDefinition
    | ruleDefinition
    ;

schemaDefinition
    : SCHEMA IDENTIFIER LPAREN parameterList RPAREN LBRACE schemaBody RBRACE
    ;

schemaBody
    : (precondition | postcondition | invariant)*
    ;

precondition
    : 'pre' COLON expression
    ;

postcondition
    : 'post' COLON expression
    ;

invariant
    : 'invariant' COLON expression
    ;

ruleDefinition
    : RULE IDENTIFIER LBRACE
        'premises' COLON expressionList SEMICOLON
        'conclusion' COLON expression SEMICOLON
        ('weight' COLON NUMBER SEMICOLON)?
        ('preconditions' COLON expressionList SEMICOLON)?
      RBRACE
    ;

parameterList
    : (parameter (COMMA parameter)*)?
    ;

parameter
    : IDENTIFIER (COLON typeAnnotation)?
    ;

typeAnnotation
    : IDENTIFIER
    | atomType
    ;

atomType
    : nodeType
    | linkType
    | ATOMSPACE
    | PATTERN
    ;

// Expressions
expression
    : primaryExpression
    | unaryExpression
    | binaryExpression
    | conditionalExpression
    | lambdaExpression
    | applicationExpression
    | patternExpression
    ;

primaryExpression
    : atom
    | NUMBER
    | STRING
    | TRUE
    | FALSE
    | IDENTIFIER
    | VARIABLE_NAME
    | LPAREN expression RPAREN
    | listExpression
    | setExpression
    ;

listExpression
    : LPAREN expressionList RPAREN
    | LBRACKET expressionList RBRACKET
    ;

setExpression
    : LBRACE expressionList RBRACE
    ;

expressionList
    : (expression (COMMA expression)*)?
    ;

unaryExpression
    : operator=(NOT | MINUS | PLUS | EXCLAMATION) expression
    ;

binaryExpression
    : left=expression operator=(STAR | SLASH | PERCENT) right=expression
    | left=expression operator=(PLUS | MINUS) right=expression
    | left=expression operator=(LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL) right=expression
    | left=expression operator=(EQUALS | NOT_EQUALS) right=expression
    | left=expression operator=AMPERSAND right=expression
    | left=expression operator=PIPE right=expression
    | left=expression operator=ARROW right=expression
    | left=expression operator=DOUBLE_ARROW right=expression
    ;

conditionalExpression
    : IF condition=expression THEN thenExpr=expression ELSE elseExpr=expression
    | COND LBRACE condClause* RBRACE
    | CASE expression LBRACE caseClause* RBRACE
    ;

condClause
    : LBRACKET condition=expression ARROW result=expression RBRACKET
    ;

caseClause
    : pattern ARROW expression
    ;

lambdaExpression
    : LAMBDA LPAREN parameterList RPAREN expression
    | LAMBDA IDENTIFIER expression
    ;

applicationExpression
    : function=expression LPAREN argumentList RPAREN
    ;

argumentList
    : (expression (COMMA expression)*)?
    ;

patternExpression
    : PATTERN LBRACE
        ('variables' COLON variableList SEMICOLON)?
        ('clauses' COLON expressionList SEMICOLON)?
        ('constraints' COLON expressionList SEMICOLON)?
      RBRACE
    | GET patternBody
    | BIND LPAREN variables=expressionList COMMA pattern=expression COMMA rewrite=expression RPAREN
    ;

patternBody
    : expression
    ;

variableList
    : LPAREN VARIABLE_NAME (COMMA VARIABLE_NAME)* RPAREN
    | VARIABLE_NAME
    ;

// Pattern matching
pattern
    : atomPattern
    | variablePattern
    | wildcardPattern
    | literalPattern
    ;

atomPattern
    : nodeType LPAREN pattern (COMMA pattern)* RPAREN
    | linkType LPAREN patternList RPAREN
    ;

variablePattern
    : VARIABLE_NAME
    | VARIABLE_NAME COLON typeAnnotation
    ;

wildcardPattern
    : STAR
    | QUESTION
    ;

literalPattern
    : NUMBER
    | STRING
    | TRUE
    | FALSE
    ;

patternList
    : (pattern (COMMA pattern)*)?
    ;
