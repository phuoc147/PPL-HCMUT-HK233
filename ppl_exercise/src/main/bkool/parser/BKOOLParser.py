# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\37\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5)\n\5\3\6\3\6\3\6\3\6\3\6\7\6\60\n\6\f\6\16\6\63\13")
        buf.write("\6\3\6\3\6\3\6\7\68\n\6\f\6\16\6;\13\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\5\7E\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7")
        buf.write("M\n\7\f\7\16\7P\13\7\3\b\3\b\3\b\3\b\3\b\7\bW\n\b\f\b")
        buf.write("\16\bZ\13\b\3\b\3\b\3\b\2\3\f\t\2\4\6\b\n\f\16\2\2\2a")
        buf.write("\2\20\3\2\2\2\4\27\3\2\2\2\6\36\3\2\2\2\b(\3\2\2\2\n*")
        buf.write("\3\2\2\2\fD\3\2\2\2\16Q\3\2\2\2\20\21\5\4\3\2\21\22\7")
        buf.write("\2\2\3\22\3\3\2\2\2\23\24\5\f\7\2\24\25\5\6\4\2\25\30")
        buf.write("\3\2\2\2\26\30\3\2\2\2\27\23\3\2\2\2\27\26\3\2\2\2\30")
        buf.write("\5\3\2\2\2\31\32\7\3\2\2\32\33\5\f\7\2\33\34\5\6\4\2\34")
        buf.write("\37\3\2\2\2\35\37\3\2\2\2\36\31\3\2\2\2\36\35\3\2\2\2")
        buf.write("\37\7\3\2\2\2 !\7\16\2\2!\"\7\4\2\2\"#\5\f\7\2#$\7\3\2")
        buf.write("\2$)\3\2\2\2%&\5\f\7\2&\'\7\3\2\2\')\3\2\2\2( \3\2\2\2")
        buf.write("(%\3\2\2\2)\t\3\2\2\2*+\7\16\2\2+,\7\5\2\2,\61\7\16\2")
        buf.write("\2-.\7\6\2\2.\60\7\16\2\2/-\3\2\2\2\60\63\3\2\2\2\61/")
        buf.write("\3\2\2\2\61\62\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64")
        buf.write("\65\7\7\2\2\659\7\b\2\2\668\5\b\5\2\67\66\3\2\2\28;\3")
        buf.write("\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;9\3\2\2\2<=\7\t")
        buf.write("\2\2=\13\3\2\2\2>?\b\7\1\2?E\7\16\2\2@E\7\r\2\2AE\5\16")
        buf.write("\b\2BC\7\n\2\2CE\5\f\7\5D>\3\2\2\2D@\3\2\2\2DA\3\2\2\2")
        buf.write("DB\3\2\2\2EN\3\2\2\2FG\f\4\2\2GH\7\13\2\2HM\5\f\7\5IJ")
        buf.write("\f\3\2\2JK\7\f\2\2KM\5\f\7\4LF\3\2\2\2LI\3\2\2\2MP\3\2")
        buf.write("\2\2NL\3\2\2\2NO\3\2\2\2O\r\3\2\2\2PN\3\2\2\2QR\7\16\2")
        buf.write("\2RS\7\5\2\2SX\5\f\7\2TU\7\6\2\2UW\5\f\7\2VT\3\2\2\2W")
        buf.write("Z\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2[\\\7")
        buf.write("\7\2\2\\\17\3\2\2\2\13\27\36(\619DLNX")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "','", "')'", "'{'", 
                     "'}'", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "ID", 
                      "WS" ]

    RULE_program = 0
    RULE_mlist = 1
    RULE_etail = 2
    RULE_stat = 3
    RULE_defi = 4
    RULE_expr = 5
    RULE_func = 6

    ruleNames =  [ "program", "mlist", "etail", "stat", "defi", "expr", 
                   "func" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INT=11
    ID=12
    WS=13

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

        def mlist(self):
            return self.getTypedRuleContext(BKOOLParser.MlistContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.mlist()
            self.state = 15
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def etail(self):
            return self.getTypedRuleContext(BKOOLParser.EtailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMlist" ):
                return visitor.visitMlist(self)
            else:
                return visitor.visitChildren(self)




    def mlist(self):

        localctx = BKOOLParser.MlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mlist)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__7, BKOOLParser.INT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.etail()
                pass
            elif token in [BKOOLParser.EOF]:
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


    class EtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def etail(self):
            return self.getTypedRuleContext(BKOOLParser.EtailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_etail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEtail" ):
                return visitor.visitEtail(self)
            else:
                return visitor.visitChildren(self)




    def etail(self):

        localctx = BKOOLParser.EtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_etail)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(BKOOLParser.T__0)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.etail()
                pass
            elif token in [BKOOLParser.EOF]:
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


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = BKOOLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(BKOOLParser.ID)
                self.state = 31
                self.match(BKOOLParser.T__1)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(BKOOLParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.expr(0)
                self.state = 36
                self.match(BKOOLParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_defi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefi" ):
                return visitor.visitDefi(self)
            else:
                return visitor.visitChildren(self)




    def defi(self):

        localctx = BKOOLParser.DefiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(BKOOLParser.ID)
            self.state = 41
            self.match(BKOOLParser.T__2)
            self.state = 42
            self.match(BKOOLParser.ID)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.T__3:
                self.state = 43
                self.match(BKOOLParser.T__3)
                self.state = 44
                self.match(BKOOLParser.ID)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(BKOOLParser.T__4)
            self.state = 51
            self.match(BKOOLParser.T__5)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__7) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 52
                self.stat()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(BKOOLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def func(self):
            return self.getTypedRuleContext(BKOOLParser.FuncContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 61
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 62
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 3:
                self.state = 63
                self.func()
                pass

            elif la_ == 4:
                self.state = 64
                self.match(BKOOLParser.T__7)
                self.state = 65
                self.expr(3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 68
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 69
                        self.match(BKOOLParser.T__8)
                        self.state = 70
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 71
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 72
                        self.match(BKOOLParser.T__9)
                        self.state = 73
                        self.expr(2)
                        pass

             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExprContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = BKOOLParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(BKOOLParser.ID)
            self.state = 80
            self.match(BKOOLParser.T__2)
            self.state = 81
            self.expr(0)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.T__3:
                self.state = 82
                self.match(BKOOLParser.T__3)
                self.state = 83
                self.expr(0)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(BKOOLParser.T__4)
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
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




