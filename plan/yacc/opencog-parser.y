
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "opencog-ast.h"

extern int yylex();
extern void yyerror(const char *s);
extern int yylineno;

AST_Node *parse_root = NULL;
%}

%union {
    char *string;
    double number;
    AST_Node *node;
    AST_List *list;
    TruthValue *tv;
    AttentionValue *av;
}

/* Tokens */
%token <string> IDENTIFIER STRING VARIABLE_NAME
%token <number> NUMBER
%token LPAREN RPAREN LBRACKET RBRACKET LBRACE RBRACE
%token DOT COMMA SEMICOLON COLON ARROW DOUBLE_ARROW
%token PIPE AMPERSAND EXCLAMATION QUESTION STAR PLUS MINUS
%token SLASH PERCENT EQUALS NOT_EQUALS LESS_THAN GREATER_THAN
%token LESS_EQUAL GREATER_EQUAL

/* Keywords */
%token ATOMSPACE ATOM NODE LINK CONCEPT PREDICATE VARIABLE
%token INHERITANCE SIMILARITY EVALUATION EXECUTION
%token IMPLICATION EQUIVALENCE AND OR NOT TRUE FALSE
%token BIND GET PUT DEFINE LAMBDA LET IF THEN ELSE
%token COND CASE WHEN UNLESS WHILE FOR MAP FILTER REDUCE
%token PATTERN RULE SCHEMA MODULE IMPORT EXPORT

/* Precedence and associativity */
%right ARROW DOUBLE_ARROW
%left PIPE
%left AMPERSAND
%left EQUALS NOT_EQUALS
%left LESS_THAN GREATER_THAN LESS_EQUAL GREATER_EQUAL
%left PLUS MINUS
%left STAR SLASH PERCENT
%right EXCLAMATION NOT
%left DOT

/* Non-terminals */
%type <node> program statement expression atom
%type <node> node_decl link_decl atom_ref primary_expr
%type <node> unary_expr binary_expr conditional_expr
%type <node> lambda_expr application_expr pattern_expr
%type <node> definition schema_def rule_def
%type <list> expression_list outgoing_list parameter_list
%type <list> argument_list variable_list pattern_list
%type <tv> truth_value
%type <av> attention_value
%type <string> node_type link_type

%%

program
    : statement_list { parse_root = $1; }
    | /* empty */ { parse_root = NULL; }
    ;

statement_list
    : statement { $$ = create_ast_list($1); }
    | statement_list statement { $$ = append_ast_list($1, $2); }
    ;

statement
    : atomspace_decl { $$ = $1; }
    | definition { $$ = $1; }
    | expression { $$ = $1; }
    ;

atomspace_decl
    : ATOMSPACE IDENTIFIER LBRACE atom_decl_list RBRACE {
        $$ = create_atomspace_node($2, $4);
    }
    ;

atom_decl_list
    : atom_decl { $$ = create_ast_list($1); }
    | atom_decl_list atom_decl { $$ = append_ast_list($1, $2); }
    | /* empty */ { $$ = NULL; }
    ;

atom_decl
    : node_decl { $$ = $1; }
    | link_decl { $$ = $1; }
    ;

node_decl
    : node_type LPAREN STRING RPAREN {
        $$ = create_node($1, $3, NULL, NULL);
    }
    | node_type LPAREN STRING COMMA truth_value RPAREN {
        $$ = create_node($1, $3, $5, NULL);
    }
    | node_type LPAREN STRING COMMA truth_value COMMA attention_value RPAREN {
        $$ = create_node($1, $3, $5, $7);
    }
    ;

link_decl
    : link_type LPAREN outgoing_list RPAREN {
        $$ = create_link($1, $3, NULL, NULL);
    }
    | link_type LPAREN outgoing_list COMMA truth_value RPAREN {
        $$ = create_link($1, $3, $5, NULL);
    }
    | link_type LPAREN outgoing_list COMMA truth_value COMMA attention_value RPAREN {
        $$ = create_link($1, $3, $5, $7);
    }
    ;

node_type
    : CONCEPT { $$ = strdup("ConceptNode"); }
    | PREDICATE { $$ = strdup("PredicateNode"); }
    | VARIABLE { $$ = strdup("VariableNode"); }
    | IDENTIFIER { $$ = $1; }
    ;

link_type
    : INHERITANCE { $$ = strdup("InheritanceLink"); }
    | SIMILARITY { $$ = strdup("SimilarityLink"); }
    | EVALUATION { $$ = strdup("EvaluationLink"); }
    | EXECUTION { $$ = strdup("ExecutionLink"); }
    | IMPLICATION { $$ = strdup("ImplicationLink"); }
    | EQUIVALENCE { $$ = strdup("EquivalenceLink"); }
    | AND { $$ = strdup("AndLink"); }
    | OR { $$ = strdup("OrLink"); }
    | NOT { $$ = strdup("NotLink"); }
    | BIND { $$ = strdup("BindLink"); }
    | GET { $$ = strdup("GetLink"); }
    | PUT { $$ = strdup("PutLink"); }
    | IDENTIFIER { $$ = $1; }
    ;

outgoing_list
    : atom { $$ = create_ast_list($1); }
    | outgoing_list COMMA atom { $$ = append_ast_list($1, $3); }
    ;

atom
    : node_decl { $$ = $1; }
    | link_decl { $$ = $1; }
    | atom_ref { $$ = $1; }
    ;

atom_ref
    : IDENTIFIER { $$ = create_atom_ref($1); }
    | VARIABLE_NAME { $$ = create_variable_ref($1); }
    | NUMBER { $$ = create_number_node($1); }
    | STRING { $$ = create_string_node($1); }
    ;

truth_value
    : LBRACKET NUMBER COMMA NUMBER RBRACKET {
        $$ = create_truth_value($2, $4);
    }
    ;

attention_value
    : LBRACKET NUMBER COMMA NUMBER COMMA NUMBER RBRACKET {
        $$ = create_attention_value($2, $4, $6);
    }
    ;

definition
    : DEFINE IDENTIFIER expression {
        $$ = create_definition($2, NULL, $3);
    }
    | DEFINE LPAREN IDENTIFIER parameter_list RPAREN expression {
        $$ = create_definition($3, $4, $6);
    }
    | schema_def { $$ = $1; }
    | rule_def { $$ = $1; }
    ;

schema_def
    : SCHEMA IDENTIFIER LPAREN parameter_list RPAREN LBRACE schema_body RBRACE {
        $$ = create_schema($2, $4, $7);
    }
    ;

schema_body
    : schema_clause { $$ = create_ast_list($1); }
    | schema_body schema_clause { $$ = append_ast_list($1, $2); }
    | /* empty */ { $$ = NULL; }
    ;

schema_clause
    : IDENTIFIER COLON expression {
        $$ = create_schema_clause($1, $3);
    }
    ;

rule_def
    : RULE IDENTIFIER LBRACE rule_body RBRACE {
        $$ = create_rule($2, $4);
    }
    ;

rule_body
    : rule_clause { $$ = create_ast_list($1); }
    | rule_body SEMICOLON rule_clause { $$ = append_ast_list($1, $3); }
    ;

rule_clause
    : IDENTIFIER COLON expression {
        $$ = create_rule_clause($1, $3);
    }
    | IDENTIFIER COLON expression_list {
        $$ = create_rule_clause($1, create_list_node($3));
    }
    ;

parameter_list
    : parameter { $$ = create_ast_list($1); }
    | parameter_list COMMA parameter { $$ = append_ast_list($1, $3); }
    | /* empty */ { $$ = NULL; }
    ;

parameter
    : IDENTIFIER { $$ = create_parameter($1, NULL); }
    | IDENTIFIER COLON IDENTIFIER { $$ = create_parameter($1, $3); }
    ;

expression
    : primary_expr { $$ = $1; }
    | unary_expr { $$ = $1; }
    | binary_expr { $$ = $1; }
    | conditional_expr { $$ = $1; }
    | lambda_expr { $$ = $1; }
    | application_expr { $$ = $1; }
    | pattern_expr { $$ = $1; }
    ;

primary_expr
    : atom { $$ = $1; }
    | TRUE { $$ = create_boolean_node(1); }
    | FALSE { $$ = create_boolean_node(0); }
    | LPAREN expression RPAREN { $$ = $2; }
    | LPAREN expression_list RPAREN { $$ = create_list_node($2); }
    | LBRACKET expression_list RBRACKET { $$ = create_list_node($2); }
    | LBRACE expression_list RBRACE { $$ = create_set_node($2); }
    ;

unary_expr
    : NOT expression { $$ = create_unary_op("not", $2); }
    | MINUS expression { $$ = create_unary_op("minus", $2); }
    | PLUS expression { $$ = create_unary_op("plus", $2); }
    | EXCLAMATION expression { $$ = create_unary_op("!", $2); }
    ;

binary_expr
    : expression PLUS expression { $$ = create_binary_op("+", $1, $3); }
    | expression MINUS expression { $$ = create_binary_op("-", $1, $3); }
    | expression STAR expression { $$ = create_binary_op("*", $1, $3); }
    | expression SLASH expression { $$ = create_binary_op("/", $1, $3); }
    | expression PERCENT expression { $$ = create_binary_op("%", $1, $3); }
    | expression EQUALS expression { $$ = create_binary_op("=", $1, $3); }
    | expression NOT_EQUALS expression { $$ = create_binary_op("!=", $1, $3); }
    | expression LESS_THAN expression { $$ = create_binary_op("<", $1, $3); }
    | expression GREATER_THAN expression { $$ = create_binary_op(">", $1, $3); }
    | expression LESS_EQUAL expression { $$ = create_binary_op("<=", $1, $3); }
    | expression GREATER_EQUAL expression { $$ = create_binary_op(">=", $1, $3); }
    | expression AMPERSAND expression { $$ = create_binary_op("&", $1, $3); }
    | expression PIPE expression { $$ = create_binary_op("|", $1, $3); }
    | expression ARROW expression { $$ = create_binary_op("->", $1, $3); }
    | expression DOUBLE_ARROW expression { $$ = create_binary_op("=>", $1, $3); }
    ;

conditional_expr
    : IF expression THEN expression ELSE expression {
        $$ = create_conditional($2, $4, $6);
    }
    | COND LBRACE cond_clause_list RBRACE {
        $$ = create_cond($3);
    }
    ;

cond_clause_list
    : cond_clause { $$ = create_ast_list($1); }
    | cond_clause_list cond_clause { $$ = append_ast_list($1, $2); }
    ;

cond_clause
    : LBRACKET expression ARROW expression RBRACKET {
        $$ = create_cond_clause($2, $4);
    }
    ;

lambda_expr
    : LAMBDA LPAREN parameter_list RPAREN expression {
        $$ = create_lambda($3, $5);
    }
    | LAMBDA IDENTIFIER expression {
        AST_List *params = create_ast_list(create_parameter($2, NULL));
        $$ = create_lambda(params, $3);
    }
    ;

application_expr
    : expression LPAREN argument_list RPAREN {
        $$ = create_application($1, $3);
    }
    ;

argument_list
    : expression { $$ = create_ast_list($1); }
    | argument_list COMMA expression { $$ = append_ast_list($1, $3); }
    | /* empty */ { $$ = NULL; }
    ;

expression_list
    : expression { $$ = create_ast_list($1); }
    | expression_list COMMA expression { $$ = append_ast_list($1, $3); }
    | /* empty */ { $$ = NULL; }
    ;

pattern_expr
    : PATTERN LBRACE pattern_body RBRACE {
        $$ = create_pattern($3);
    }
    | GET expression {
        $$ = create_get_link($2);
    }
    | BIND LPAREN variable_list COMMA expression COMMA expression RPAREN {
        $$ = create_bind_link($3, $5, $7);
    }
    ;

pattern_body
    : pattern_clause { $$ = create_ast_list($1); }
    | pattern_body SEMICOLON pattern_clause { $$ = append_ast_list($1, $3); }
    | /* empty */ { $$ = NULL; }
    ;

pattern_clause
    : IDENTIFIER COLON expression {
        $$ = create_pattern_clause($1, $3);
    }
    | IDENTIFIER COLON variable_list {
        $$ = create_pattern_clause($1, create_list_node($3));
    }
    ;

variable_list
    : VARIABLE_NAME { $$ = create_ast_list(create_variable_ref($1)); }
    | variable_list COMMA VARIABLE_NAME { 
        $$ = append_ast_list($1, create_variable_ref($3)); 
    }
    | LPAREN variable_list RPAREN { $$ = $2; }
    | /* empty */ { $$ = NULL; }
    ;

pattern_list
    : pattern { $$ = create_ast_list($1); }
    | pattern_list COMMA pattern { $$ = append_ast_list($1, $3); }
    | /* empty */ { $$ = NULL; }
    ;

pattern
    : atom { $$ = $1; }
    | VARIABLE_NAME { $$ = create_variable_ref($1); }
    | STAR { $$ = create_wildcard("*"); }
    | QUESTION { $$ = create_wildcard("?"); }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Parse error at line %d: %s\n", yylineno, s);
}

AST_Node *parse_opencog(const char *input) {
    yy_scan_string(input);
    yyparse();
    return parse_root;
}
