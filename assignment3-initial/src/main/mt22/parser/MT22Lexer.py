# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01c8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\3\2\3\2\3\2\3\2\7\2\u008c\n\2\f\2\16\2\u008f\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\7\2\u0097\n\2\f\2\16\2\u009a\13")
        buf.write("\2\5\2\u009c\n\2\3\2\3\2\3\3\3\3\3\3\7\3\u00a3\n\3\f\3")
        buf.write("\16\3\u00a6\13\3\3\3\3\3\6\3\u00aa\n\3\r\3\16\3\u00ab")
        buf.write("\7\3\u00ae\n\3\f\3\16\3\u00b1\13\3\5\3\u00b3\n\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\u00c5\n\4\3\4\3\4\3\5\3\5\7\5\u00cb\n\5\f\5\16")
        buf.write("\5\u00ce\13\5\3\6\3\6\5\6\u00d2\n\6\3\6\6\6\u00d5\n\6")
        buf.write("\r\6\16\6\u00d6\3\7\3\7\5\7\u00db\n\7\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\7\t\u00e4\n\t\f\t\16\t\u00e7\13\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\5")
        buf.write("=\u01b0\n=\3=\3=\3=\7=\u01b5\n=\f=\16=\u01b8\13=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3B\3B\3C\3C\3C\3\u008d\2D\3")
        buf.write("\3\5\4\7\5\t\2\13\2\r\6\17\7\21\b\23\t\25\2\27\2\31\2")
        buf.write("\33\n\35\13\37\f!\r#\16%\17\'\20)\21+\22-\23/\24\61\25")
        buf.write("\63\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"")
        buf.write("M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66")
        buf.write("u\67w8y9{:};\177<\u0081=\u0083>\u0085?\3\2\13\4\2\f\f")
        buf.write("\17\17\4\2GGgg\4\2--//\4\2$$^^\n\2$$))^^ddhhppttvv\3\2")
        buf.write("\62;\3\2\63;\4\2C\\c|\5\2\n\f\16\17\"\"\2\u01d7\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\3\u009b\3\2\2\2\5\u00b2\3\2\2\2\7\u00c4")
        buf.write("\3\2\2\2\t\u00c8\3\2\2\2\13\u00cf\3\2\2\2\r\u00da\3\2")
        buf.write("\2\2\17\u00dc\3\2\2\2\21\u00e0\3\2\2\2\23\u00ea\3\2\2")
        buf.write("\2\25\u00ee\3\2\2\2\27\u00f1\3\2\2\2\31\u00f4\3\2\2\2")
        buf.write("\33\u00f7\3\2\2\2\35\u00ff\3\2\2\2\37\u0107\3\2\2\2!\u010e")
        buf.write("\3\2\2\2#\u0114\3\2\2\2%\u0119\3\2\2\2\'\u011f\3\2\2\2")
        buf.write(")\u0124\3\2\2\2+\u0128\3\2\2\2-\u012e\3\2\2\2/\u0131\3")
        buf.write("\2\2\2\61\u013a\3\2\2\2\63\u013d\3\2\2\2\65\u0142\3\2")
        buf.write("\2\2\67\u0149\3\2\2\29\u014e\3\2\2\2;\u0154\3\2\2\2=\u015d")
        buf.write("\3\2\2\2?\u0161\3\2\2\2A\u0164\3\2\2\2C\u016c\3\2\2\2")
        buf.write("E\u0172\3\2\2\2G\u0174\3\2\2\2I\u0176\3\2\2\2K\u0178\3")
        buf.write("\2\2\2M\u017a\3\2\2\2O\u017c\3\2\2\2Q\u017e\3\2\2\2S\u0181")
        buf.write("\3\2\2\2U\u0184\3\2\2\2W\u0187\3\2\2\2Y\u018a\3\2\2\2")
        buf.write("[\u018c\3\2\2\2]\u018e\3\2\2\2_\u0191\3\2\2\2a\u0193\3")
        buf.write("\2\2\2c\u0196\3\2\2\2e\u0199\3\2\2\2g\u019b\3\2\2\2i\u019d")
        buf.write("\3\2\2\2k\u019f\3\2\2\2m\u01a1\3\2\2\2o\u01a3\3\2\2\2")
        buf.write("q\u01a5\3\2\2\2s\u01a7\3\2\2\2u\u01a9\3\2\2\2w\u01ab\3")
        buf.write("\2\2\2y\u01af\3\2\2\2{\u01b9\3\2\2\2}\u01bb\3\2\2\2\177")
        buf.write("\u01bd\3\2\2\2\u0081\u01bf\3\2\2\2\u0083\u01c1\3\2\2\2")
        buf.write("\u0085\u01c5\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089")
        buf.write("\7,\2\2\u0089\u008d\3\2\2\2\u008a\u008c\13\2\2\2\u008b")
        buf.write("\u008a\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008d\u008b\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d\3")
        buf.write("\2\2\2\u0090\u0091\7,\2\2\u0091\u009c\7\61\2\2\u0092\u0093")
        buf.write("\7\61\2\2\u0093\u0094\7\61\2\2\u0094\u0098\3\2\2\2\u0095")
        buf.write("\u0097\n\2\2\2\u0096\u0095\3\2\2\2\u0097\u009a\3\2\2\2")
        buf.write("\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u009c\3")
        buf.write("\2\2\2\u009a\u0098\3\2\2\2\u009b\u0087\3\2\2\2\u009b\u0092")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\b\2\2\2\u009e")
        buf.write("\4\3\2\2\2\u009f\u00b3\7\62\2\2\u00a0\u00a4\5\177@\2\u00a1")
        buf.write("\u00a3\5}?\2\u00a2\u00a1\3\2\2\2\u00a3\u00a6\3\2\2\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00af\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a7\u00a9\5{>\2\u00a8\u00aa\5}")
        buf.write("?\2\u00a9\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00a7\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b2\u009f\3\2\2\2\u00b2\u00a0\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b5\b\3\3\2\u00b5\6\3\2\2\2\u00b6\u00b7")
        buf.write("\5\5\3\2\u00b7\u00b8\5\t\5\2\u00b8\u00b9\5\13\6\2\u00b9")
        buf.write("\u00c5\3\2\2\2\u00ba\u00bb\5\5\3\2\u00bb\u00bc\5\t\5\2")
        buf.write("\u00bc\u00c5\3\2\2\2\u00bd\u00be\5\t\5\2\u00be\u00bf\5")
        buf.write("\13\6\2\u00bf\u00c5\3\2\2\2\u00c0\u00c1\5\5\3\2\u00c1")
        buf.write("\u00c2\5\13\6\2\u00c2\u00c5\3\2\2\2\u00c3\u00c5\5\t\5")
        buf.write("\2\u00c4\u00b6\3\2\2\2\u00c4\u00ba\3\2\2\2\u00c4\u00bd")
        buf.write("\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\b\4\4\2\u00c7\b\3\2\2\2\u00c8")
        buf.write("\u00cc\7\60\2\2\u00c9\u00cb\5}?\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cd\n\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1")
        buf.write("\t\3\2\2\u00d0\u00d2\t\4\2\2\u00d1\u00d0\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3\u00d5\5}?\2\u00d4")
        buf.write("\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\f\3\2\2\2\u00d8\u00db\5\'\24")
        buf.write("\2\u00d9\u00db\5%\23\2\u00da\u00d8\3\2\2\2\u00da\u00d9")
        buf.write("\3\2\2\2\u00db\16\3\2\2\2\u00dc\u00dd\5\21\t\2\u00dd\u00de")
        buf.write("\7$\2\2\u00de\u00df\b\b\5\2\u00df\20\3\2\2\2\u00e0\u00e5")
        buf.write("\7$\2\2\u00e1\u00e4\5\25\13\2\u00e2\u00e4\n\5\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\3")
        buf.write("\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\b\t\6\2\u00e9\22")
        buf.write("\3\2\2\2\u00ea\u00eb\5\21\t\2\u00eb\u00ec\5\31\r\2\u00ec")
        buf.write("\u00ed\b\n\7\2\u00ed\24\3\2\2\2\u00ee\u00ef\7^\2\2\u00ef")
        buf.write("\u00f0\t\6\2\2\u00f0\26\3\2\2\2\u00f1\u00f2\7^\2\2\u00f2")
        buf.write("\u00f3\7p\2\2\u00f3\30\3\2\2\2\u00f4\u00f5\7^\2\2\u00f5")
        buf.write("\u00f6\n\6\2\2\u00f6\32\3\2\2\2\u00f7\u00f8\7d\2\2\u00f8")
        buf.write("\u00f9\7q\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7n\2\2\u00fb")
        buf.write("\u00fc\7g\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe\7p\2\2\u00fe")
        buf.write("\34\3\2\2\2\u00ff\u0100\7k\2\2\u0100\u0101\7p\2\2\u0101")
        buf.write("\u0102\7v\2\2\u0102\u0103\7g\2\2\u0103\u0104\7i\2\2\u0104")
        buf.write("\u0105\7g\2\2\u0105\u0106\7t\2\2\u0106\36\3\2\2\2\u0107")
        buf.write("\u0108\7u\2\2\u0108\u0109\7v\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7k\2\2\u010b\u010c\7p\2\2\u010c\u010d\7i\2\2\u010d")
        buf.write(" \3\2\2\2\u010e\u010f\7h\2\2\u010f\u0110\7n\2\2\u0110")
        buf.write("\u0111\7q\2\2\u0111\u0112\7c\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\"\3\2\2\2\u0114\u0115\7x\2\2\u0115\u0116\7q\2\2\u0116")
        buf.write("\u0117\7k\2\2\u0117\u0118\7f\2\2\u0118$\3\2\2\2\u0119")
        buf.write("\u011a\7h\2\2\u011a\u011b\7c\2\2\u011b\u011c\7n\2\2\u011c")
        buf.write("\u011d\7u\2\2\u011d\u011e\7g\2\2\u011e&\3\2\2\2\u011f")
        buf.write("\u0120\7v\2\2\u0120\u0121\7t\2\2\u0121\u0122\7w\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123(\3\2\2\2\u0124\u0125\7h\2\2\u0125")
        buf.write("\u0126\7q\2\2\u0126\u0127\7t\2\2\u0127*\3\2\2\2\u0128")
        buf.write("\u0129\7y\2\2\u0129\u012a\7j\2\2\u012a\u012b\7k\2\2\u012b")
        buf.write("\u012c\7n\2\2\u012c\u012d\7g\2\2\u012d,\3\2\2\2\u012e")
        buf.write("\u012f\7f\2\2\u012f\u0130\7q\2\2\u0130.\3\2\2\2\u0131")
        buf.write("\u0132\7h\2\2\u0132\u0133\7w\2\2\u0133\u0134\7p\2\2\u0134")
        buf.write("\u0135\7e\2\2\u0135\u0136\7v\2\2\u0136\u0137\7k\2\2\u0137")
        buf.write("\u0138\7q\2\2\u0138\u0139\7p\2\2\u0139\60\3\2\2\2\u013a")
        buf.write("\u013b\7k\2\2\u013b\u013c\7h\2\2\u013c\62\3\2\2\2\u013d")
        buf.write("\u013e\7g\2\2\u013e\u013f\7n\2\2\u013f\u0140\7u\2\2\u0140")
        buf.write("\u0141\7g\2\2\u0141\64\3\2\2\2\u0142\u0143\7t\2\2\u0143")
        buf.write("\u0144\7g\2\2\u0144\u0145\7v\2\2\u0145\u0146\7w\2\2\u0146")
        buf.write("\u0147\7t\2\2\u0147\u0148\7p\2\2\u0148\66\3\2\2\2\u0149")
        buf.write("\u014a\7c\2\2\u014a\u014b\7w\2\2\u014b\u014c\7v\2\2\u014c")
        buf.write("\u014d\7q\2\2\u014d8\3\2\2\2\u014e\u014f\7d\2\2\u014f")
        buf.write("\u0150\7t\2\2\u0150\u0151\7g\2\2\u0151\u0152\7c\2\2\u0152")
        buf.write("\u0153\7m\2\2\u0153:\3\2\2\2\u0154\u0155\7e\2\2\u0155")
        buf.write("\u0156\7q\2\2\u0156\u0157\7p\2\2\u0157\u0158\7v\2\2\u0158")
        buf.write("\u0159\7k\2\2\u0159\u015a\7p\2\2\u015a\u015b\7w\2\2\u015b")
        buf.write("\u015c\7g\2\2\u015c<\3\2\2\2\u015d\u015e\7q\2\2\u015e")
        buf.write("\u015f\7w\2\2\u015f\u0160\7v\2\2\u0160>\3\2\2\2\u0161")
        buf.write("\u0162\7q\2\2\u0162\u0163\7h\2\2\u0163@\3\2\2\2\u0164")
        buf.write("\u0165\7k\2\2\u0165\u0166\7p\2\2\u0166\u0167\7j\2\2\u0167")
        buf.write("\u0168\7g\2\2\u0168\u0169\7t\2\2\u0169\u016a\7k\2\2\u016a")
        buf.write("\u016b\7v\2\2\u016bB\3\2\2\2\u016c\u016d\7c\2\2\u016d")
        buf.write("\u016e\7t\2\2\u016e\u016f\7t\2\2\u016f\u0170\7c\2\2\u0170")
        buf.write("\u0171\7{\2\2\u0171D\3\2\2\2\u0172\u0173\7-\2\2\u0173")
        buf.write("F\3\2\2\2\u0174\u0175\7/\2\2\u0175H\3\2\2\2\u0176\u0177")
        buf.write("\7,\2\2\u0177J\3\2\2\2\u0178\u0179\7\61\2\2\u0179L\3\2")
        buf.write("\2\2\u017a\u017b\7\'\2\2\u017bN\3\2\2\2\u017c\u017d\7")
        buf.write("#\2\2\u017dP\3\2\2\2\u017e\u017f\7(\2\2\u017f\u0180\7")
        buf.write("(\2\2\u0180R\3\2\2\2\u0181\u0182\7~\2\2\u0182\u0183\7")
        buf.write("~\2\2\u0183T\3\2\2\2\u0184\u0185\7?\2\2\u0185\u0186\7")
        buf.write("?\2\2\u0186V\3\2\2\2\u0187\u0188\7#\2\2\u0188\u0189\7")
        buf.write("?\2\2\u0189X\3\2\2\2\u018a\u018b\7?\2\2\u018bZ\3\2\2\2")
        buf.write("\u018c\u018d\7>\2\2\u018d\\\3\2\2\2\u018e\u018f\7>\2\2")
        buf.write("\u018f\u0190\7?\2\2\u0190^\3\2\2\2\u0191\u0192\7@\2\2")
        buf.write("\u0192`\3\2\2\2\u0193\u0194\7@\2\2\u0194\u0195\7?\2\2")
        buf.write("\u0195b\3\2\2\2\u0196\u0197\7<\2\2\u0197\u0198\7<\2\2")
        buf.write("\u0198d\3\2\2\2\u0199\u019a\7*\2\2\u019af\3\2\2\2\u019b")
        buf.write("\u019c\7+\2\2\u019ch\3\2\2\2\u019d\u019e\7}\2\2\u019e")
        buf.write("j\3\2\2\2\u019f\u01a0\7\177\2\2\u01a0l\3\2\2\2\u01a1\u01a2")
        buf.write("\7]\2\2\u01a2n\3\2\2\2\u01a3\u01a4\7_\2\2\u01a4p\3\2\2")
        buf.write("\2\u01a5\u01a6\7\60\2\2\u01a6r\3\2\2\2\u01a7\u01a8\7.")
        buf.write("\2\2\u01a8t\3\2\2\2\u01a9\u01aa\7=\2\2\u01aav\3\2\2\2")
        buf.write("\u01ab\u01ac\7<\2\2\u01acx\3\2\2\2\u01ad\u01b0\5\u0081")
        buf.write("A\2\u01ae\u01b0\5{>\2\u01af\u01ad\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b6\3\2\2\2\u01b1\u01b5\5\u0081A\2\u01b2")
        buf.write("\u01b5\5{>\2\u01b3\u01b5\5}?\2\u01b4\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7z\3\2\2")
        buf.write("\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7a\2\2\u01ba|\3\2\2")
        buf.write("\2\u01bb\u01bc\t\7\2\2\u01bc~\3\2\2\2\u01bd\u01be\t\b")
        buf.write("\2\2\u01be\u0080\3\2\2\2\u01bf\u01c0\t\t\2\2\u01c0\u0082")
        buf.write("\3\2\2\2\u01c1\u01c2\t\n\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c4\bB\2\2\u01c4\u0084\3\2\2\2\u01c5\u01c6\13\2\2\2")
        buf.write("\u01c6\u01c7\bC\b\2\u01c7\u0086\3\2\2\2\24\2\u008d\u0098")
        buf.write("\u009b\u00a4\u00ab\u00af\u00b2\u00c4\u00cc\u00d1\u00d6")
        buf.write("\u00da\u00e3\u00e5\u01af\u01b4\u01b6\t\b\2\2\3\3\2\3\4")
        buf.write("\3\3\b\4\3\t\5\3\n\6\3C\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT = 1
    INTLIT = 2
    FLOATLIT = 3
    BOOLLIT = 4
    STRINGLIT = 5
    UNCLOSE_STRING = 6
    ILLEGAL_ESCCAPE = 7
    BOOLEAN = 8
    INTEGER = 9
    STRING = 10
    FLOAT = 11
    VOID = 12
    FALSE = 13
    TRUE = 14
    FOR = 15
    WHILE = 16
    DO = 17
    FUNCTION = 18
    IF = 19
    ELSE = 20
    RETURN = 21
    AUTO = 22
    BREAK = 23
    CONTINUE = 24
    OUT = 25
    OF = 26
    INHERIT = 27
    ARRAY = 28
    ADD = 29
    SUB = 30
    MUL = 31
    DIV = 32
    MOD = 33
    NOT = 34
    AND = 35
    OR = 36
    EQUAL = 37
    NOT_EQUAL = 38
    ASSIGN = 39
    LT = 40
    LE = 41
    GT = 42
    GE = 43
    CONCAT = 44
    Lb = 45
    Rb = 46
    LB = 47
    RB = 48
    LQB = 49
    RQB = 50
    DOT = 51
    COMMA = 52
    SEMI = 53
    COLON = 54
    IDENTIFIERS = 55
    UNDERSCORE = 56
    DIGIT = 57
    NONZERO_DIGIT = 58
    CHAR = 59
    WS = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'integer'", "'string'", "'float'", "'void'", "'false'", 
            "'true'", "'for'", "'while'", "'do'", "'function'", "'if'", 
            "'else'", "'return'", "'auto'", "'break'", "'continue'", "'out'", 
            "'of'", "'inherit'", "'array'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'='", "'<'", 
            "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'{'", "'}'", "'['", 
            "']'", "'.'", "','", "';'", "':'", "'_'" ]

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

    ruleNames = [ "COMMENT", "INTLIT", "FLOATLIT", "DEC", "EXP", "BOOLLIT", 
                  "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCCAPE", "ECS", 
                  "NEWLINE", "ILLEGAL_ESC", "BOOLEAN", "INTEGER", "STRING", 
                  "FLOAT", "VOID", "FALSE", "TRUE", "FOR", "WHILE", "DO", 
                  "FUNCTION", "IF", "ELSE", "RETURN", "AUTO", "BREAK", "CONTINUE", 
                  "OUT", "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "ASSIGN", "LT", "LE", "GT", "GE", "CONCAT", "Lb", "Rb", 
                  "LB", "RB", "LQB", "RQB", "DOT", "COMMA", "SEMI", "COLON", 
                  "IDENTIFIERS", "UNDERSCORE", "DIGIT", "NONZERO_DIGIT", 
                  "CHAR", "WS", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INTLIT_action 
            actions[2] = self.FLOATLIT_action 
            actions[6] = self.STRINGLIT_action 
            actions[7] = self.UNCLOSE_STRING_action 
            actions[8] = self.ILLEGAL_ESCCAPE_action 
            actions[65] = self.ERROR_CHAR_action 
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
     


