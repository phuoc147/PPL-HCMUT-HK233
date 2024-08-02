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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2I")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\7\f\u0113\n\f\f\f\16\f\u0116\13\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u011e\n\f\f\f\16\f\u0121\13\f\5\f")
        buf.write("\u0123\n\f\3\f\3\f\3\r\3\r\3\r\7\r\u012a\n\r\f\r\16\r")
        buf.write("\u012d\13\r\3\r\3\r\6\r\u0131\n\r\r\r\16\r\u0132\7\r\u0135")
        buf.write("\n\r\f\r\16\r\u0138\13\r\5\r\u013a\n\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u014c\n\16\3\16\3\16\3\17\3\17\7\17\u0152")
        buf.write("\n\17\f\17\16\17\u0155\13\17\3\20\3\20\5\20\u0159\n\20")
        buf.write("\3\20\6\20\u015c\n\20\r\20\16\20\u015d\3\21\3\21\5\21")
        buf.write("\u0162\n\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u016b")
        buf.write("\n\23\f\23\16\23\u016e\13\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*")
        buf.write("\3*\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3")
        buf.write("?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\5")
        buf.write("G\u0237\nG\3G\3G\3G\7G\u023c\nG\fG\16G\u023f\13G\3H\3")
        buf.write("H\3I\3I\3J\3J\3K\3K\3L\3L\3L\3L\3M\3M\3M\3\u0114\2N\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\2\37\2!\20#\21%\22\'\23)\2+\2-\2/\24\61\25\63")
        buf.write("\26\65\27\67\309\31;\32=\33?\34A\35C\36E\37G I!K\"M#O")
        buf.write("$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63o\64q\65s\66u")
        buf.write("\67w8y9{:};\177<\u0081=\u0083>\u0085?\u0087@\u0089A\u008b")
        buf.write("B\u008dC\u008fD\u0091E\u0093F\u0095G\u0097H\u0099I\3\2")
        buf.write("\13\4\2\f\f\17\17\4\2GGgg\4\2--//\4\2$$^^\n\2$$))^^dd")
        buf.write("hhppttvv\3\2\62;\3\2\63;\4\2C\\c|\5\2\n\f\16\17\"\"\2")
        buf.write("\u025e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u00a7\3\2\2\2\7\u00b4")
        buf.write("\3\2\2\2\t\u00be\3\2\2\2\13\u00c9\3\2\2\2\r\u00d5\3\2")
        buf.write("\2\2\17\u00e2\3\2\2\2\21\u00ed\3\2\2\2\23\u00f9\3\2\2")
        buf.write("\2\25\u00ff\3\2\2\2\27\u0122\3\2\2\2\31\u0139\3\2\2\2")
        buf.write("\33\u014b\3\2\2\2\35\u014f\3\2\2\2\37\u0156\3\2\2\2!\u0161")
        buf.write("\3\2\2\2#\u0163\3\2\2\2%\u0167\3\2\2\2\'\u0171\3\2\2\2")
        buf.write(")\u0175\3\2\2\2+\u0178\3\2\2\2-\u017b\3\2\2\2/\u017e\3")
        buf.write("\2\2\2\61\u0186\3\2\2\2\63\u018e\3\2\2\2\65\u0195\3\2")
        buf.write("\2\2\67\u019b\3\2\2\29\u01a0\3\2\2\2;\u01a6\3\2\2\2=\u01ab")
        buf.write("\3\2\2\2?\u01af\3\2\2\2A\u01b5\3\2\2\2C\u01b8\3\2\2\2")
        buf.write("E\u01c1\3\2\2\2G\u01c4\3\2\2\2I\u01c9\3\2\2\2K\u01d0\3")
        buf.write("\2\2\2M\u01d5\3\2\2\2O\u01db\3\2\2\2Q\u01e4\3\2\2\2S\u01e8")
        buf.write("\3\2\2\2U\u01eb\3\2\2\2W\u01f3\3\2\2\2Y\u01f9\3\2\2\2")
        buf.write("[\u01fb\3\2\2\2]\u01fd\3\2\2\2_\u01ff\3\2\2\2a\u0201\3")
        buf.write("\2\2\2c\u0203\3\2\2\2e\u0205\3\2\2\2g\u0208\3\2\2\2i\u020b")
        buf.write("\3\2\2\2k\u020e\3\2\2\2m\u0211\3\2\2\2o\u0213\3\2\2\2")
        buf.write("q\u0215\3\2\2\2s\u0218\3\2\2\2u\u021a\3\2\2\2w\u021d\3")
        buf.write("\2\2\2y\u0220\3\2\2\2{\u0222\3\2\2\2}\u0224\3\2\2\2\177")
        buf.write("\u0226\3\2\2\2\u0081\u0228\3\2\2\2\u0083\u022a\3\2\2\2")
        buf.write("\u0085\u022c\3\2\2\2\u0087\u022e\3\2\2\2\u0089\u0230\3")
        buf.write("\2\2\2\u008b\u0232\3\2\2\2\u008d\u0236\3\2\2\2\u008f\u0240")
        buf.write("\3\2\2\2\u0091\u0242\3\2\2\2\u0093\u0244\3\2\2\2\u0095")
        buf.write("\u0246\3\2\2\2\u0097\u0248\3\2\2\2\u0099\u024c\3\2\2\2")
        buf.write("\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e\7c")
        buf.write("\2\2\u009e\u009f\7f\2\2\u009f\u00a0\7K\2\2\u00a0\u00a1")
        buf.write("\7p\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7i\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7t\2\2\u00a6\4")
        buf.write("\3\2\2\2\u00a7\u00a8\7r\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7v\2\2\u00ac\u00ad")
        buf.write("\7K\2\2\u00ad\u00ae\7p\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7g\2\2\u00b0\u00b1\7i\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7t\2\2\u00b3\6\3\2\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8\7f\2\2\u00b8\u00b9")
        buf.write("\7H\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7v\2\2\u00bd\b\3\2\2\2\u00be\u00bf")
        buf.write("\7r\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7v\2\2\u00c3\u00c4\7H\2\2\u00c4\u00c5")
        buf.write("\7n\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\n\3\2\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce")
        buf.write("\7D\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7n\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4")
        buf.write("\7p\2\2\u00d4\f\3\2\2\2\u00d5\u00d6\7r\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7v\2\2\u00da\u00db\7D\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7p\2\2\u00e1\16\3\2\2\2\u00e2\u00e3")
        buf.write("\7t\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7f\2\2\u00e6\u00e7\7U\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9")
        buf.write("\7t\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec")
        buf.write("\7i\2\2\u00ec\20\3\2\2\2\u00ed\u00ee\7r\2\2\u00ee\u00ef")
        buf.write("\7t\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2")
        buf.write("\7v\2\2\u00f2\u00f3\7U\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7t\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7i\2\2\u00f8\22\3\2\2\2\u00f9\u00fa\7u\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7r\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe\24\3\2\2\2\u00ff\u0100\7r\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7g\2\2\u0102\u0103\7x\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\u0105\7p\2\2\u0105\u0106\7v\2\2\u0106\u0107")
        buf.write("\7F\2\2\u0107\u0108\7g\2\2\u0108\u0109\7h\2\2\u0109\u010a")
        buf.write("\7c\2\2\u010a\u010b\7w\2\2\u010b\u010c\7n\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d\26\3\2\2\2\u010e\u010f\7\61\2\2\u010f\u0110")
        buf.write("\7,\2\2\u0110\u0114\3\2\2\2\u0111\u0113\13\2\2\2\u0112")
        buf.write("\u0111\3\2\2\2\u0113\u0116\3\2\2\2\u0114\u0115\3\2\2\2")
        buf.write("\u0114\u0112\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0114\3")
        buf.write("\2\2\2\u0117\u0118\7,\2\2\u0118\u0123\7\61\2\2\u0119\u011a")
        buf.write("\7\61\2\2\u011a\u011b\7\61\2\2\u011b\u011f\3\2\2\2\u011c")
        buf.write("\u011e\n\2\2\2\u011d\u011c\3\2\2\2\u011e\u0121\3\2\2\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0123\3")
        buf.write("\2\2\2\u0121\u011f\3\2\2\2\u0122\u010e\3\2\2\2\u0122\u0119")
        buf.write("\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\b\f\2\2\u0125")
        buf.write("\30\3\2\2\2\u0126\u013a\7\62\2\2\u0127\u012b\5\u0093J")
        buf.write("\2\u0128\u012a\5\u0091I\2\u0129\u0128\3\2\2\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u0136\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u0130\5\u008f")
        buf.write("H\2\u012f\u0131\5\u0091I\2\u0130\u012f\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u0135\3\2\2\2\u0134\u012e\3\2\2\2\u0135\u0138\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u013a\3")
        buf.write("\2\2\2\u0138\u0136\3\2\2\2\u0139\u0126\3\2\2\2\u0139\u0127")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\b\r\3\2\u013c")
        buf.write("\32\3\2\2\2\u013d\u013e\5\31\r\2\u013e\u013f\5\35\17\2")
        buf.write("\u013f\u0140\5\37\20\2\u0140\u014c\3\2\2\2\u0141\u0142")
        buf.write("\5\31\r\2\u0142\u0143\5\35\17\2\u0143\u014c\3\2\2\2\u0144")
        buf.write("\u0145\5\35\17\2\u0145\u0146\5\37\20\2\u0146\u014c\3\2")
        buf.write("\2\2\u0147\u0148\5\31\r\2\u0148\u0149\5\37\20\2\u0149")
        buf.write("\u014c\3\2\2\2\u014a\u014c\5\35\17\2\u014b\u013d\3\2\2")
        buf.write("\2\u014b\u0141\3\2\2\2\u014b\u0144\3\2\2\2\u014b\u0147")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d")
        buf.write("\u014e\b\16\4\2\u014e\34\3\2\2\2\u014f\u0153\7\60\2\2")
        buf.write("\u0150\u0152\5\u0091I\2\u0151\u0150\3\2\2\2\u0152\u0155")
        buf.write("\3\2\2\2\u0153\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\36\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0158\t\3\2\2\u0157")
        buf.write("\u0159\t\4\2\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015b\3\2\2\2\u015a\u015c\5\u0091I\2\u015b\u015a")
        buf.write("\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e \3\2\2\2\u015f\u0162\5;\36\2\u0160")
        buf.write("\u0162\59\35\2\u0161\u015f\3\2\2\2\u0161\u0160\3\2\2\2")
        buf.write("\u0162\"\3\2\2\2\u0163\u0164\5%\23\2\u0164\u0165\7$\2")
        buf.write("\2\u0165\u0166\b\22\5\2\u0166$\3\2\2\2\u0167\u016c\7$")
        buf.write("\2\2\u0168\u016b\5)\25\2\u0169\u016b\n\5\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016f\u0170\b\23\6\2\u0170&\3\2\2")
        buf.write("\2\u0171\u0172\5%\23\2\u0172\u0173\5-\27\2\u0173\u0174")
        buf.write("\b\24\7\2\u0174(\3\2\2\2\u0175\u0176\7^\2\2\u0176\u0177")
        buf.write("\t\6\2\2\u0177*\3\2\2\2\u0178\u0179\7^\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017a,\3\2\2\2\u017b\u017c\7^\2\2\u017c\u017d")
        buf.write("\n\6\2\2\u017d.\3\2\2\2\u017e\u017f\7d\2\2\u017f\u0180")
        buf.write("\7q\2\2\u0180\u0181\7q\2\2\u0181\u0182\7n\2\2\u0182\u0183")
        buf.write("\7g\2\2\u0183\u0184\7c\2\2\u0184\u0185\7p\2\2\u0185\60")
        buf.write("\3\2\2\2\u0186\u0187\7k\2\2\u0187\u0188\7p\2\2\u0188\u0189")
        buf.write("\7v\2\2\u0189\u018a\7g\2\2\u018a\u018b\7i\2\2\u018b\u018c")
        buf.write("\7g\2\2\u018c\u018d\7t\2\2\u018d\62\3\2\2\2\u018e\u018f")
        buf.write("\7u\2\2\u018f\u0190\7v\2\2\u0190\u0191\7t\2\2\u0191\u0192")
        buf.write("\7k\2\2\u0192\u0193\7p\2\2\u0193\u0194\7i\2\2\u0194\64")
        buf.write("\3\2\2\2\u0195\u0196\7h\2\2\u0196\u0197\7n\2\2\u0197\u0198")
        buf.write("\7q\2\2\u0198\u0199\7c\2\2\u0199\u019a\7v\2\2\u019a\66")
        buf.write("\3\2\2\2\u019b\u019c\7x\2\2\u019c\u019d\7q\2\2\u019d\u019e")
        buf.write("\7k\2\2\u019e\u019f\7f\2\2\u019f8\3\2\2\2\u01a0\u01a1")
        buf.write("\7h\2\2\u01a1\u01a2\7c\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4")
        buf.write("\7u\2\2\u01a4\u01a5\7g\2\2\u01a5:\3\2\2\2\u01a6\u01a7")
        buf.write("\7v\2\2\u01a7\u01a8\7t\2\2\u01a8\u01a9\7w\2\2\u01a9\u01aa")
        buf.write("\7g\2\2\u01aa<\3\2\2\2\u01ab\u01ac\7h\2\2\u01ac\u01ad")
        buf.write("\7q\2\2\u01ad\u01ae\7t\2\2\u01ae>\3\2\2\2\u01af\u01b0")
        buf.write("\7y\2\2\u01b0\u01b1\7j\2\2\u01b1\u01b2\7k\2\2\u01b2\u01b3")
        buf.write("\7n\2\2\u01b3\u01b4\7g\2\2\u01b4@\3\2\2\2\u01b5\u01b6")
        buf.write("\7f\2\2\u01b6\u01b7\7q\2\2\u01b7B\3\2\2\2\u01b8\u01b9")
        buf.write("\7h\2\2\u01b9\u01ba\7w\2\2\u01ba\u01bb\7p\2\2\u01bb\u01bc")
        buf.write("\7e\2\2\u01bc\u01bd\7v\2\2\u01bd\u01be\7k\2\2\u01be\u01bf")
        buf.write("\7q\2\2\u01bf\u01c0\7p\2\2\u01c0D\3\2\2\2\u01c1\u01c2")
        buf.write("\7k\2\2\u01c2\u01c3\7h\2\2\u01c3F\3\2\2\2\u01c4\u01c5")
        buf.write("\7g\2\2\u01c5\u01c6\7n\2\2\u01c6\u01c7\7u\2\2\u01c7\u01c8")
        buf.write("\7g\2\2\u01c8H\3\2\2\2\u01c9\u01ca\7t\2\2\u01ca\u01cb")
        buf.write("\7g\2\2\u01cb\u01cc\7v\2\2\u01cc\u01cd\7w\2\2\u01cd\u01ce")
        buf.write("\7t\2\2\u01ce\u01cf\7p\2\2\u01cfJ\3\2\2\2\u01d0\u01d1")
        buf.write("\7c\2\2\u01d1\u01d2\7w\2\2\u01d2\u01d3\7v\2\2\u01d3\u01d4")
        buf.write("\7q\2\2\u01d4L\3\2\2\2\u01d5\u01d6\7d\2\2\u01d6\u01d7")
        buf.write("\7t\2\2\u01d7\u01d8\7g\2\2\u01d8\u01d9\7c\2\2\u01d9\u01da")
        buf.write("\7m\2\2\u01daN\3\2\2\2\u01db\u01dc\7e\2\2\u01dc\u01dd")
        buf.write("\7q\2\2\u01dd\u01de\7p\2\2\u01de\u01df\7v\2\2\u01df\u01e0")
        buf.write("\7k\2\2\u01e0\u01e1\7p\2\2\u01e1\u01e2\7w\2\2\u01e2\u01e3")
        buf.write("\7g\2\2\u01e3P\3\2\2\2\u01e4\u01e5\7q\2\2\u01e5\u01e6")
        buf.write("\7w\2\2\u01e6\u01e7\7v\2\2\u01e7R\3\2\2\2\u01e8\u01e9")
        buf.write("\7q\2\2\u01e9\u01ea\7h\2\2\u01eaT\3\2\2\2\u01eb\u01ec")
        buf.write("\7k\2\2\u01ec\u01ed\7p\2\2\u01ed\u01ee\7j\2\2\u01ee\u01ef")
        buf.write("\7g\2\2\u01ef\u01f0\7t\2\2\u01f0\u01f1\7k\2\2\u01f1\u01f2")
        buf.write("\7v\2\2\u01f2V\3\2\2\2\u01f3\u01f4\7c\2\2\u01f4\u01f5")
        buf.write("\7t\2\2\u01f5\u01f6\7t\2\2\u01f6\u01f7\7c\2\2\u01f7\u01f8")
        buf.write("\7{\2\2\u01f8X\3\2\2\2\u01f9\u01fa\7-\2\2\u01faZ\3\2\2")
        buf.write("\2\u01fb\u01fc\7/\2\2\u01fc\\\3\2\2\2\u01fd\u01fe\7,\2")
        buf.write("\2\u01fe^\3\2\2\2\u01ff\u0200\7\61\2\2\u0200`\3\2\2\2")
        buf.write("\u0201\u0202\7\'\2\2\u0202b\3\2\2\2\u0203\u0204\7#\2\2")
        buf.write("\u0204d\3\2\2\2\u0205\u0206\7(\2\2\u0206\u0207\7(\2\2")
        buf.write("\u0207f\3\2\2\2\u0208\u0209\7~\2\2\u0209\u020a\7~\2\2")
        buf.write("\u020ah\3\2\2\2\u020b\u020c\7?\2\2\u020c\u020d\7?\2\2")
        buf.write("\u020dj\3\2\2\2\u020e\u020f\7#\2\2\u020f\u0210\7?\2\2")
        buf.write("\u0210l\3\2\2\2\u0211\u0212\7?\2\2\u0212n\3\2\2\2\u0213")
        buf.write("\u0214\7>\2\2\u0214p\3\2\2\2\u0215\u0216\7>\2\2\u0216")
        buf.write("\u0217\7?\2\2\u0217r\3\2\2\2\u0218\u0219\7@\2\2\u0219")
        buf.write("t\3\2\2\2\u021a\u021b\7@\2\2\u021b\u021c\7?\2\2\u021c")
        buf.write("v\3\2\2\2\u021d\u021e\7<\2\2\u021e\u021f\7<\2\2\u021f")
        buf.write("x\3\2\2\2\u0220\u0221\7*\2\2\u0221z\3\2\2\2\u0222\u0223")
        buf.write("\7+\2\2\u0223|\3\2\2\2\u0224\u0225\7}\2\2\u0225~\3\2\2")
        buf.write("\2\u0226\u0227\7\177\2\2\u0227\u0080\3\2\2\2\u0228\u0229")
        buf.write("\7]\2\2\u0229\u0082\3\2\2\2\u022a\u022b\7_\2\2\u022b\u0084")
        buf.write("\3\2\2\2\u022c\u022d\7\60\2\2\u022d\u0086\3\2\2\2\u022e")
        buf.write("\u022f\7.\2\2\u022f\u0088\3\2\2\2\u0230\u0231\7=\2\2\u0231")
        buf.write("\u008a\3\2\2\2\u0232\u0233\7<\2\2\u0233\u008c\3\2\2\2")
        buf.write("\u0234\u0237\5\u0095K\2\u0235\u0237\5\u008fH\2\u0236\u0234")
        buf.write("\3\2\2\2\u0236\u0235\3\2\2\2\u0237\u023d\3\2\2\2\u0238")
        buf.write("\u023c\5\u0095K\2\u0239\u023c\5\u008fH\2\u023a\u023c\5")
        buf.write("\u0091I\2\u023b\u0238\3\2\2\2\u023b\u0239\3\2\2\2\u023b")
        buf.write("\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b\3\2\2\2")
        buf.write("\u023d\u023e\3\2\2\2\u023e\u008e\3\2\2\2\u023f\u023d\3")
        buf.write("\2\2\2\u0240\u0241\7a\2\2\u0241\u0090\3\2\2\2\u0242\u0243")
        buf.write("\t\7\2\2\u0243\u0092\3\2\2\2\u0244\u0245\t\b\2\2\u0245")
        buf.write("\u0094\3\2\2\2\u0246\u0247\t\t\2\2\u0247\u0096\3\2\2\2")
        buf.write("\u0248\u0249\t\n\2\2\u0249\u024a\3\2\2\2\u024a\u024b\b")
        buf.write("L\2\2\u024b\u0098\3\2\2\2\u024c\u024d\13\2\2\2\u024d\u024e")
        buf.write("\bM\b\2\u024e\u009a\3\2\2\2\24\2\u0114\u011f\u0122\u012b")
        buf.write("\u0132\u0136\u0139\u014b\u0153\u0158\u015d\u0161\u016a")
        buf.write("\u016c\u0236\u023b\u023d\t\b\2\2\3\r\2\3\16\3\3\22\4\3")
        buf.write("\23\5\3\24\6\3M\7")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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
     


