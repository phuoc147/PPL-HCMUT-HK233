# Generated from d:/PPL_HCMUT/assignment3-initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,378,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,1,0,1,0,1,1,1,1,3,1,88,8,1,1,1,1,1,1,1,1,1,3,1,94,
        8,1,3,1,96,8,1,1,2,1,2,3,2,100,8,2,1,2,1,2,1,2,3,2,105,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,117,8,3,1,4,1,4,3,4,121,8,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,134,8,5,1,6,1,
        6,1,6,1,6,3,6,140,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,3,12,177,8,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,190,8,14,1,
        15,1,15,1,15,1,15,1,15,3,15,197,8,15,1,16,1,16,1,16,1,16,1,16,3,
        16,204,8,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,212,8,17,10,17,12,
        17,215,9,17,1,18,1,18,1,18,1,18,1,18,1,18,5,18,223,8,18,10,18,12,
        18,226,9,18,1,19,1,19,1,19,1,19,1,19,1,19,5,19,234,8,19,10,19,12,
        19,237,9,19,1,20,1,20,1,20,3,20,242,8,20,1,21,1,21,1,21,3,21,247,
        8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,258,8,22,
        1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,268,8,24,1,24,1,24,
        1,25,1,25,3,25,274,8,25,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,295,
        8,27,1,28,1,28,1,28,1,28,3,28,301,8,28,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,3,29,310,8,29,1,29,1,29,1,29,3,29,315,8,29,1,29,1,29,1,
        30,1,30,1,30,1,30,1,30,3,30,324,8,30,1,31,3,31,327,8,31,1,31,3,31,
        330,8,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,3,32,339,8,32,1,33,1,
        33,1,33,3,33,344,8,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,
        35,1,35,1,35,3,35,357,8,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,
        39,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,3,40,376,8,40,1,
        40,0,3,34,36,38,41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
        78,80,0,5,2,0,37,38,40,43,1,0,35,36,1,0,29,30,1,0,31,33,1,0,8,11,
        386,0,82,1,0,0,0,2,95,1,0,0,0,4,104,1,0,0,0,6,116,1,0,0,0,8,120,
        1,0,0,0,10,126,1,0,0,0,12,135,1,0,0,0,14,150,1,0,0,0,16,156,1,0,
        0,0,18,164,1,0,0,0,20,167,1,0,0,0,22,170,1,0,0,0,24,173,1,0,0,0,
        26,180,1,0,0,0,28,189,1,0,0,0,30,196,1,0,0,0,32,203,1,0,0,0,34,205,
        1,0,0,0,36,216,1,0,0,0,38,227,1,0,0,0,40,241,1,0,0,0,42,246,1,0,
        0,0,44,257,1,0,0,0,46,259,1,0,0,0,48,263,1,0,0,0,50,273,1,0,0,0,
        52,277,1,0,0,0,54,294,1,0,0,0,56,300,1,0,0,0,58,302,1,0,0,0,60,323,
        1,0,0,0,62,326,1,0,0,0,64,338,1,0,0,0,66,340,1,0,0,0,68,347,1,0,
        0,0,70,356,1,0,0,0,72,358,1,0,0,0,74,360,1,0,0,0,76,362,1,0,0,0,
        78,364,1,0,0,0,80,375,1,0,0,0,82,83,3,2,1,0,83,84,5,0,0,1,84,1,1,
        0,0,0,85,88,3,50,25,0,86,88,3,58,29,0,87,85,1,0,0,0,87,86,1,0,0,
        0,88,89,1,0,0,0,89,90,3,2,1,0,90,96,1,0,0,0,91,94,3,50,25,0,92,94,
        3,58,29,0,93,91,1,0,0,0,93,92,1,0,0,0,94,96,1,0,0,0,95,87,1,0,0,
        0,95,93,1,0,0,0,96,3,1,0,0,0,97,100,3,6,3,0,98,100,3,50,25,0,99,
        97,1,0,0,0,99,98,1,0,0,0,100,101,1,0,0,0,101,102,3,4,2,0,102,105,
        1,0,0,0,103,105,1,0,0,0,104,99,1,0,0,0,104,103,1,0,0,0,105,5,1,0,
        0,0,106,117,3,8,4,0,107,117,3,10,5,0,108,117,3,12,6,0,109,117,3,
        14,7,0,110,117,3,16,8,0,111,117,3,18,9,0,112,117,3,20,10,0,113,117,
        3,22,11,0,114,117,3,24,12,0,115,117,3,26,13,0,116,106,1,0,0,0,116,
        107,1,0,0,0,116,108,1,0,0,0,116,109,1,0,0,0,116,110,1,0,0,0,116,
        111,1,0,0,0,116,112,1,0,0,0,116,113,1,0,0,0,116,114,1,0,0,0,116,
        115,1,0,0,0,117,7,1,0,0,0,118,121,5,55,0,0,119,121,3,68,34,0,120,
        118,1,0,0,0,120,119,1,0,0,0,121,122,1,0,0,0,122,123,5,39,0,0,123,
        124,3,30,15,0,124,125,5,53,0,0,125,9,1,0,0,0,126,127,5,19,0,0,127,
        128,5,45,0,0,128,129,3,30,15,0,129,130,5,46,0,0,130,133,3,6,3,0,
        131,132,5,20,0,0,132,134,3,6,3,0,133,131,1,0,0,0,133,134,1,0,0,0,
        134,11,1,0,0,0,135,136,5,15,0,0,136,139,5,45,0,0,137,140,5,55,0,
        0,138,140,3,68,34,0,139,137,1,0,0,0,139,138,1,0,0,0,140,141,1,0,
        0,0,141,142,5,39,0,0,142,143,3,30,15,0,143,144,5,52,0,0,144,145,
        3,30,15,0,145,146,5,52,0,0,146,147,3,30,15,0,147,148,5,46,0,0,148,
        149,3,6,3,0,149,13,1,0,0,0,150,151,5,16,0,0,151,152,5,45,0,0,152,
        153,3,30,15,0,153,154,5,46,0,0,154,155,3,6,3,0,155,15,1,0,0,0,156,
        157,5,17,0,0,157,158,3,26,13,0,158,159,5,16,0,0,159,160,5,45,0,0,
        160,161,3,30,15,0,161,162,5,46,0,0,162,163,5,53,0,0,163,17,1,0,0,
        0,164,165,5,23,0,0,165,166,5,53,0,0,166,19,1,0,0,0,167,168,5,24,
        0,0,168,169,5,53,0,0,169,21,1,0,0,0,170,171,3,48,24,0,171,172,5,
        53,0,0,172,23,1,0,0,0,173,176,5,21,0,0,174,177,3,30,15,0,175,177,
        1,0,0,0,176,174,1,0,0,0,176,175,1,0,0,0,177,178,1,0,0,0,178,179,
        5,53,0,0,179,25,1,0,0,0,180,181,5,47,0,0,181,182,3,4,2,0,182,183,
        5,48,0,0,183,27,1,0,0,0,184,185,3,30,15,0,185,186,5,52,0,0,186,187,
        3,28,14,0,187,190,1,0,0,0,188,190,3,30,15,0,189,184,1,0,0,0,189,
        188,1,0,0,0,190,29,1,0,0,0,191,192,3,32,16,0,192,193,5,44,0,0,193,
        194,3,32,16,0,194,197,1,0,0,0,195,197,3,32,16,0,196,191,1,0,0,0,
        196,195,1,0,0,0,197,31,1,0,0,0,198,199,3,34,17,0,199,200,7,0,0,0,
        200,201,3,34,17,0,201,204,1,0,0,0,202,204,3,34,17,0,203,198,1,0,
        0,0,203,202,1,0,0,0,204,33,1,0,0,0,205,206,6,17,-1,0,206,207,3,36,
        18,0,207,213,1,0,0,0,208,209,10,2,0,0,209,210,7,1,0,0,210,212,3,
        36,18,0,211,208,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,
        1,0,0,0,214,35,1,0,0,0,215,213,1,0,0,0,216,217,6,18,-1,0,217,218,
        3,38,19,0,218,224,1,0,0,0,219,220,10,2,0,0,220,221,7,2,0,0,221,223,
        3,38,19,0,222,219,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,225,
        1,0,0,0,225,37,1,0,0,0,226,224,1,0,0,0,227,228,6,19,-1,0,228,229,
        3,40,20,0,229,235,1,0,0,0,230,231,10,2,0,0,231,232,7,3,0,0,232,234,
        3,40,20,0,233,230,1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,
        1,0,0,0,236,39,1,0,0,0,237,235,1,0,0,0,238,239,5,34,0,0,239,242,
        3,40,20,0,240,242,3,42,21,0,241,238,1,0,0,0,241,240,1,0,0,0,242,
        41,1,0,0,0,243,244,5,30,0,0,244,247,3,42,21,0,245,247,3,44,22,0,
        246,243,1,0,0,0,246,245,1,0,0,0,247,43,1,0,0,0,248,258,3,46,23,0,
        249,258,3,48,24,0,250,258,5,2,0,0,251,258,5,3,0,0,252,258,5,4,0,
        0,253,258,5,5,0,0,254,258,5,55,0,0,255,258,3,68,34,0,256,258,3,66,
        33,0,257,248,1,0,0,0,257,249,1,0,0,0,257,250,1,0,0,0,257,251,1,0,
        0,0,257,252,1,0,0,0,257,253,1,0,0,0,257,254,1,0,0,0,257,255,1,0,
        0,0,257,256,1,0,0,0,258,45,1,0,0,0,259,260,5,45,0,0,260,261,3,30,
        15,0,261,262,5,46,0,0,262,47,1,0,0,0,263,264,5,55,0,0,264,267,5,
        45,0,0,265,268,3,28,14,0,266,268,1,0,0,0,267,265,1,0,0,0,267,266,
        1,0,0,0,268,269,1,0,0,0,269,270,5,46,0,0,270,49,1,0,0,0,271,274,
        3,52,26,0,272,274,3,54,27,0,273,271,1,0,0,0,273,272,1,0,0,0,274,
        275,1,0,0,0,275,276,5,53,0,0,276,51,1,0,0,0,277,278,3,56,28,0,278,
        279,5,54,0,0,279,280,3,64,32,0,280,53,1,0,0,0,281,282,5,55,0,0,282,
        283,5,52,0,0,283,284,1,0,0,0,284,285,3,54,27,0,285,286,5,52,0,0,
        286,287,3,30,15,0,287,295,1,0,0,0,288,289,5,55,0,0,289,290,5,54,
        0,0,290,291,3,64,32,0,291,292,5,39,0,0,292,293,3,30,15,0,293,295,
        1,0,0,0,294,281,1,0,0,0,294,288,1,0,0,0,295,55,1,0,0,0,296,297,5,
        55,0,0,297,298,5,52,0,0,298,301,3,56,28,0,299,301,5,55,0,0,300,296,
        1,0,0,0,300,299,1,0,0,0,301,57,1,0,0,0,302,303,5,55,0,0,303,304,
        5,54,0,0,304,305,5,18,0,0,305,306,3,70,35,0,306,309,5,45,0,0,307,
        310,3,60,30,0,308,310,1,0,0,0,309,307,1,0,0,0,309,308,1,0,0,0,310,
        311,1,0,0,0,311,314,5,46,0,0,312,313,5,27,0,0,313,315,5,55,0,0,314,
        312,1,0,0,0,314,315,1,0,0,0,315,316,1,0,0,0,316,317,3,26,13,0,317,
        59,1,0,0,0,318,319,3,62,31,0,319,320,5,52,0,0,320,321,3,60,30,0,
        321,324,1,0,0,0,322,324,3,62,31,0,323,318,1,0,0,0,323,322,1,0,0,
        0,324,61,1,0,0,0,325,327,5,27,0,0,326,325,1,0,0,0,326,327,1,0,0,
        0,327,329,1,0,0,0,328,330,5,25,0,0,329,328,1,0,0,0,329,330,1,0,0,
        0,330,331,1,0,0,0,331,332,5,55,0,0,332,333,5,54,0,0,333,334,3,64,
        32,0,334,63,1,0,0,0,335,339,3,72,36,0,336,339,3,78,39,0,337,339,
        3,76,38,0,338,335,1,0,0,0,338,336,1,0,0,0,338,337,1,0,0,0,339,65,
        1,0,0,0,340,343,5,47,0,0,341,344,3,28,14,0,342,344,1,0,0,0,343,341,
        1,0,0,0,343,342,1,0,0,0,344,345,1,0,0,0,345,346,5,48,0,0,346,67,
        1,0,0,0,347,348,5,55,0,0,348,349,5,49,0,0,349,350,3,28,14,0,350,
        351,5,50,0,0,351,69,1,0,0,0,352,357,3,72,36,0,353,357,3,74,37,0,
        354,357,3,78,39,0,355,357,3,76,38,0,356,352,1,0,0,0,356,353,1,0,
        0,0,356,354,1,0,0,0,356,355,1,0,0,0,357,71,1,0,0,0,358,359,7,4,0,
        0,359,73,1,0,0,0,360,361,5,12,0,0,361,75,1,0,0,0,362,363,5,22,0,
        0,363,77,1,0,0,0,364,365,5,28,0,0,365,366,5,49,0,0,366,367,3,80,
        40,0,367,368,5,50,0,0,368,369,5,26,0,0,369,370,3,72,36,0,370,79,
        1,0,0,0,371,372,5,2,0,0,372,373,5,52,0,0,373,376,3,80,40,0,374,376,
        5,2,0,0,375,371,1,0,0,0,375,374,1,0,0,0,376,81,1,0,0,0,32,87,93,
        95,99,104,116,120,133,139,176,189,196,203,213,224,235,241,246,257,
        267,273,294,300,309,314,323,326,329,338,343,356,375
    ]

class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'boolean'", "'integer'", "'string'", "'float'", "'void'", 
                     "'false'", "'true'", "'for'", "'while'", "'do'", "'function'", 
                     "'if'", "'else'", "'return'", "'auto'", "'break'", 
                     "'continue'", "'out'", "'of'", "'inherit'", "'array'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'='", "'<'", "'<='", "'>'", "'>='", 
                     "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", 
                     "','", "';'", "':'", "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCCAPE", 
                      "BOOLEAN", "INTEGER", "STRING", "FLOAT", "VOID", "FALSE", 
                      "TRUE", "FOR", "WHILE", "DO", "FUNCTION", "IF", "ELSE", 
                      "RETURN", "AUTO", "BREAK", "CONTINUE", "OUT", "OF", 
                      "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", "ASSIGN", 
                      "LT", "LE", "GT", "GE", "CONCAT", "Lb", "Rb", "LB", 
                      "RB", "LQB", "RQB", "DOT", "COMMA", "SEMI", "COLON", 
                      "IDENTIFIERS", "UNDERSCORE", "DIGIT", "NONZERO_DIGIT", 
                      "CHAR", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decllst = 1
    RULE_stat_list = 2
    RULE_statement = 3
    RULE_assign_stat = 4
    RULE_if_stat = 5
    RULE_for_stat = 6
    RULE_while_stat = 7
    RULE_dowhile_stat = 8
    RULE_break_stat = 9
    RULE_continue_stat = 10
    RULE_fucnt_stat = 11
    RULE_return_stat = 12
    RULE_blockstat = 13
    RULE_exprlst = 14
    RULE_exp = 15
    RULE_exp1 = 16
    RULE_exp2 = 17
    RULE_exp3 = 18
    RULE_exp4 = 19
    RULE_exp5 = 20
    RULE_exp6 = 21
    RULE_exp7 = 22
    RULE_subexp = 23
    RULE_functcall = 24
    RULE_vardecl = 25
    RULE_shortvardecl = 26
    RULE_assignvardecl = 27
    RULE_idendecl = 28
    RULE_funcdecl = 29
    RULE_para_list = 30
    RULE_para_pattern = 31
    RULE_type_decl = 32
    RULE_arraylit = 33
    RULE_array_access = 34
    RULE_all_t = 35
    RULE_atomic_t = 36
    RULE_void_t = 37
    RULE_auto_t = 38
    RULE_array_t = 39
    RULE_dimensionlist = 40

    ruleNames =  [ "program", "decllst", "stat_list", "statement", "assign_stat", 
                   "if_stat", "for_stat", "while_stat", "dowhile_stat", 
                   "break_stat", "continue_stat", "fucnt_stat", "return_stat", 
                   "blockstat", "exprlst", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "subexp", "functcall", 
                   "vardecl", "shortvardecl", "assignvardecl", "idendecl", 
                   "funcdecl", "para_list", "para_pattern", "type_decl", 
                   "arraylit", "array_access", "all_t", "atomic_t", "void_t", 
                   "auto_t", "array_t", "dimensionlist" ]

    EOF = Token.EOF
    COMMENT=1
    INTLIT=2
    FLOATLIT=3
    BOOLLIT=4
    STRINGLIT=5
    UNCLOSE_STRING=6
    ILLEGAL_ESCCAPE=7
    BOOLEAN=8
    INTEGER=9
    STRING=10
    FLOAT=11
    VOID=12
    FALSE=13
    TRUE=14
    FOR=15
    WHILE=16
    DO=17
    FUNCTION=18
    IF=19
    ELSE=20
    RETURN=21
    AUTO=22
    BREAK=23
    CONTINUE=24
    OUT=25
    OF=26
    INHERIT=27
    ARRAY=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33
    NOT=34
    AND=35
    OR=36
    EQUAL=37
    NOT_EQUAL=38
    ASSIGN=39
    LT=40
    LE=41
    GT=42
    GE=43
    CONCAT=44
    Lb=45
    Rb=46
    LB=47
    RB=48
    LQB=49
    RQB=50
    DOT=51
    COMMA=52
    SEMI=53
    COLON=54
    IDENTIFIERS=55
    UNDERSCORE=56
    DIGIT=57
    NONZERO_DIGIT=58
    CHAR=59
    WS=60
    ERROR_CHAR=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllst(self):
            return self.getTypedRuleContext(MT22Parser.DecllstContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.decllst()
            self.state = 83
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllst(self):
            return self.getTypedRuleContext(MT22Parser.DecllstContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MT22Parser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_decllst




    def decllst(self):

        localctx = MT22Parser.DecllstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decllst)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 85
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 86
                    self.funcdecl()
                    pass


                self.state = 89
                self.decllst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 91
                    self.vardecl()
                    pass

                elif la_ == 2:
                    self.state = 92
                    self.funcdecl()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_list(self):
            return self.getTypedRuleContext(MT22Parser.Stat_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MT22Parser.VardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_stat_list




    def stat_list(self):

        localctx = MT22Parser.Stat_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat_list)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 17, 19, 21, 23, 24, 47, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 98
                    self.vardecl()
                    pass


                self.state = 101
                self.stat_list()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stat(self):
            return self.getTypedRuleContext(MT22Parser.Assign_statContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(MT22Parser.If_statContext,0)


        def for_stat(self):
            return self.getTypedRuleContext(MT22Parser.For_statContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(MT22Parser.While_statContext,0)


        def dowhile_stat(self):
            return self.getTypedRuleContext(MT22Parser.Dowhile_statContext,0)


        def break_stat(self):
            return self.getTypedRuleContext(MT22Parser.Break_statContext,0)


        def continue_stat(self):
            return self.getTypedRuleContext(MT22Parser.Continue_statContext,0)


        def fucnt_stat(self):
            return self.getTypedRuleContext(MT22Parser.Fucnt_statContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(MT22Parser.Return_statContext,0)


        def blockstat(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.assign_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.if_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.for_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 109
                self.while_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 110
                self.dowhile_stat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 111
                self.break_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 112
                self.continue_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 113
                self.fucnt_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 114
                self.return_stat()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 115
                self.blockstat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def array_access(self):
            return self.getTypedRuleContext(MT22Parser.Array_accessContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assign_stat




    def assign_stat(self):

        localctx = MT22Parser.Assign_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 118
                self.match(MT22Parser.IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 119
                self.array_access()
                pass


            self.state = 122
            self.match(MT22Parser.ASSIGN)
            self.state = 123
            self.exp()
            self.state = 124
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_if_stat




    def if_stat(self):

        localctx = MT22Parser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(MT22Parser.IF)
            self.state = 127
            self.match(MT22Parser.Lb)
            self.state = 128
            self.exp()
            self.state = 129
            self.match(MT22Parser.Rb)
            self.state = 130
            self.statement()
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 131
                self.match(MT22Parser.ELSE)
                self.state = 132
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def array_access(self):
            return self.getTypedRuleContext(MT22Parser.Array_accessContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_stat




    def for_stat(self):

        localctx = MT22Parser.For_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MT22Parser.FOR)
            self.state = 136
            self.match(MT22Parser.Lb)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 137
                self.match(MT22Parser.IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 138
                self.array_access()
                pass


            self.state = 141
            self.match(MT22Parser.ASSIGN)
            self.state = 142
            self.exp()
            self.state = 143
            self.match(MT22Parser.COMMA)
            self.state = 144
            self.exp()
            self.state = 145
            self.match(MT22Parser.COMMA)
            self.state = 146
            self.exp()
            self.state = 147
            self.match(MT22Parser.Rb)
            self.state = 148
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_stat




    def while_stat(self):

        localctx = MT22Parser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(MT22Parser.WHILE)
            self.state = 151
            self.match(MT22Parser.Lb)
            self.state = 152
            self.exp()
            self.state = 153
            self.match(MT22Parser.Rb)
            self.state = 154
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstat(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhile_stat




    def dowhile_stat(self):

        localctx = MT22Parser.Dowhile_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dowhile_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(MT22Parser.DO)
            self.state = 157
            self.blockstat()
            self.state = 158
            self.match(MT22Parser.WHILE)
            self.state = 159
            self.match(MT22Parser.Lb)
            self.state = 160
            self.exp()
            self.state = 161
            self.match(MT22Parser.Rb)
            self.state = 162
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_stat




    def break_stat(self):

        localctx = MT22Parser.Break_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MT22Parser.BREAK)
            self.state = 165
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_stat




    def continue_stat(self):

        localctx = MT22Parser.Continue_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(MT22Parser.CONTINUE)
            self.state = 168
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fucnt_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functcall(self):
            return self.getTypedRuleContext(MT22Parser.FunctcallContext,0)


        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_fucnt_stat




    def fucnt_stat(self):

        localctx = MT22Parser.Fucnt_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fucnt_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.functcall()
            self.state = 171
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_stat




    def return_stat(self):

        localctx = MT22Parser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MT22Parser.RETURN)
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 30, 34, 45, 47, 55]:
                self.state = 174
                self.exp()
                pass
            elif token in [53]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def stat_list(self):
            return self.getTypedRuleContext(MT22Parser.Stat_listContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstat




    def blockstat(self):

        localctx = MT22Parser.BlockstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_blockstat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(MT22Parser.LB)
            self.state = 181
            self.stat_list()
            self.state = 182
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MT22Parser.ExprlstContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exprlst




    def exprlst(self):

        localctx = MT22Parser.ExprlstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprlst)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.exp()
                self.state = 185
                self.match(MT22Parser.COMMA)
                self.state = 186
                self.exprlst()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Exp1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(MT22Parser.CONCAT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp




    def exp(self):

        localctx = MT22Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_exp)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.exp1()
                self.state = 192
                self.match(MT22Parser.CONCAT)
                self.state = 193
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Exp2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Exp2Context,i)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MT22Parser.NOT_EQUAL, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def LE(self):
            return self.getToken(MT22Parser.LE, 0)

        def GE(self):
            return self.getToken(MT22Parser.GE, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp1




    def exp1(self):

        localctx = MT22Parser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.exp2(0)
                self.state = 199
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16904991277056) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MT22Parser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(MT22Parser.Exp2Context,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 208
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 209
                    _la = self._input.LA(1)
                    if not(_la==35 or _la==36):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 210
                    self.exp3(0) 
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(MT22Parser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(MT22Parser.Exp3Context,0)


        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def ADD(self):
            return self.getToken(MT22Parser.ADD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 219
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 220
                    _la = self._input.LA(1)
                    if not(_la==29 or _la==30):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 221
                    self.exp4(0) 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(MT22Parser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(MT22Parser.Exp4Context,0)


        def MUL(self):
            return self.getToken(MT22Parser.MUL, 0)

        def DIV(self):
            return self.getToken(MT22Parser.DIV, 0)

        def MOD(self):
            return self.getToken(MT22Parser.MOD, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385536) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 232
                    self.exp5() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(MT22Parser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MT22Parser.Exp6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp5




    def exp5(self):

        localctx = MT22Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp5)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(MT22Parser.NOT)
                self.state = 239
                self.exp5()
                pass
            elif token in [2, 3, 4, 5, 30, 45, 47, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(MT22Parser.SUB, 0)

        def exp6(self):
            return self.getTypedRuleContext(MT22Parser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(MT22Parser.Exp7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp6




    def exp6(self):

        localctx = MT22Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp6)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(MT22Parser.SUB)
                self.state = 244
                self.exp6()
                pass
            elif token in [2, 3, 4, 5, 45, 47, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subexp(self):
            return self.getTypedRuleContext(MT22Parser.SubexpContext,0)


        def functcall(self):
            return self.getTypedRuleContext(MT22Parser.FunctcallContext,0)


        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def array_access(self):
            return self.getTypedRuleContext(MT22Parser.Array_accessContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(MT22Parser.ArraylitContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_exp7




    def exp7(self):

        localctx = MT22Parser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp7)
        try:
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.subexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.functcall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 250
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 251
                self.match(MT22Parser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 252
                self.match(MT22Parser.BOOLLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 253
                self.match(MT22Parser.STRINGLIT)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 254
                self.match(MT22Parser.IDENTIFIERS)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 255
                self.array_access()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 256
                self.arraylit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_subexp




    def subexp(self):

        localctx = MT22Parser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_subexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MT22Parser.Lb)
            self.state = 260
            self.exp()
            self.state = 261
            self.match(MT22Parser.Rb)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MT22Parser.ExprlstContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functcall




    def functcall(self):

        localctx = MT22Parser.FunctcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_functcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MT22Parser.IDENTIFIERS)
            self.state = 264
            self.match(MT22Parser.Lb)
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 30, 34, 45, 47, 55]:
                self.state = 265
                self.exprlst()
                pass
            elif token in [46]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 269
            self.match(MT22Parser.Rb)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MT22Parser.SEMI, 0)

        def shortvardecl(self):
            return self.getTypedRuleContext(MT22Parser.ShortvardeclContext,0)


        def assignvardecl(self):
            return self.getTypedRuleContext(MT22Parser.AssignvardeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_vardecl




    def vardecl(self):

        localctx = MT22Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 271
                self.shortvardecl()
                pass

            elif la_ == 2:
                self.state = 272
                self.assignvardecl()
                pass


            self.state = 275
            self.match(MT22Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idendecl(self):
            return self.getTypedRuleContext(MT22Parser.IdendeclContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_decl(self):
            return self.getTypedRuleContext(MT22Parser.Type_declContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_shortvardecl




    def shortvardecl(self):

        localctx = MT22Parser.ShortvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_shortvardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.idendecl()
            self.state = 278
            self.match(MT22Parser.COLON)
            self.state = 279
            self.type_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignvardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignvardecl(self):
            return self.getTypedRuleContext(MT22Parser.AssignvardeclContext,0)


        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def exp(self):
            return self.getTypedRuleContext(MT22Parser.ExpContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_decl(self):
            return self.getTypedRuleContext(MT22Parser.Type_declContext,0)


        def ASSIGN(self):
            return self.getToken(MT22Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignvardecl




    def assignvardecl(self):

        localctx = MT22Parser.AssignvardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignvardecl)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.match(MT22Parser.IDENTIFIERS)
                self.state = 282
                self.match(MT22Parser.COMMA)
                self.state = 284
                self.assignvardecl()

                self.state = 285
                self.match(MT22Parser.COMMA)
                self.state = 286
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(MT22Parser.IDENTIFIERS)
                self.state = 289
                self.match(MT22Parser.COLON)
                self.state = 290
                self.type_decl()
                self.state = 291
                self.match(MT22Parser.ASSIGN)
                self.state = 292
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdendeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def idendecl(self):
            return self.getTypedRuleContext(MT22Parser.IdendeclContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idendecl




    def idendecl(self):

        localctx = MT22Parser.IdendeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_idendecl)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(MT22Parser.IDENTIFIERS)
                self.state = 297
                self.match(MT22Parser.COMMA)
                self.state = 298
                self.idendecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(MT22Parser.IDENTIFIERS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.IDENTIFIERS)
            else:
                return self.getToken(MT22Parser.IDENTIFIERS, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def all_t(self):
            return self.getTypedRuleContext(MT22Parser.All_tContext,0)


        def Lb(self):
            return self.getToken(MT22Parser.Lb, 0)

        def Rb(self):
            return self.getToken(MT22Parser.Rb, 0)

        def blockstat(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatContext,0)


        def para_list(self):
            return self.getTypedRuleContext(MT22Parser.Para_listContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_funcdecl




    def funcdecl(self):

        localctx = MT22Parser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(MT22Parser.IDENTIFIERS)
            self.state = 303
            self.match(MT22Parser.COLON)
            self.state = 304
            self.match(MT22Parser.FUNCTION)
            self.state = 305
            self.all_t()
            self.state = 306
            self.match(MT22Parser.Lb)
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 27, 55]:
                self.state = 307
                self.para_list()
                pass
            elif token in [46]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 311
            self.match(MT22Parser.Rb)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 312
                self.match(MT22Parser.INHERIT)
                self.state = 313
                self.match(MT22Parser.IDENTIFIERS)


            self.state = 316
            self.blockstat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_pattern(self):
            return self.getTypedRuleContext(MT22Parser.Para_patternContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def para_list(self):
            return self.getTypedRuleContext(MT22Parser.Para_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_para_list




    def para_list(self):

        localctx = MT22Parser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_para_list)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.para_pattern()
                self.state = 319
                self.match(MT22Parser.COMMA)
                self.state = 320
                self.para_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.para_pattern()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_patternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def type_decl(self):
            return self.getTypedRuleContext(MT22Parser.Type_declContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_para_pattern




    def para_pattern(self):

        localctx = MT22Parser.Para_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_para_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 325
                self.match(MT22Parser.INHERIT)


            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 328
                self.match(MT22Parser.OUT)


            self.state = 331
            self.match(MT22Parser.IDENTIFIERS)
            self.state = 332
            self.match(MT22Parser.COLON)
            self.state = 333
            self.type_decl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_t(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_tContext,0)


        def array_t(self):
            return self.getTypedRuleContext(MT22Parser.Array_tContext,0)


        def auto_t(self):
            return self.getTypedRuleContext(MT22Parser.Auto_tContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_type_decl




    def type_decl(self):

        localctx = MT22Parser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_type_decl)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.atomic_t()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.array_t()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.auto_t()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MT22Parser.ExprlstContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraylit




    def arraylit(self):

        localctx = MT22Parser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arraylit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.match(MT22Parser.LB)
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5, 30, 34, 45, 47, 55]:
                self.state = 341
                self.exprlst()
                pass
            elif token in [48]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 345
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self):
            return self.getToken(MT22Parser.IDENTIFIERS, 0)

        def LQB(self):
            return self.getToken(MT22Parser.LQB, 0)

        def RQB(self):
            return self.getToken(MT22Parser.RQB, 0)

        def exprlst(self):
            return self.getTypedRuleContext(MT22Parser.ExprlstContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_access




    def array_access(self):

        localctx = MT22Parser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(MT22Parser.IDENTIFIERS)
            self.state = 348
            self.match(MT22Parser.LQB)

            self.state = 349
            self.exprlst()
            self.state = 350
            self.match(MT22Parser.RQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_t(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_tContext,0)


        def void_t(self):
            return self.getTypedRuleContext(MT22Parser.Void_tContext,0)


        def array_t(self):
            return self.getTypedRuleContext(MT22Parser.Array_tContext,0)


        def auto_t(self):
            return self.getTypedRuleContext(MT22Parser.Auto_tContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_all_t




    def all_t(self):

        localctx = MT22Parser.All_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_all_t)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.atomic_t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.void_t()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.array_t()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.auto_t()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_t




    def atomic_t(self):

        localctx = MT22Parser.Atomic_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_atomic_t)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Void_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_void_t




    def void_t(self):

        localctx = MT22Parser.Void_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_void_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MT22Parser.VOID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Auto_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_auto_t




    def auto_t(self):

        localctx = MT22Parser.Auto_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_auto_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(MT22Parser.AUTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_tContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LQB(self):
            return self.getToken(MT22Parser.LQB, 0)

        def dimensionlist(self):
            return self.getTypedRuleContext(MT22Parser.DimensionlistContext,0)


        def RQB(self):
            return self.getToken(MT22Parser.RQB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_t(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_tContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_t




    def array_t(self):

        localctx = MT22Parser.Array_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_array_t)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MT22Parser.ARRAY)
            self.state = 365
            self.match(MT22Parser.LQB)
            self.state = 366
            self.dimensionlist()
            self.state = 367
            self.match(MT22Parser.RQB)
            self.state = 368
            self.match(MT22Parser.OF)
            self.state = 369
            self.atomic_t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def dimensionlist(self):
            return self.getTypedRuleContext(MT22Parser.DimensionlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_dimensionlist




    def dimensionlist(self):

        localctx = MT22Parser.DimensionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_dimensionlist)
        try:
            self.state = 375
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.match(MT22Parser.INTLIT)
                self.state = 372
                self.match(MT22Parser.COMMA)
                self.state = 373
                self.dimensionlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(MT22Parser.INTLIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.exp2_sempred
        self._predicates[18] = self.exp3_sempred
        self._predicates[19] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




