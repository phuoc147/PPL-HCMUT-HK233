# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mlist.
    def visitMlist(self, ctx:BKOOLParser.MlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#etail.
    def visitEtail(self, ctx:BKOOLParser.EtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stat.
    def visitStat(self, ctx:BKOOLParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#defi.
    def visitDefi(self, ctx:BKOOLParser.DefiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#func.
    def visitFunc(self, ctx:BKOOLParser.FuncContext):
        return self.visitChildren(ctx)



del BKOOLParser