/* 2212714 */
grammar MT22;

@lexer::header {
from lexererr import *
import re
}

options{
	language = Python3;
}

program: decllst EOF;

decllst: (vardecl | funcdecl) decllst | (vardecl | funcdecl);
/* *****STATEMENTS***** */
stat_list: (statement | vardecl) stat_list |;
statement:
	assign_stat
	| if_stat
	| for_stat
	| while_stat
	| dowhile_stat
	| break_stat
	| continue_stat
	| fucnt_stat
	| return_stat
	| blockstat;
assign_stat: (IDENTIFIERS | array_access) ASSIGN exp SEMI;
if_stat: IF Lb exp Rb statement (ELSE statement)?;
for_stat:
	FOR Lb (IDENTIFIERS | array_access) ASSIGN exp COMMA exp COMMA exp Rb statement;
while_stat: WHILE Lb exp Rb statement;
dowhile_stat: DO blockstat WHILE Lb exp Rb SEMI;
break_stat: BREAK SEMI;
continue_stat: CONTINUE SEMI;
fucnt_stat: functcall SEMI;
return_stat: RETURN (exp |) SEMI;
blockstat: LB stat_list RB;



/* *****EXPRESSIONS***** */
exprlst: (exp COMMA exprlst) | exp;
exp: (exp1 CONCAT exp1) | exp1;

exp1: exp2 (EQUAL | NOT_EQUAL | LT | LE | GE | GT) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (SUB | ADD) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7:
	subexp
	| functcall
	| INTLIT
	| FLOATLIT
	| BOOLLIT
	| STRINGLIT
	| IDENTIFIERS
	| array_access
	| arraylit;
subexp: Lb exp Rb;
functcall: IDENTIFIERS Lb (exprlst |) Rb;

/* *****DECLARATIONS***** */
vardecl: (shortvardecl | assignvardecl) SEMI;
shortvardecl: idendecl COLON type_decl;
assignvardecl: (IDENTIFIERS COMMA) assignvardecl (COMMA exp)
	| IDENTIFIERS COLON type_decl ASSIGN exp;
idendecl: IDENTIFIERS COMMA idendecl | IDENTIFIERS;

funcdecl:
	IDENTIFIERS COLON FUNCTION all_t Lb (para_list |) Rb (
		INHERIT IDENTIFIERS
	)? blockstat;
para_list: para_pattern COMMA para_list | para_pattern;
para_pattern: INHERIT? OUT? IDENTIFIERS COLON type_decl;
type_decl: atomic_t | array_t | auto_t;

//CHARACTER SETS ??
COMMENT: (('/*' .*? '*/') | ('//' ~[\r\n]*)) -> skip;

/* *****LITERALS***** */
INTLIT: ('0' | (NONZERO_DIGIT DIGIT* (UNDERSCORE DIGIT+)*)) {self.text = self.text.replace("_","")};
FLOATLIT: (
		(INTLIT DEC EXP)
		| (INTLIT DEC)
		| (DEC EXP)
		| (INTLIT EXP)
		| DEC
	) {self.text = self.text.replace("_","")};

fragment DEC: '.' DIGIT*;
fragment EXP: [eE] [-+]? DIGIT+;
BOOLLIT: TRUE | FALSE;
STRINGLIT:
	UNCLOSE_STRING '"' {index = self.text.find('\n')
if index != -1: raise UncloseString(self.text[1:index-1])
else: self.text = self.text[1:-1]};
UNCLOSE_STRING:
	'"' (ECS | ~[\\"])* { raise UncloseString(self.text[1:]) };
ILLEGAL_ESCCAPE:
	UNCLOSE_STRING ILLEGAL_ESC { raise IllegalEscape(self.text[1:]) };
fragment ECS: '\\' [bfrnt'\\"];
fragment NEWLINE: '\\' 'n';
fragment ILLEGAL_ESC: '\\' ~[bfrnt'\\"];
arraylit: LB (exprlst |) RB;
array_access: IDENTIFIERS LQB (exprlst) RQB;
/* *****TYPE SYSTEMS***** */
all_t: atomic_t | void_t | array_t | auto_t;
atomic_t: INTEGER | BOOLEAN | FLOAT | STRING;
void_t: VOID;
auto_t: AUTO;
array_t: ARRAY LQB dimensionlist RQB OF atomic_t;
dimensionlist: INTLIT COMMA dimensionlist | INTLIT;
/* *****KEYWORD***** */
BOOLEAN: 'boolean';
INTEGER: 'integer';
STRING: 'string';
FLOAT: 'float';
VOID: 'void';
FALSE: 'false';
TRUE: 'true';
FOR: 'for';
WHILE: 'while';
DO: 'do';
FUNCTION: 'function';
IF: 'if';
ELSE: 'else';
RETURN: 'return';
AUTO: 'auto';
BREAK: 'break';
CONTINUE: 'continue';
OUT: 'out';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';
/* ***** Operator ***** */
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
ASSIGN: '=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';
CONCAT: '::';
/*********** Seperators *******************/
Lb: '(';
Rb: ')';
LB: '{';
RB: '}';
LQB: '[';
RQB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
IDENTIFIERS: (CHAR | UNDERSCORE) (CHAR | UNDERSCORE | DIGIT)*;

UNDERSCORE: '_';
DIGIT: [0-9];
NONZERO_DIGIT: [1-9];
CHAR: [a-zA-Z];

WS: [ \t\r\n\f\b] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};