
grammar OpenCogAtomese;

program: statement* EOF;

statement: atomDefinition
         | linkDefinition  
         | queryStatement
         | ruleDefinition
         | schemeExpression;

atomDefinition: '(' atomType atomName ')';
linkDefinition: '(' linkType atom+ ')';
queryStatement: '(' 'Get' atomPattern ')';
ruleDefinition: '(' 'BindLink' variableDecl implicationLink ')';

atomType: 'ConceptNode' | 'PredicateNode' | 'NumberNode' | 'WordNode';
linkType: 'InheritanceLink' | 'SimilarityLink' | 'EvaluationLink' | 'ListLink';

atomPattern: '(' atomType (VARIABLE | atomName) ')';
variableDecl: '(' 'VariableList' variable+ ')';
implicationLink: '(' 'ImplicationLink' premise conclusion ')';

premise: atom | linkDefinition;
conclusion: atom | linkDefinition;

atom: '(' atomType atomName ')'
    | VARIABLE;

atomName: STRING | IDENTIFIER;
variable: '(' 'VariableNode' STRING ')';

schemeExpression: '(' schemeFunction argument* ')';
schemeFunction: IDENTIFIER;
argument: atom | linkDefinition | STRING | NUMBER | schemeExpression;

VARIABLE: '$' IDENTIFIER;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_-]*;
STRING: '"' (~["\r\n])* '"';
NUMBER: '-'? [0-9]+ ('.' [0-9]+)?;
COMMENT: ';' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
