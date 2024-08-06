# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllst.
    def visitDecllst(self, ctx:MT22Parser.DecllstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stat_list.
    def visitStat_list(self, ctx:MT22Parser.Stat_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stat.
    def visitAssign_stat(self, ctx:MT22Parser.Assign_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stat.
    def visitIf_stat(self, ctx:MT22Parser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stat.
    def visitFor_stat(self, ctx:MT22Parser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stat.
    def visitWhile_stat(self, ctx:MT22Parser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile_stat.
    def visitDowhile_stat(self, ctx:MT22Parser.Dowhile_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stat.
    def visitBreak_stat(self, ctx:MT22Parser.Break_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stat.
    def visitContinue_stat(self, ctx:MT22Parser.Continue_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fucnt_stat.
    def visitFucnt_stat(self, ctx:MT22Parser.Fucnt_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stat.
    def visitReturn_stat(self, ctx:MT22Parser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstat.
    def visitBlockstat(self, ctx:MT22Parser.BlockstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlst.
    def visitExprlst(self, ctx:MT22Parser.ExprlstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexp.
    def visitSubexp(self, ctx:MT22Parser.SubexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functcall.
    def visitFunctcall(self, ctx:MT22Parser.FunctcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortvardecl.
    def visitShortvardecl(self, ctx:MT22Parser.ShortvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignvardecl.
    def visitAssignvardecl(self, ctx:MT22Parser.AssignvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idendecl.
    def visitIdendecl(self, ctx:MT22Parser.IdendeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list.
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_pattern.
    def visitPara_pattern(self, ctx:MT22Parser.Para_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_decl.
    def visitType_decl(self, ctx:MT22Parser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_access.
    def visitArray_access(self, ctx:MT22Parser.Array_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#all_t.
    def visitAll_t(self, ctx:MT22Parser.All_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_t.
    def visitAtomic_t(self, ctx:MT22Parser.Atomic_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_t.
    def visitVoid_t(self, ctx:MT22Parser.Void_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_t.
    def visitAuto_t(self, ctx:MT22Parser.Auto_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_t.
    def visitArray_t(self, ctx:MT22Parser.Array_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensionlist.
    def visitDimensionlist(self, ctx:MT22Parser.DimensionlistContext):
        return self.visitChildren(ctx)



del MT22Parser