
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "opencog-parser.tab.h"

int yylineno = 1;
%}

%option noyywrap
%option yylineno

/* Character classes */
DIGIT           [0-9]
LETTER          [a-zA-Z]
ALPHANUM        [a-zA-Z0-9]
IDENTIFIER_CHAR [a-zA-Z0-9_-]
WHITESPACE      [ \t\r]
NEWLINE         \n

/* Number patterns */
INTEGER         {DIGIT}+
FLOAT           {DIGIT}+\.{DIGIT}+
SCIENTIFIC      ({INTEGER}|{FLOAT})[eE][+-]?{DIGIT}+
NUMBER          {INTEGER}|{FLOAT}|{SCIENTIFIC}

/* String patterns */
STRING_CHAR     [^\\"]
ESCAPE_CHAR     \\[\\"/bfnrt]
UNICODE_ESCAPE  \\u[0-9a-fA-F]{4}
STRING_CONTENT  ({STRING_CHAR}|{ESCAPE_CHAR}|{UNICODE_ESCAPE})*
STRING          \"{STRING_CONTENT}\"

/* Identifier patterns */
IDENTIFIER      {LETTER}{IDENTIFIER_CHAR}*
VARIABLE_NAME   \${LETTER}{IDENTIFIER_CHAR}*

/* Comment patterns */
LINE_COMMENT    ;[^\r\n]*
BLOCK_COMMENT   #\|([^|]|\|[^#])*\|#

%%

{WHITESPACE}+   { /* ignore whitespace */ }
{NEWLINE}       { yylineno++; }
{LINE_COMMENT}  { /* ignore line comments */ }
{BLOCK_COMMENT} { /* ignore block comments */ }

/* Punctuation */
"("             { return LPAREN; }
")"             { return RPAREN; }
"["             { return LBRACKET; }
"]"             { return RBRACKET; }
"{"             { return LBRACE; }
"}"             { return RBRACE; }
"."             { return DOT; }
","             { return COMMA; }
";"             { return SEMICOLON; }
":"             { return COLON; }
"->"            { return ARROW; }
"=>"            { return DOUBLE_ARROW; }
"|"             { return PIPE; }
"&"             { return AMPERSAND; }
"!"             { return EXCLAMATION; }
"?"             { return QUESTION; }
"*"             { return STAR; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"/"             { return SLASH; }
"%"             { return PERCENT; }
"="             { return EQUALS; }
"!="            { return NOT_EQUALS; }
"<"             { return LESS_THAN; }
">"             { return GREATER_THAN; }
"<="            { return LESS_EQUAL; }
">="            { return GREATER_EQUAL; }

/* Keywords - AtomSpace core */
"AtomSpace"     { return ATOMSPACE; }
"Atom"          { return ATOM; }
"Node"          { return NODE; }
"Link"          { return LINK; }

/* Node types */
"Concept"       { return CONCEPT; }
"ConceptNode"   { return CONCEPT; }
"Predicate"     { return PREDICATE; }
"PredicateNode" { return PREDICATE; }
"Variable"      { return VARIABLE; }
"VariableNode"  { return VARIABLE; }

/* Link types */
"Inheritance"   { return INHERITANCE; }
"InheritanceLink" { return INHERITANCE; }
"Similarity"    { return SIMILARITY; }
"SimilarityLink" { return SIMILARITY; }
"Evaluation"    { return EVALUATION; }
"EvaluationLink" { return EVALUATION; }
"Execution"     { return EXECUTION; }
"ExecutionLink" { return EXECUTION; }
"Implication"   { return IMPLICATION; }
"ImplicationLink" { return IMPLICATION; }
"Equivalence"   { return EQUIVALENCE; }
"EquivalenceLink" { return EQUIVALENCE; }

/* Logical operators */
"And"           { return AND; }
"AndLink"       { return AND; }
"Or"            { return OR; }
"OrLink"        { return OR; }
"Not"           { return NOT; }
"NotLink"       { return NOT; }
"True"          { return TRUE; }
"TrueLink"      { return TRUE; }
"False"         { return FALSE; }
"FalseLink"     { return FALSE; }

/* Pattern matching */
"Bind"          { return BIND; }
"BindLink"      { return BIND; }
"Get"           { return GET; }
"GetLink"       { return GET; }
"Put"           { return PUT; }
"PutLink"       { return PUT; }
"Pattern"       { return PATTERN; }
"PatternLink"   { return PATTERN; }

/* Language constructs */
"define"        { return DEFINE; }
"lambda"        { return LAMBDA; }
"let"           { return LET; }
"if"            { return IF; }
"then"          { return THEN; }
"else"          { return ELSE; }
"cond"          { return COND; }
"case"          { return CASE; }
"when"          { return WHEN; }
"unless"        { return UNLESS; }
"while"         { return WHILE; }
"for"           { return FOR; }

/* Higher-order functions */
"map"           { return MAP; }
"filter"        { return FILTER; }
"reduce"        { return REDUCE; }

/* Meta-programming */
"Rule"          { return RULE; }
"Schema"        { return SCHEMA; }

/* Module system */
"module"        { return MODULE; }
"import"        { return IMPORT; }
"export"        { return EXPORT; }

/* Literals */
{NUMBER}        { 
    yylval.number = atof(yytext); 
    return NUMBER; 
}

{STRING}        { 
    /* Remove quotes and process escape sequences */
    char *str = malloc(strlen(yytext) - 1);
    strncpy(str, yytext + 1, strlen(yytext) - 2);
    str[strlen(yytext) - 2] = '\0';
    yylval.string = str;
    return STRING; 
}

{VARIABLE_NAME} { 
    yylval.string = strdup(yytext); 
    return VARIABLE_NAME; 
}

{IDENTIFIER}    { 
    yylval.string = strdup(yytext); 
    return IDENTIFIER; 
}

/* Catch-all for unexpected characters */
.               { 
    fprintf(stderr, "Unexpected character '%c' at line %d\n", 
            yytext[0], yylineno); 
    return yytext[0];
}

%%

/* Additional C code */
void init_lexer() {
    yylineno = 1;
}

void cleanup_lexer() {
    if (YY_CURRENT_BUFFER) {
        yy_delete_buffer(YY_CURRENT_BUFFER);
    }
}

/* String scanning functions */
void yy_scan_string_cleanup(const char *str) {
    YY_BUFFER_STATE buffer = yy_scan_string(str);
    yyparse();
    yy_delete_buffer(buffer);
}

/* File scanning functions */
int yy_scan_file(FILE *file) {
    YY_BUFFER_STATE buffer = yy_create_buffer(file, YY_BUF_SIZE);
    yy_switch_to_buffer(buffer);
    int result = yyparse();
    yy_delete_buffer(buffer);
    return result;
}

/* Error handling */
void yyerror_detailed(const char *msg, const char *context) {
    fprintf(stderr, "Lexical error at line %d: %s\n", yylineno, msg);
    if (context) {
        fprintf(stderr, "Context: %s\n", context);
    }
}

/* Utility functions for token information */
const char *token_name(int token) {
    switch (token) {
        case LPAREN: return "LPAREN";
        case RPAREN: return "RPAREN";
        case LBRACKET: return "LBRACKET";
        case RBRACKET: return "RBRACKET";
        case LBRACE: return "LBRACE";
        case RBRACE: return "RBRACE";
        case ATOMSPACE: return "ATOMSPACE";
        case CONCEPT: return "CONCEPT";
        case PREDICATE: return "PREDICATE";
        case VARIABLE: return "VARIABLE";
        case INHERITANCE: return "INHERITANCE";
        case SIMILARITY: return "SIMILARITY";
        case EVALUATION: return "EVALUATION";
        case BIND: return "BIND";
        case GET: return "GET";
        case PUT: return "PUT";
        case DEFINE: return "DEFINE";
        case LAMBDA: return "LAMBDA";
        case IF: return "IF";
        case THEN: return "THEN";
        case ELSE: return "ELSE";
        case TRUE: return "TRUE";
        case FALSE: return "FALSE";
        case NUMBER: return "NUMBER";
        case STRING: return "STRING";
        case IDENTIFIER: return "IDENTIFIER";
        case VARIABLE_NAME: return "VARIABLE_NAME";
        default: return "UNKNOWN";
    }
}

void print_token(int token, YYSTYPE value) {
    printf("Token: %s", token_name(token));
    switch (token) {
        case NUMBER:
            printf(" (value: %g)", value.number);
            break;
        case STRING:
        case IDENTIFIER:
        case VARIABLE_NAME:
            printf(" (value: %s)", value.string);
            break;
    }
    printf(" at line %d\n", yylineno);
}
