grammar BKOOL;

@lexer::eader {
from lexererr import *
}

options {
	language = Python3;
}
// Use ANTLR to write regular expressions describing Pascal strings are made up of a sequence of
// characters between single quotes: 'string'. The single quote itself can appear as two single
// quotes back to back in a string: 'isn''t'.

program: mlist EOF;
mlist :expr etail|;
decl: decl_tail 'M' |;
decl_tail: decl 'N' | 'P' 'M' 'N';
a: b|;
b: 'f'a| ;
etail: ';' expr etail |;
stat: ID '=' expr ';' | expr ';';
defi: ID '(' ID (',' ID)* ')' '{' stat* '}';
expr:
	ID
	| INT
	| func
	| 'not' expr
	| expr 'and' expr
	| expr 'or' expr;
func: ID '(' expr (',' expr)* ')';
INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\n\r\f]+ -> skip;