# Generated from d:/PPL_HCMUT/assignment3-initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
import re


def serializedATN():
    return [
        4,0,71,589,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,2,73,7,73,2,74,7,74,2,75,7,75,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,5,10,273,8,10,10,10,12,10,276,9,10,1,10,1,10,1,10,1,10,
        1,10,1,10,5,10,284,8,10,10,10,12,10,287,9,10,3,10,289,8,10,1,10,
        1,10,1,11,1,11,1,11,5,11,296,8,11,10,11,12,11,299,9,11,1,11,1,11,
        4,11,303,8,11,11,11,12,11,304,5,11,307,8,11,10,11,12,11,310,9,11,
        3,11,312,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,3,12,330,8,12,1,12,1,12,1,13,1,13,
        5,13,336,8,13,10,13,12,13,339,9,13,1,14,1,14,3,14,343,8,14,1,14,
        4,14,346,8,14,11,14,12,14,347,1,15,1,15,3,15,352,8,15,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,5,17,361,8,17,10,17,12,17,364,9,17,1,17,
        1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,
        1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,
        1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,39,
        1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,
        1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,
        1,46,1,46,1,47,1,47,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,50,1,51,
        1,51,1,51,1,52,1,52,1,52,1,53,1,53,1,54,1,54,1,55,1,55,1,55,1,56,
        1,56,1,57,1,57,1,57,1,58,1,58,1,58,1,59,1,59,1,60,1,60,1,61,1,61,
        1,62,1,62,1,63,1,63,1,64,1,64,1,65,1,65,1,66,1,66,1,67,1,67,1,68,
        1,68,1,69,1,69,3,69,565,8,69,1,69,1,69,1,69,5,69,570,8,69,10,69,
        12,69,573,9,69,1,70,1,70,1,71,1,71,1,72,1,72,1,73,1,73,1,74,1,74,
        1,74,1,74,1,75,1,75,1,75,1,274,0,76,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,0,29,0,31,14,33,15,35,16,
        37,17,39,0,41,0,43,0,45,18,47,19,49,20,51,21,53,22,55,23,57,24,59,
        25,61,26,63,27,65,28,67,29,69,30,71,31,73,32,75,33,77,34,79,35,81,
        36,83,37,85,38,87,39,89,40,91,41,93,42,95,43,97,44,99,45,101,46,
        103,47,105,48,107,49,109,50,111,51,113,52,115,53,117,54,119,55,121,
        56,123,57,125,58,127,59,129,60,131,61,133,62,135,63,137,64,139,65,
        141,66,143,67,145,68,147,69,149,70,151,71,1,0,9,2,0,10,10,13,13,
        2,0,69,69,101,101,2,0,43,43,45,45,2,0,34,34,92,92,8,0,34,34,39,39,
        92,92,98,98,102,102,110,110,114,114,116,116,1,0,48,57,1,0,49,57,
        2,0,65,90,97,122,3,0,8,10,12,13,32,32,604,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,
        0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,
        0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,
        0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,
        0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,
        0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,
        0,0,105,1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,
        1,0,0,0,0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,
        0,123,1,0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,
        0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,0,139,1,0,0,0,0,
        141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,0,147,1,0,0,0,0,149,1,0,
        0,0,0,151,1,0,0,0,1,153,1,0,0,0,3,165,1,0,0,0,5,178,1,0,0,0,7,188,
        1,0,0,0,9,199,1,0,0,0,11,211,1,0,0,0,13,224,1,0,0,0,15,235,1,0,0,
        0,17,247,1,0,0,0,19,253,1,0,0,0,21,288,1,0,0,0,23,311,1,0,0,0,25,
        329,1,0,0,0,27,333,1,0,0,0,29,340,1,0,0,0,31,351,1,0,0,0,33,353,
        1,0,0,0,35,357,1,0,0,0,37,367,1,0,0,0,39,371,1,0,0,0,41,374,1,0,
        0,0,43,377,1,0,0,0,45,380,1,0,0,0,47,388,1,0,0,0,49,396,1,0,0,0,
        51,403,1,0,0,0,53,409,1,0,0,0,55,414,1,0,0,0,57,420,1,0,0,0,59,425,
        1,0,0,0,61,429,1,0,0,0,63,435,1,0,0,0,65,438,1,0,0,0,67,447,1,0,
        0,0,69,450,1,0,0,0,71,455,1,0,0,0,73,462,1,0,0,0,75,467,1,0,0,0,
        77,473,1,0,0,0,79,482,1,0,0,0,81,486,1,0,0,0,83,489,1,0,0,0,85,497,
        1,0,0,0,87,503,1,0,0,0,89,505,1,0,0,0,91,507,1,0,0,0,93,509,1,0,
        0,0,95,511,1,0,0,0,97,513,1,0,0,0,99,515,1,0,0,0,101,518,1,0,0,0,
        103,521,1,0,0,0,105,524,1,0,0,0,107,527,1,0,0,0,109,529,1,0,0,0,
        111,531,1,0,0,0,113,534,1,0,0,0,115,536,1,0,0,0,117,539,1,0,0,0,
        119,542,1,0,0,0,121,544,1,0,0,0,123,546,1,0,0,0,125,548,1,0,0,0,
        127,550,1,0,0,0,129,552,1,0,0,0,131,554,1,0,0,0,133,556,1,0,0,0,
        135,558,1,0,0,0,137,560,1,0,0,0,139,564,1,0,0,0,141,574,1,0,0,0,
        143,576,1,0,0,0,145,578,1,0,0,0,147,580,1,0,0,0,149,582,1,0,0,0,
        151,586,1,0,0,0,153,154,5,114,0,0,154,155,5,101,0,0,155,156,5,97,
        0,0,156,157,5,100,0,0,157,158,5,73,0,0,158,159,5,110,0,0,159,160,
        5,116,0,0,160,161,5,101,0,0,161,162,5,103,0,0,162,163,5,101,0,0,
        163,164,5,114,0,0,164,2,1,0,0,0,165,166,5,112,0,0,166,167,5,114,
        0,0,167,168,5,105,0,0,168,169,5,110,0,0,169,170,5,116,0,0,170,171,
        5,73,0,0,171,172,5,110,0,0,172,173,5,116,0,0,173,174,5,101,0,0,174,
        175,5,103,0,0,175,176,5,101,0,0,176,177,5,114,0,0,177,4,1,0,0,0,
        178,179,5,114,0,0,179,180,5,101,0,0,180,181,5,97,0,0,181,182,5,100,
        0,0,182,183,5,70,0,0,183,184,5,108,0,0,184,185,5,111,0,0,185,186,
        5,97,0,0,186,187,5,116,0,0,187,6,1,0,0,0,188,189,5,112,0,0,189,190,
        5,114,0,0,190,191,5,105,0,0,191,192,5,110,0,0,192,193,5,116,0,0,
        193,194,5,70,0,0,194,195,5,108,0,0,195,196,5,111,0,0,196,197,5,97,
        0,0,197,198,5,116,0,0,198,8,1,0,0,0,199,200,5,114,0,0,200,201,5,
        101,0,0,201,202,5,97,0,0,202,203,5,100,0,0,203,204,5,66,0,0,204,
        205,5,111,0,0,205,206,5,111,0,0,206,207,5,108,0,0,207,208,5,101,
        0,0,208,209,5,97,0,0,209,210,5,110,0,0,210,10,1,0,0,0,211,212,5,
        112,0,0,212,213,5,114,0,0,213,214,5,105,0,0,214,215,5,110,0,0,215,
        216,5,116,0,0,216,217,5,66,0,0,217,218,5,111,0,0,218,219,5,111,0,
        0,219,220,5,108,0,0,220,221,5,101,0,0,221,222,5,97,0,0,222,223,5,
        110,0,0,223,12,1,0,0,0,224,225,5,114,0,0,225,226,5,101,0,0,226,227,
        5,97,0,0,227,228,5,100,0,0,228,229,5,83,0,0,229,230,5,116,0,0,230,
        231,5,114,0,0,231,232,5,105,0,0,232,233,5,110,0,0,233,234,5,103,
        0,0,234,14,1,0,0,0,235,236,5,112,0,0,236,237,5,114,0,0,237,238,5,
        105,0,0,238,239,5,110,0,0,239,240,5,116,0,0,240,241,5,83,0,0,241,
        242,5,116,0,0,242,243,5,114,0,0,243,244,5,105,0,0,244,245,5,110,
        0,0,245,246,5,103,0,0,246,16,1,0,0,0,247,248,5,115,0,0,248,249,5,
        117,0,0,249,250,5,112,0,0,250,251,5,101,0,0,251,252,5,114,0,0,252,
        18,1,0,0,0,253,254,5,112,0,0,254,255,5,114,0,0,255,256,5,101,0,0,
        256,257,5,118,0,0,257,258,5,101,0,0,258,259,5,110,0,0,259,260,5,
        116,0,0,260,261,5,68,0,0,261,262,5,101,0,0,262,263,5,102,0,0,263,
        264,5,97,0,0,264,265,5,117,0,0,265,266,5,108,0,0,266,267,5,116,0,
        0,267,20,1,0,0,0,268,269,5,47,0,0,269,270,5,42,0,0,270,274,1,0,0,
        0,271,273,9,0,0,0,272,271,1,0,0,0,273,276,1,0,0,0,274,275,1,0,0,
        0,274,272,1,0,0,0,275,277,1,0,0,0,276,274,1,0,0,0,277,278,5,42,0,
        0,278,289,5,47,0,0,279,280,5,47,0,0,280,281,5,47,0,0,281,285,1,0,
        0,0,282,284,8,0,0,0,283,282,1,0,0,0,284,287,1,0,0,0,285,283,1,0,
        0,0,285,286,1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,288,268,1,0,
        0,0,288,279,1,0,0,0,289,290,1,0,0,0,290,291,6,10,0,0,291,22,1,0,
        0,0,292,312,5,48,0,0,293,297,3,145,72,0,294,296,3,143,71,0,295,294,
        1,0,0,0,296,299,1,0,0,0,297,295,1,0,0,0,297,298,1,0,0,0,298,308,
        1,0,0,0,299,297,1,0,0,0,300,302,3,141,70,0,301,303,3,143,71,0,302,
        301,1,0,0,0,303,304,1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,
        307,1,0,0,0,306,300,1,0,0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,
        309,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,311,292,1,0,0,0,311,
        293,1,0,0,0,312,313,1,0,0,0,313,314,6,11,1,0,314,24,1,0,0,0,315,
        316,3,23,11,0,316,317,3,27,13,0,317,318,3,29,14,0,318,330,1,0,0,
        0,319,320,3,23,11,0,320,321,3,27,13,0,321,330,1,0,0,0,322,323,3,
        27,13,0,323,324,3,29,14,0,324,330,1,0,0,0,325,326,3,23,11,0,326,
        327,3,29,14,0,327,330,1,0,0,0,328,330,3,27,13,0,329,315,1,0,0,0,
        329,319,1,0,0,0,329,322,1,0,0,0,329,325,1,0,0,0,329,328,1,0,0,0,
        330,331,1,0,0,0,331,332,6,12,2,0,332,26,1,0,0,0,333,337,5,46,0,0,
        334,336,3,143,71,0,335,334,1,0,0,0,336,339,1,0,0,0,337,335,1,0,0,
        0,337,338,1,0,0,0,338,28,1,0,0,0,339,337,1,0,0,0,340,342,7,1,0,0,
        341,343,7,2,0,0,342,341,1,0,0,0,342,343,1,0,0,0,343,345,1,0,0,0,
        344,346,3,143,71,0,345,344,1,0,0,0,346,347,1,0,0,0,347,345,1,0,0,
        0,347,348,1,0,0,0,348,30,1,0,0,0,349,352,3,57,28,0,350,352,3,55,
        27,0,351,349,1,0,0,0,351,350,1,0,0,0,352,32,1,0,0,0,353,354,3,35,
        17,0,354,355,5,34,0,0,355,356,6,16,3,0,356,34,1,0,0,0,357,362,5,
        34,0,0,358,361,3,39,19,0,359,361,8,3,0,0,360,358,1,0,0,0,360,359,
        1,0,0,0,361,364,1,0,0,0,362,360,1,0,0,0,362,363,1,0,0,0,363,365,
        1,0,0,0,364,362,1,0,0,0,365,366,6,17,4,0,366,36,1,0,0,0,367,368,
        3,35,17,0,368,369,3,43,21,0,369,370,6,18,5,0,370,38,1,0,0,0,371,
        372,5,92,0,0,372,373,7,4,0,0,373,40,1,0,0,0,374,375,5,92,0,0,375,
        376,5,110,0,0,376,42,1,0,0,0,377,378,5,92,0,0,378,379,8,4,0,0,379,
        44,1,0,0,0,380,381,5,98,0,0,381,382,5,111,0,0,382,383,5,111,0,0,
        383,384,5,108,0,0,384,385,5,101,0,0,385,386,5,97,0,0,386,387,5,110,
        0,0,387,46,1,0,0,0,388,389,5,105,0,0,389,390,5,110,0,0,390,391,5,
        116,0,0,391,392,5,101,0,0,392,393,5,103,0,0,393,394,5,101,0,0,394,
        395,5,114,0,0,395,48,1,0,0,0,396,397,5,115,0,0,397,398,5,116,0,0,
        398,399,5,114,0,0,399,400,5,105,0,0,400,401,5,110,0,0,401,402,5,
        103,0,0,402,50,1,0,0,0,403,404,5,102,0,0,404,405,5,108,0,0,405,406,
        5,111,0,0,406,407,5,97,0,0,407,408,5,116,0,0,408,52,1,0,0,0,409,
        410,5,118,0,0,410,411,5,111,0,0,411,412,5,105,0,0,412,413,5,100,
        0,0,413,54,1,0,0,0,414,415,5,102,0,0,415,416,5,97,0,0,416,417,5,
        108,0,0,417,418,5,115,0,0,418,419,5,101,0,0,419,56,1,0,0,0,420,421,
        5,116,0,0,421,422,5,114,0,0,422,423,5,117,0,0,423,424,5,101,0,0,
        424,58,1,0,0,0,425,426,5,102,0,0,426,427,5,111,0,0,427,428,5,114,
        0,0,428,60,1,0,0,0,429,430,5,119,0,0,430,431,5,104,0,0,431,432,5,
        105,0,0,432,433,5,108,0,0,433,434,5,101,0,0,434,62,1,0,0,0,435,436,
        5,100,0,0,436,437,5,111,0,0,437,64,1,0,0,0,438,439,5,102,0,0,439,
        440,5,117,0,0,440,441,5,110,0,0,441,442,5,99,0,0,442,443,5,116,0,
        0,443,444,5,105,0,0,444,445,5,111,0,0,445,446,5,110,0,0,446,66,1,
        0,0,0,447,448,5,105,0,0,448,449,5,102,0,0,449,68,1,0,0,0,450,451,
        5,101,0,0,451,452,5,108,0,0,452,453,5,115,0,0,453,454,5,101,0,0,
        454,70,1,0,0,0,455,456,5,114,0,0,456,457,5,101,0,0,457,458,5,116,
        0,0,458,459,5,117,0,0,459,460,5,114,0,0,460,461,5,110,0,0,461,72,
        1,0,0,0,462,463,5,97,0,0,463,464,5,117,0,0,464,465,5,116,0,0,465,
        466,5,111,0,0,466,74,1,0,0,0,467,468,5,98,0,0,468,469,5,114,0,0,
        469,470,5,101,0,0,470,471,5,97,0,0,471,472,5,107,0,0,472,76,1,0,
        0,0,473,474,5,99,0,0,474,475,5,111,0,0,475,476,5,110,0,0,476,477,
        5,116,0,0,477,478,5,105,0,0,478,479,5,110,0,0,479,480,5,117,0,0,
        480,481,5,101,0,0,481,78,1,0,0,0,482,483,5,111,0,0,483,484,5,117,
        0,0,484,485,5,116,0,0,485,80,1,0,0,0,486,487,5,111,0,0,487,488,5,
        102,0,0,488,82,1,0,0,0,489,490,5,105,0,0,490,491,5,110,0,0,491,492,
        5,104,0,0,492,493,5,101,0,0,493,494,5,114,0,0,494,495,5,105,0,0,
        495,496,5,116,0,0,496,84,1,0,0,0,497,498,5,97,0,0,498,499,5,114,
        0,0,499,500,5,114,0,0,500,501,5,97,0,0,501,502,5,121,0,0,502,86,
        1,0,0,0,503,504,5,43,0,0,504,88,1,0,0,0,505,506,5,45,0,0,506,90,
        1,0,0,0,507,508,5,42,0,0,508,92,1,0,0,0,509,510,5,47,0,0,510,94,
        1,0,0,0,511,512,5,37,0,0,512,96,1,0,0,0,513,514,5,33,0,0,514,98,
        1,0,0,0,515,516,5,38,0,0,516,517,5,38,0,0,517,100,1,0,0,0,518,519,
        5,124,0,0,519,520,5,124,0,0,520,102,1,0,0,0,521,522,5,61,0,0,522,
        523,5,61,0,0,523,104,1,0,0,0,524,525,5,33,0,0,525,526,5,61,0,0,526,
        106,1,0,0,0,527,528,5,61,0,0,528,108,1,0,0,0,529,530,5,60,0,0,530,
        110,1,0,0,0,531,532,5,60,0,0,532,533,5,61,0,0,533,112,1,0,0,0,534,
        535,5,62,0,0,535,114,1,0,0,0,536,537,5,62,0,0,537,538,5,61,0,0,538,
        116,1,0,0,0,539,540,5,58,0,0,540,541,5,58,0,0,541,118,1,0,0,0,542,
        543,5,40,0,0,543,120,1,0,0,0,544,545,5,41,0,0,545,122,1,0,0,0,546,
        547,5,123,0,0,547,124,1,0,0,0,548,549,5,125,0,0,549,126,1,0,0,0,
        550,551,5,91,0,0,551,128,1,0,0,0,552,553,5,93,0,0,553,130,1,0,0,
        0,554,555,5,46,0,0,555,132,1,0,0,0,556,557,5,44,0,0,557,134,1,0,
        0,0,558,559,5,59,0,0,559,136,1,0,0,0,560,561,5,58,0,0,561,138,1,
        0,0,0,562,565,3,147,73,0,563,565,3,141,70,0,564,562,1,0,0,0,564,
        563,1,0,0,0,565,571,1,0,0,0,566,570,3,147,73,0,567,570,3,141,70,
        0,568,570,3,143,71,0,569,566,1,0,0,0,569,567,1,0,0,0,569,568,1,0,
        0,0,570,573,1,0,0,0,571,569,1,0,0,0,571,572,1,0,0,0,572,140,1,0,
        0,0,573,571,1,0,0,0,574,575,5,95,0,0,575,142,1,0,0,0,576,577,7,5,
        0,0,577,144,1,0,0,0,578,579,7,6,0,0,579,146,1,0,0,0,580,581,7,7,
        0,0,581,148,1,0,0,0,582,583,7,8,0,0,583,584,1,0,0,0,584,585,6,74,
        0,0,585,150,1,0,0,0,586,587,9,0,0,0,587,588,6,75,6,0,588,152,1,0,
        0,0,18,0,274,285,288,297,304,308,311,329,337,342,347,351,360,362,
        564,569,571,7,6,0,0,1,11,0,1,12,1,1,16,2,1,17,3,1,18,4,1,75,5
    ]

class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    COMMENT = 11
    INTLIT = 12
    FLOATLIT = 13
    BOOLLIT = 14
    STRINGLIT = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCCAPE = 17
    BOOLEAN = 18
    INTEGER = 19
    STRING = 20
    FLOAT = 21
    VOID = 22
    FALSE = 23
    TRUE = 24
    FOR = 25
    WHILE = 26
    DO = 27
    FUNCTION = 28
    IF = 29
    ELSE = 30
    RETURN = 31
    AUTO = 32
    BREAK = 33
    CONTINUE = 34
    OUT = 35
    OF = 36
    INHERIT = 37
    ARRAY = 38
    ADD = 39
    SUB = 40
    MUL = 41
    DIV = 42
    MOD = 43
    NOT = 44
    AND = 45
    OR = 46
    EQUAL = 47
    NOT_EQUAL = 48
    ASSIGN = 49
    LT = 50
    LE = 51
    GT = 52
    GE = 53
    CONCAT = 54
    Lb = 55
    Rb = 56
    LB = 57
    RB = 58
    LQB = 59
    RQB = 60
    DOT = 61
    COMMA = 62
    SEMI = 63
    COLON = 64
    IDENTIFIERS = 65
    UNDERSCORE = 66
    DIGIT = 67
    NONZERO_DIGIT = 68
    CHAR = 69
    WS = 70
    ERROR_CHAR = 71

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'printFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'boolean'", "'integer'", "'string'", 
            "'float'", "'void'", "'false'", "'true'", "'for'", "'while'", 
            "'do'", "'function'", "'if'", "'else'", "'return'", "'auto'", 
            "'break'", "'continue'", "'out'", "'of'", "'inherit'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'='", "'<'", "'<='", "'>'", "'>='", "'::'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "'.'", "','", "';'", "':'", 
            "'_'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCCAPE", "BOOLEAN", "INTEGER", "STRING", "FLOAT", 
            "VOID", "FALSE", "TRUE", "FOR", "WHILE", "DO", "FUNCTION", "IF", 
            "ELSE", "RETURN", "AUTO", "BREAK", "CONTINUE", "OUT", "OF", 
            "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "EQUAL", "NOT_EQUAL", "ASSIGN", "LT", "LE", "GT", 
            "GE", "CONCAT", "Lb", "Rb", "LB", "RB", "LQB", "RQB", "DOT", 
            "COMMA", "SEMI", "COLON", "IDENTIFIERS", "UNDERSCORE", "DIGIT", 
            "NONZERO_DIGIT", "CHAR", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "COMMENT", "INTLIT", "FLOATLIT", 
                  "DEC", "EXP", "BOOLLIT", "STRINGLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCCAPE", "ECS", "NEWLINE", "ILLEGAL_ESC", "BOOLEAN", 
                  "INTEGER", "STRING", "FLOAT", "VOID", "FALSE", "TRUE", 
                  "FOR", "WHILE", "DO", "FUNCTION", "IF", "ELSE", "RETURN", 
                  "AUTO", "BREAK", "CONTINUE", "OUT", "OF", "INHERIT", "ARRAY", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "NOT_EQUAL", "ASSIGN", "LT", "LE", "GT", "GE", 
                  "CONCAT", "Lb", "Rb", "LB", "RB", "LQB", "RQB", "DOT", 
                  "COMMA", "SEMI", "COLON", "IDENTIFIERS", "UNDERSCORE", 
                  "DIGIT", "NONZERO_DIGIT", "CHAR", "WS", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[11] = self.INTLIT_action 
            actions[12] = self.FLOATLIT_action 
            actions[16] = self.STRINGLIT_action 
            actions[17] = self.UNCLOSE_STRING_action 
            actions[18] = self.ILLEGAL_ESCCAPE_action 
            actions[75] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_","")
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            index = self.text.find('\n')
            if index != -1: raise UncloseString(self.text[1:index-1])
            else: self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise UncloseString(self.text[1:]) 
     

    def ILLEGAL_ESCCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             raise IllegalEscape(self.text[1:]) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


