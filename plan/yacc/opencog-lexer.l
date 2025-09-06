
%{
#include "opencog-parser.tab.h"
#include <string.h>
%}

%option noyywrap

%%

"ConceptNode"       { return CONCEPT_NODE; }
"PredicateNode"     { return PREDICATE_NODE; }
"NumberNode"        { return NUMBER_NODE; }
"WordNode"          { return WORD_NODE; }
"InheritanceLink"   { return INHERITANCE_LINK; }
"SimilarityLink"    { return SIMILARITY_LINK; }
"EvaluationLink"    { return EVALUATION_LINK; }
"ListLink"          { return LIST_LINK; }
"Get"               { return GET_QUERY; }
"BindLink"          { return BIND_LINK; }
"VariableList"      { return VARIABLE_LIST; }
"ImplicationLink"   { return IMPLICATION_LINK; }

"("                 { return LPAREN; }
")"                 { return RPAREN; }

\$[a-zA-Z_][a-zA-Z0-9_-]* {
    yylval.string = strdup(yytext);
    return VARIABLE;
}

[a-zA-Z_][a-zA-Z0-9_-]* {
    yylval.string = strdup(yytext);
    return IDENTIFIER;
}

\"[^"]*\" {
    yylval.string = strndup(yytext + 1, strlen(yytext) - 2);
    return STRING;
}

-?[0-9]+(\.[0-9]+)? {
    yylval.number = atof(yytext);
    return NUMBER;
}

;[^\n]*             { /* skip comments */ }
[ \t\r\n]+          { /* skip whitespace */ }

.                   { return yytext[0]; }

%%
