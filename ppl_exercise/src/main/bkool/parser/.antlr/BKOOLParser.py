# Generated from d:/PPL_HCMUT/ppl_exercise/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
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
        4,1,17,122,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        3,1,30,8,1,1,2,1,2,1,2,3,2,35,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,43,
        8,3,1,4,1,4,3,4,47,8,4,1,5,1,5,1,5,3,5,52,8,5,1,6,1,6,1,6,1,6,1,
        6,3,6,59,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,69,8,7,1,8,1,8,
        1,8,1,8,1,8,5,8,76,8,8,10,8,12,8,79,9,8,1,8,1,8,1,8,5,8,84,8,8,10,
        8,12,8,87,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,97,8,9,1,9,1,9,
        1,9,1,9,1,9,1,9,5,9,105,8,9,10,9,12,9,108,9,9,1,10,1,10,1,10,1,10,
        1,10,5,10,115,8,10,10,10,12,10,118,9,10,1,10,1,10,1,10,0,1,18,11,
        0,2,4,6,8,10,12,14,16,18,20,0,0,125,0,22,1,0,0,0,2,29,1,0,0,0,4,
        34,1,0,0,0,6,42,1,0,0,0,8,46,1,0,0,0,10,51,1,0,0,0,12,58,1,0,0,0,
        14,68,1,0,0,0,16,70,1,0,0,0,18,96,1,0,0,0,20,109,1,0,0,0,22,23,3,
        2,1,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,3,18,9,0,26,27,3,12,6,0,27,
        30,1,0,0,0,28,30,1,0,0,0,29,25,1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,
        0,31,32,5,1,0,0,32,35,3,6,3,0,33,35,1,0,0,0,34,31,1,0,0,0,34,33,
        1,0,0,0,35,5,1,0,0,0,36,37,3,4,2,0,37,38,5,2,0,0,38,43,1,0,0,0,39,
        40,5,3,0,0,40,41,5,1,0,0,41,43,5,2,0,0,42,36,1,0,0,0,42,39,1,0,0,
        0,43,7,1,0,0,0,44,47,3,10,5,0,45,47,1,0,0,0,46,44,1,0,0,0,46,45,
        1,0,0,0,47,9,1,0,0,0,48,49,5,4,0,0,49,52,3,8,4,0,50,52,1,0,0,0,51,
        48,1,0,0,0,51,50,1,0,0,0,52,11,1,0,0,0,53,54,5,5,0,0,54,55,3,18,
        9,0,55,56,3,12,6,0,56,59,1,0,0,0,57,59,1,0,0,0,58,53,1,0,0,0,58,
        57,1,0,0,0,59,13,1,0,0,0,60,61,5,16,0,0,61,62,5,6,0,0,62,63,3,18,
        9,0,63,64,5,5,0,0,64,69,1,0,0,0,65,66,3,18,9,0,66,67,5,5,0,0,67,
        69,1,0,0,0,68,60,1,0,0,0,68,65,1,0,0,0,69,15,1,0,0,0,70,71,5,16,
        0,0,71,72,5,7,0,0,72,77,5,16,0,0,73,74,5,8,0,0,74,76,5,16,0,0,75,
        73,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,
        0,79,77,1,0,0,0,80,81,5,9,0,0,81,85,5,10,0,0,82,84,3,14,7,0,83,82,
        1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,
        87,85,1,0,0,0,88,89,5,11,0,0,89,17,1,0,0,0,90,91,6,9,-1,0,91,97,
        5,16,0,0,92,97,5,15,0,0,93,97,3,20,10,0,94,95,5,12,0,0,95,97,3,18,
        9,3,96,90,1,0,0,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,97,106,
        1,0,0,0,98,99,10,2,0,0,99,100,5,13,0,0,100,105,3,18,9,3,101,102,
        10,1,0,0,102,103,5,14,0,0,103,105,3,18,9,2,104,98,1,0,0,0,104,101,
        1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,19,1,
        0,0,0,108,106,1,0,0,0,109,110,5,16,0,0,110,111,5,7,0,0,111,116,3,
        18,9,0,112,113,5,8,0,0,113,115,3,18,9,0,114,112,1,0,0,0,115,118,
        1,0,0,0,116,114,1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,116,
        1,0,0,0,119,120,5,9,0,0,120,21,1,0,0,0,13,29,34,42,46,51,58,68,77,
        85,96,104,106,116
    ]

class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'M'", "'N'", "'P'", "'f'", "';'", "'='", 
                     "'('", "','", "')'", "'{'", "'}'", "'not'", "'and'", 
                     "'or'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "ID", 
                      "WS" ]

    RULE_program = 0
    RULE_mlist = 1
    RULE_decl = 2
    RULE_decl_tail = 3
    RULE_a = 4
    RULE_b = 5
    RULE_etail = 6
    RULE_stat = 7
    RULE_defi = 8
    RULE_expr = 9
    RULE_func = 10

    ruleNames =  [ "program", "mlist", "decl", "decl_tail", "a", "b", "etail", 
                   "stat", "defi", "expr", "func" ]

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
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    INT=15
    ID=16
    WS=17

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

        def mlist(self):
            return self.getTypedRuleContext(BKOOLParser.MlistContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.mlist()
            self.state = 23
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




    def mlist(self):

        localctx = BKOOLParser.MlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mlist)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.etail()
                pass
            elif token in [-1]:
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


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(BKOOLParser.T__0)
                self.state = 32
                self.decl_tail()
                pass
            elif token in [2]:
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


    class Decl_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_tail




    def decl_tail(self):

        localctx = BKOOLParser.Decl_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decl_tail)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.decl()
                self.state = 37
                self.match(BKOOLParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(BKOOLParser.T__2)
                self.state = 40
                self.match(BKOOLParser.T__0)
                self.state = 41
                self.match(BKOOLParser.T__1)
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


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def b(self):
            return self.getTypedRuleContext(BKOOLParser.BContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_a




    def a(self):

        localctx = BKOOLParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_a)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.b()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a(self):
            return self.getTypedRuleContext(BKOOLParser.AContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_b




    def b(self):

        localctx = BKOOLParser.BContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_b)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(BKOOLParser.T__3)
                self.state = 49
                self.a()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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




    def etail(self):

        localctx = BKOOLParser.EtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_etail)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(BKOOLParser.T__4)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.etail()
                pass
            elif token in [-1]:
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




    def stat(self):

        localctx = BKOOLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stat)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.match(BKOOLParser.ID)
                self.state = 61
                self.match(BKOOLParser.T__5)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(BKOOLParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(BKOOLParser.T__4)
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




    def defi(self):

        localctx = BKOOLParser.DefiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_defi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(BKOOLParser.ID)
            self.state = 71
            self.match(BKOOLParser.T__6)
            self.state = 72
            self.match(BKOOLParser.ID)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 73
                self.match(BKOOLParser.T__7)
                self.state = 74
                self.match(BKOOLParser.ID)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(BKOOLParser.T__8)
            self.state = 81
            self.match(BKOOLParser.T__9)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 102400) != 0):
                self.state = 82
                self.stat()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(BKOOLParser.T__10)
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 91
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 92
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 3:
                self.state = 93
                self.func()
                pass

            elif la_ == 4:
                self.state = 94
                self.match(BKOOLParser.T__11)
                self.state = 95
                self.expr(3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 104
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 99
                        self.match(BKOOLParser.T__12)
                        self.state = 100
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 102
                        self.match(BKOOLParser.T__13)
                        self.state = 103
                        self.expr(2)
                        pass

             
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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




    def func(self):

        localctx = BKOOLParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(BKOOLParser.ID)
            self.state = 110
            self.match(BKOOLParser.T__6)
            self.state = 111
            self.expr(0)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 112
                self.match(BKOOLParser.T__7)
                self.state = 113
                self.expr(0)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self.match(BKOOLParser.T__8)
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
        self._predicates[9] = self.expr_sempred
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
         




