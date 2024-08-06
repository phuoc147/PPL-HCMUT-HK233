# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u017c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\3\3\3\5\3Z\n")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3`\n\3\5\3b\n\3\3\4\3\4\5\4f\n\4")
        buf.write("\3\4\3\4\3\4\5\4k\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5w\n\5\3\6\3\6\5\6{\n\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u008e\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\5")
        buf.write("\16\u00b3\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00c0\n\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\5\21\u00c7\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00ce")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00d6\n\23\f")
        buf.write("\23\16\23\u00d9\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u00e1\n\24\f\24\16\24\u00e4\13\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\7\25\u00ec\n\25\f\25\16\25\u00ef\13\25\3")
        buf.write("\26\3\26\3\26\5\26\u00f4\n\26\3\27\3\27\3\27\5\27\u00f9")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0104\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\5")
        buf.write("\32\u010e\n\32\3\32\3\32\3\33\3\33\5\33\u0114\n\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0129\n\35\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u012f\n\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0138\n\37\3\37\3\37\3\37\5\37\u013d")
        buf.write("\n\37\3\37\3\37\3 \3 \3 \3 \3 \5 \u0146\n \3!\5!\u0149")
        buf.write("\n!\3!\5!\u014c\n!\3!\3!\3!\3!\3\"\3\"\3\"\5\"\u0155\n")
        buf.write("\"\3#\3#\3#\5#\u015a\n#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%")
        buf.write("\3%\5%\u0167\n%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3)\3)")
        buf.write("\3)\3*\3*\3*\3*\5*\u017a\n*\3*\2\5$&(+\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPR\2\7\4\2\'(*-\3\2%&\3\2\37 \3\2!#\3\2\n\r\2\u0184")
        buf.write("\2T\3\2\2\2\4a\3\2\2\2\6j\3\2\2\2\bv\3\2\2\2\nz\3\2\2")
        buf.write("\2\f\u0080\3\2\2\2\16\u0089\3\2\2\2\20\u0098\3\2\2\2\22")
        buf.write("\u009e\3\2\2\2\24\u00a6\3\2\2\2\26\u00a9\3\2\2\2\30\u00ac")
        buf.write("\3\2\2\2\32\u00af\3\2\2\2\34\u00b6\3\2\2\2\36\u00bf\3")
        buf.write("\2\2\2 \u00c6\3\2\2\2\"\u00cd\3\2\2\2$\u00cf\3\2\2\2&")
        buf.write("\u00da\3\2\2\2(\u00e5\3\2\2\2*\u00f3\3\2\2\2,\u00f8\3")
        buf.write("\2\2\2.\u0103\3\2\2\2\60\u0105\3\2\2\2\62\u0109\3\2\2")
        buf.write("\2\64\u0113\3\2\2\2\66\u0117\3\2\2\28\u0128\3\2\2\2:\u012e")
        buf.write("\3\2\2\2<\u0130\3\2\2\2>\u0145\3\2\2\2@\u0148\3\2\2\2")
        buf.write("B\u0154\3\2\2\2D\u0156\3\2\2\2F\u015d\3\2\2\2H\u0166\3")
        buf.write("\2\2\2J\u0168\3\2\2\2L\u016a\3\2\2\2N\u016c\3\2\2\2P\u016e")
        buf.write("\3\2\2\2R\u0179\3\2\2\2TU\5\4\3\2UV\7\2\2\3V\3\3\2\2\2")
        buf.write("WZ\5\64\33\2XZ\5<\37\2YW\3\2\2\2YX\3\2\2\2Z[\3\2\2\2[")
        buf.write("\\\5\4\3\2\\b\3\2\2\2]`\5\64\33\2^`\5<\37\2_]\3\2\2\2")
        buf.write("_^\3\2\2\2`b\3\2\2\2aY\3\2\2\2a_\3\2\2\2b\5\3\2\2\2cf")
        buf.write("\5\b\5\2df\5\64\33\2ec\3\2\2\2ed\3\2\2\2fg\3\2\2\2gh\5")
        buf.write("\6\4\2hk\3\2\2\2ik\3\2\2\2je\3\2\2\2ji\3\2\2\2k\7\3\2")
        buf.write("\2\2lw\5\n\6\2mw\5\f\7\2nw\5\16\b\2ow\5\20\t\2pw\5\22")
        buf.write("\n\2qw\5\24\13\2rw\5\26\f\2sw\5\30\r\2tw\5\32\16\2uw\5")
        buf.write("\34\17\2vl\3\2\2\2vm\3\2\2\2vn\3\2\2\2vo\3\2\2\2vp\3\2")
        buf.write("\2\2vq\3\2\2\2vr\3\2\2\2vs\3\2\2\2vt\3\2\2\2vu\3\2\2\2")
        buf.write("w\t\3\2\2\2x{\79\2\2y{\5F$\2zx\3\2\2\2zy\3\2\2\2{|\3\2")
        buf.write("\2\2|}\7)\2\2}~\5 \21\2~\177\7\67\2\2\177\13\3\2\2\2\u0080")
        buf.write("\u0081\7\25\2\2\u0081\u0082\7/\2\2\u0082\u0083\5 \21\2")
        buf.write("\u0083\u0084\7\60\2\2\u0084\u0087\5\b\5\2\u0085\u0086")
        buf.write("\7\26\2\2\u0086\u0088\5\b\5\2\u0087\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\r\3\2\2\2\u0089\u008a\7\21\2\2\u008a")
        buf.write("\u008d\7/\2\2\u008b\u008e\79\2\2\u008c\u008e\5F$\2\u008d")
        buf.write("\u008b\3\2\2\2\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\7)\2\2\u0090\u0091\5 \21\2\u0091\u0092\7")
        buf.write("\66\2\2\u0092\u0093\5 \21\2\u0093\u0094\7\66\2\2\u0094")
        buf.write("\u0095\5 \21\2\u0095\u0096\7\60\2\2\u0096\u0097\5\b\5")
        buf.write("\2\u0097\17\3\2\2\2\u0098\u0099\7\22\2\2\u0099\u009a\7")
        buf.write("/\2\2\u009a\u009b\5 \21\2\u009b\u009c\7\60\2\2\u009c\u009d")
        buf.write("\5\b\5\2\u009d\21\3\2\2\2\u009e\u009f\7\23\2\2\u009f\u00a0")
        buf.write("\5\34\17\2\u00a0\u00a1\7\22\2\2\u00a1\u00a2\7/\2\2\u00a2")
        buf.write("\u00a3\5 \21\2\u00a3\u00a4\7\60\2\2\u00a4\u00a5\7\67\2")
        buf.write("\2\u00a5\23\3\2\2\2\u00a6\u00a7\7\31\2\2\u00a7\u00a8\7")
        buf.write("\67\2\2\u00a8\25\3\2\2\2\u00a9\u00aa\7\32\2\2\u00aa\u00ab")
        buf.write("\7\67\2\2\u00ab\27\3\2\2\2\u00ac\u00ad\5\62\32\2\u00ad")
        buf.write("\u00ae\7\67\2\2\u00ae\31\3\2\2\2\u00af\u00b2\7\27\2\2")
        buf.write("\u00b0\u00b3\5 \21\2\u00b1\u00b3\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write("\7\67\2\2\u00b5\33\3\2\2\2\u00b6\u00b7\7\61\2\2\u00b7")
        buf.write("\u00b8\5\6\4\2\u00b8\u00b9\7\62\2\2\u00b9\35\3\2\2\2\u00ba")
        buf.write("\u00bb\5 \21\2\u00bb\u00bc\7\66\2\2\u00bc\u00bd\5\36\20")
        buf.write("\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\5 \21\2\u00bf\u00ba")
        buf.write("\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\37\3\2\2\2\u00c1\u00c2")
        buf.write("\5\"\22\2\u00c2\u00c3\7.\2\2\u00c3\u00c4\5\"\22\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\5\"\22\2\u00c6\u00c1\3\2\2")
        buf.write("\2\u00c6\u00c5\3\2\2\2\u00c7!\3\2\2\2\u00c8\u00c9\5$\23")
        buf.write("\2\u00c9\u00ca\t\2\2\2\u00ca\u00cb\5$\23\2\u00cb\u00ce")
        buf.write("\3\2\2\2\u00cc\u00ce\5$\23\2\u00cd\u00c8\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce#\3\2\2\2\u00cf\u00d0\b\23\1\2\u00d0")
        buf.write("\u00d1\5&\24\2\u00d1\u00d7\3\2\2\2\u00d2\u00d3\f\4\2\2")
        buf.write("\u00d3\u00d4\t\3\2\2\u00d4\u00d6\5&\24\2\u00d5\u00d2\3")
        buf.write("\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8%\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db")
        buf.write("\b\24\1\2\u00db\u00dc\5(\25\2\u00dc\u00e2\3\2\2\2\u00dd")
        buf.write("\u00de\f\4\2\2\u00de\u00df\t\4\2\2\u00df\u00e1\5(\25\2")
        buf.write("\u00e0\u00dd\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2\u00e0\3")
        buf.write("\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\'\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e5\u00e6\b\25\1\2\u00e6\u00e7\5*\26\2\u00e7")
        buf.write("\u00ed\3\2\2\2\u00e8\u00e9\f\4\2\2\u00e9\u00ea\t\5\2\2")
        buf.write("\u00ea\u00ec\5*\26\2\u00eb\u00e8\3\2\2\2\u00ec\u00ef\3")
        buf.write("\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee)")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\7$\2\2\u00f1")
        buf.write("\u00f4\5*\26\2\u00f2\u00f4\5,\27\2\u00f3\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f2\3\2\2\2\u00f4+\3\2\2\2\u00f5\u00f6\7 \2\2")
        buf.write("\u00f6\u00f9\5,\27\2\u00f7\u00f9\5.\30\2\u00f8\u00f5\3")
        buf.write("\2\2\2\u00f8\u00f7\3\2\2\2\u00f9-\3\2\2\2\u00fa\u0104")
        buf.write("\5\60\31\2\u00fb\u0104\5\62\32\2\u00fc\u0104\7\4\2\2\u00fd")
        buf.write("\u0104\7\5\2\2\u00fe\u0104\7\6\2\2\u00ff\u0104\7\7\2\2")
        buf.write("\u0100\u0104\79\2\2\u0101\u0104\5F$\2\u0102\u0104\5D#")
        buf.write("\2\u0103\u00fa\3\2\2\2\u0103\u00fb\3\2\2\2\u0103\u00fc")
        buf.write("\3\2\2\2\u0103\u00fd\3\2\2\2\u0103\u00fe\3\2\2\2\u0103")
        buf.write("\u00ff\3\2\2\2\u0103\u0100\3\2\2\2\u0103\u0101\3\2\2\2")
        buf.write("\u0103\u0102\3\2\2\2\u0104/\3\2\2\2\u0105\u0106\7/\2\2")
        buf.write("\u0106\u0107\5 \21\2\u0107\u0108\7\60\2\2\u0108\61\3\2")
        buf.write("\2\2\u0109\u010a\79\2\2\u010a\u010d\7/\2\2\u010b\u010e")
        buf.write("\5\36\20\2\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110\7\60\2")
        buf.write("\2\u0110\63\3\2\2\2\u0111\u0114\5\66\34\2\u0112\u0114")
        buf.write("\58\35\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("\u0115\3\2\2\2\u0115\u0116\7\67\2\2\u0116\65\3\2\2\2\u0117")
        buf.write("\u0118\5:\36\2\u0118\u0119\78\2\2\u0119\u011a\5B\"\2\u011a")
        buf.write("\67\3\2\2\2\u011b\u011c\79\2\2\u011c\u011d\7\66\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u011f\58\35\2\u011f\u0120\7\66\2")
        buf.write("\2\u0120\u0121\5 \21\2\u0121\u0129\3\2\2\2\u0122\u0123")
        buf.write("\79\2\2\u0123\u0124\78\2\2\u0124\u0125\5B\"\2\u0125\u0126")
        buf.write("\7)\2\2\u0126\u0127\5 \21\2\u0127\u0129\3\2\2\2\u0128")
        buf.write("\u011b\3\2\2\2\u0128\u0122\3\2\2\2\u01299\3\2\2\2\u012a")
        buf.write("\u012b\79\2\2\u012b\u012c\7\66\2\2\u012c\u012f\5:\36\2")
        buf.write("\u012d\u012f\79\2\2\u012e\u012a\3\2\2\2\u012e\u012d\3")
        buf.write("\2\2\2\u012f;\3\2\2\2\u0130\u0131\79\2\2\u0131\u0132\7")
        buf.write("8\2\2\u0132\u0133\7\24\2\2\u0133\u0134\5H%\2\u0134\u0137")
        buf.write("\7/\2\2\u0135\u0138\5> \2\u0136\u0138\3\2\2\2\u0137\u0135")
        buf.write("\3\2\2\2\u0137\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139")
        buf.write("\u013c\7\60\2\2\u013a\u013b\7\35\2\2\u013b\u013d\79\2")
        buf.write("\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e\u013f\5\34\17\2\u013f=\3\2\2\2\u0140\u0141")
        buf.write("\5@!\2\u0141\u0142\7\66\2\2\u0142\u0143\5> \2\u0143\u0146")
        buf.write("\3\2\2\2\u0144\u0146\5@!\2\u0145\u0140\3\2\2\2\u0145\u0144")
        buf.write("\3\2\2\2\u0146?\3\2\2\2\u0147\u0149\7\35\2\2\u0148\u0147")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2\u014a")
        buf.write("\u014c\7\33\2\2\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2")
        buf.write("\2\u014c\u014d\3\2\2\2\u014d\u014e\79\2\2\u014e\u014f")
        buf.write("\78\2\2\u014f\u0150\5B\"\2\u0150A\3\2\2\2\u0151\u0155")
        buf.write("\5J&\2\u0152\u0155\5P)\2\u0153\u0155\5N(\2\u0154\u0151")
        buf.write("\3\2\2\2\u0154\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("C\3\2\2\2\u0156\u0159\7\61\2\2\u0157\u015a\5\36\20\2\u0158")
        buf.write("\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015b\u015c\7\62\2\2\u015cE\3\2\2")
        buf.write("\2\u015d\u015e\79\2\2\u015e\u015f\7\63\2\2\u015f\u0160")
        buf.write("\5\36\20\2\u0160\u0161\7\64\2\2\u0161G\3\2\2\2\u0162\u0167")
        buf.write("\5J&\2\u0163\u0167\5L\'\2\u0164\u0167\5P)\2\u0165\u0167")
        buf.write("\5N(\2\u0166\u0162\3\2\2\2\u0166\u0163\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0166\u0165\3\2\2\2\u0167I\3\2\2\2\u0168\u0169")
        buf.write("\t\6\2\2\u0169K\3\2\2\2\u016a\u016b\7\16\2\2\u016bM\3")
        buf.write("\2\2\2\u016c\u016d\7\30\2\2\u016dO\3\2\2\2\u016e\u016f")
        buf.write("\7\36\2\2\u016f\u0170\7\63\2\2\u0170\u0171\5R*\2\u0171")
        buf.write("\u0172\7\64\2\2\u0172\u0173\7\34\2\2\u0173\u0174\5J&\2")
        buf.write("\u0174Q\3\2\2\2\u0175\u0176\7\4\2\2\u0176\u0177\7\66\2")
        buf.write("\2\u0177\u017a\5R*\2\u0178\u017a\7\4\2\2\u0179\u0175\3")
        buf.write("\2\2\2\u0179\u0178\3\2\2\2\u017aS\3\2\2\2\"Y_aejvz\u0087")
        buf.write("\u008d\u00b2\u00bf\u00c6\u00cd\u00d7\u00e2\u00ed\u00f3")
        buf.write("\u00f8\u0103\u010d\u0113\u0128\u012e\u0137\u013c\u0145")
        buf.write("\u0148\u014b\u0154\u0159\u0166\u0179")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecllst" ):
                return visitor.visitDecllst(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat_list" ):
                return visitor.visitStat_list(self)
            else:
                return visitor.visitChildren(self)




    def stat_list(self):

        localctx = MT22Parser.Stat_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat_list)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.FOR, MT22Parser.WHILE, MT22Parser.DO, MT22Parser.IF, MT22Parser.RETURN, MT22Parser.BREAK, MT22Parser.CONTINUE, MT22Parser.LB, MT22Parser.IDENTIFIERS]:
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
            elif token in [MT22Parser.RB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stat" ):
                return visitor.visitAssign_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stat" ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stat" ):
                return visitor.visitFor_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stat" ):
                return visitor.visitWhile_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhile_stat" ):
                return visitor.visitDowhile_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stat" ):
                return visitor.visitBreak_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stat" ):
                return visitor.visitContinue_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFucnt_stat" ):
                return visitor.visitFucnt_stat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stat" ):
                return visitor.visitReturn_stat(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.Lb, MT22Parser.LB, MT22Parser.IDENTIFIERS]:
                self.state = 174
                self.exp()
                pass
            elif token in [MT22Parser.SEMI]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstat" ):
                return visitor.visitBlockstat(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlst" ):
                return visitor.visitExprlst(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUAL) | (1 << MT22Parser.NOT_EQUAL) | (1 << MT22Parser.LT) | (1 << MT22Parser.LE) | (1 << MT22Parser.GT) | (1 << MT22Parser.GE))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



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
                    if not(_la==MT22Parser.ADD or _la==MT22Parser.SUB):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUL) | (1 << MT22Parser.DIV) | (1 << MT22Parser.MOD))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = MT22Parser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp5)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(MT22Parser.NOT)
                self.state = 239
                self.exp5()
                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.SUB, MT22Parser.Lb, MT22Parser.LB, MT22Parser.IDENTIFIERS]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = MT22Parser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp6)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(MT22Parser.SUB)
                self.state = 244
                self.exp6()
                pass
            elif token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.Lb, MT22Parser.LB, MT22Parser.IDENTIFIERS]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubexp" ):
                return visitor.visitSubexp(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctcall" ):
                return visitor.visitFunctcall(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.Lb, MT22Parser.LB, MT22Parser.IDENTIFIERS]:
                self.state = 265
                self.exprlst()
                pass
            elif token in [MT22Parser.Rb]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortvardecl" ):
                return visitor.visitShortvardecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignvardecl" ):
                return visitor.visitAssignvardecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdendecl" ):
                return visitor.visitIdendecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MT22Parser.OUT, MT22Parser.INHERIT, MT22Parser.IDENTIFIERS]:
                self.state = 307
                self.para_list()
                pass
            elif token in [MT22Parser.Rb]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 311
            self.match(MT22Parser.Rb)
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_pattern" ):
                return visitor.visitPara_pattern(self)
            else:
                return visitor.visitChildren(self)




    def para_pattern(self):

        localctx = MT22Parser.Para_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_para_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 325
                self.match(MT22Parser.INHERIT)


            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_decl" ):
                return visitor.visitType_decl(self)
            else:
                return visitor.visitChildren(self)




    def type_decl(self):

        localctx = MT22Parser.Type_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_type_decl)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.atomic_t()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.array_t()
                pass
            elif token in [MT22Parser.AUTO]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




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
            if token in [MT22Parser.INTLIT, MT22Parser.FLOATLIT, MT22Parser.BOOLLIT, MT22Parser.STRINGLIT, MT22Parser.SUB, MT22Parser.NOT, MT22Parser.Lb, MT22Parser.LB, MT22Parser.IDENTIFIERS]:
                self.state = 341
                self.exprlst()
                pass
            elif token in [MT22Parser.RB]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_t" ):
                return visitor.visitAll_t(self)
            else:
                return visitor.visitChildren(self)




    def all_t(self):

        localctx = MT22Parser.All_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_all_t)
        try:
            self.state = 356
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.INTEGER, MT22Parser.STRING, MT22Parser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.atomic_t()
                pass
            elif token in [MT22Parser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.void_t()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.array_t()
                pass
            elif token in [MT22Parser.AUTO]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomic_t" ):
                return visitor.visitAtomic_t(self)
            else:
                return visitor.visitChildren(self)




    def atomic_t(self):

        localctx = MT22Parser.Atomic_tContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_atomic_t)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING) | (1 << MT22Parser.FLOAT))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoid_t" ):
                return visitor.visitVoid_t(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAuto_t" ):
                return visitor.visitAuto_t(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_t" ):
                return visitor.visitArray_t(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensionlist" ):
                return visitor.visitDimensionlist(self)
            else:
                return visitor.visitChildren(self)




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
         




