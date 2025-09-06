
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "opencog_ast.h"

extern int yylex();
void yyerror(const char *s);
%}

%union {
    char *string;
    int number;
    struct atom_node *atom;
    struct link_node *link;
    struct query_node *query;
}

%token <string> IDENTIFIER STRING VARIABLE
%token <number> NUMBER
%token CONCEPT_NODE PREDICATE_NODE NUMBER_NODE WORD_NODE
%token INHERITANCE_LINK SIMILARITY_LINK EVALUATION_LINK LIST_LINK
%token GET_QUERY BIND_LINK VARIABLE_LIST IMPLICATION_LINK
%token LPAREN RPAREN

%type <atom> atom atom_def
%type <link> link link_def
%type <query> query_stmt

%%

program:
    /* empty */
    | program statement
    ;

statement:
    atom_def { process_atom($1); }
    | link_def { process_link($1); }
    | query_stmt { process_query($1); }
    ;

atom_def:
    LPAREN CONCEPT_NODE STRING RPAREN {
        $$ = create_atom(CONCEPT, $3);
    }
    | LPAREN PREDICATE_NODE STRING RPAREN {
        $$ = create_atom(PREDICATE, $3);
    }
    | LPAREN NUMBER_NODE NUMBER RPAREN {
        $$ = create_atom(NUMBER_TYPE, $3);
    }
    ;

link_def:
    LPAREN INHERITANCE_LINK atom atom RPAREN {
        $$ = create_link(INHERITANCE, $3, $4);
    }
    | LPAREN SIMILARITY_LINK atom atom RPAREN {
        $$ = create_link(SIMILARITY, $3, $4);
    }
    | LPAREN EVALUATION_LINK atom atom_list RPAREN {
        $$ = create_evaluation_link($3, $4);
    }
    ;

atom:
    atom_def { $$ = $1; }
    | VARIABLE { $$ = create_variable($1); }
    ;

atom_list:
    LPAREN LIST_LINK atom_sequence RPAREN
    ;

atom_sequence:
    atom
    | atom_sequence atom
    ;

query_stmt:
    LPAREN GET_QUERY atom_pattern RPAREN {
        $$ = create_query($3);
    }
    ;

atom_pattern:
    LPAREN CONCEPT_NODE VARIABLE RPAREN {
        $$ = create_pattern(CONCEPT, $3);
    }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Parse error: %s\n", s);
}

int main() {
    return yyparse();
}
