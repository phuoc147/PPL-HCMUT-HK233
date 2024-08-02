from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllst()))
    def visitDecllst(self, ctx: MT22Parser.DecllstContext):
        if ctx.vardecl(): return list(self.visit(ctx.vardecl())) + list(self.visit(ctx.decllst()) if ctx.decllst() else [])
        else: return [self.visit(ctx.funcdecl())] + list(self.visit(ctx.decllst()) if ctx.decllst() else [])
    
    # *****DECLARATIONS***** # 
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.shortvardecl(): return self.visit(ctx.shortvardecl())
        else: return self.visit(ctx.assignvardecl())
    def visitShortvardecl(self, ctx: MT22Parser.ShortvardeclContext):
        idlist = self.visit(ctx.idendecl())
        typ = self.visit(ctx.type_decl())
        return list(map(lambda id: VarDecl(id,typ),idlist))
    def AssignvardeclHelper(self, ctx: MT22Parser.AssignvardeclContext,lst:list):
        lst[0].append(ctx.IDENTIFIERS().getText())
        lst[1].append(self.visit(ctx.exp()))
        if ctx.type_decl() is None: return self.AssignvardeclHelper(ctx.assignvardecl(),lst)
        else: return self.visit(ctx.type_decl())
    def visitAssignvardecl(self, ctx: MT22Parser.AssignvardeclContext):
        lst = [[],[]]
        typ = self.AssignvardeclHelper(ctx,lst)
        idlist,explist = lst
        explist.reverse()
        return list(map(lambda id,exp: VarDecl(id,typ,exp),idlist,explist))
    def visitIdendecl(self, ctx: MT22Parser.IdendeclContext):
        if ctx.getChildCount() == 1: return [ctx.IDENTIFIERS().getText()]
        return [ctx.IDENTIFIERS().getText()] + self.visit(ctx.idendecl())
    
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        return FuncDecl(
            name= ctx.IDENTIFIERS(0).getText(),
            return_type= self.visit(ctx.all_t()),
            params= [] if ctx.para_list() == None else self.visit(ctx.para_list()),
            inherit= None if ctx.INHERIT() is None else ctx.IDENTIFIERS(1).getText(),
            body= self.visit(ctx.blockstat())       
        )
    def visitPara_list(self, ctx: MT22Parser.Para_listContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.para_pattern()) 
        return self.visit(ctx.para_pattern()) + self.visit(ctx.para_list())
    def visitPara_pattern(self, ctx: MT22Parser.Para_patternContext):
        return [ParamDecl(
            name= ctx.IDENTIFIERS().getText(),
            typ= self.visit(ctx.type_decl()),
            out= False if ctx.OUT() is None else True,
            inherit= False if ctx.INHERIT() is None else True
        )]
    def visitType_decl(self, ctx: MT22Parser.Type_declContext): 
        if ctx.atomic_t(): return self.visit(ctx.atomic_t())
        elif ctx.array_t(): return self.visit(ctx.array_t())
        else: return self.visit(ctx.auto_t())

    # *****STATEMENTS***** #
    def visitStat_list(self,ctx:MT22Parser.Stat_listContext):
        if ctx.getChildCount() == 0: return []
        else:
            if ctx.statement(): return [self.visit(ctx.statement())] + self.visit(ctx.stat_list())
            else: return self.visit(ctx.vardecl()) + self.visit(ctx.stat_list())
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        return self.visitChildren(ctx)
    def visitAssign_stat(self,ctx:MT22Parser.Assign_statContext):
        return AssignStmt(
            lhs=Id(ctx.IDENTIFIERS().getText()) if ctx.IDENTIFIERS() else self.visit(ctx.array_access()),
            rhs=self.visit(ctx.exp())
        )
    def visitBlockstat(self, ctx: MT22Parser.BlockstatContext):
        return BlockStmt(self.visit(ctx.stat_list()))
    def visitIf_stat(self,ctx:MT22Parser.If_statContext):
        return IfStmt(
            cond= self.visit(ctx.exp()),
            tstmt= self.visit(ctx.statement(0)),
            fstmt= self.visit(ctx.statement(1)) if ctx.ELSE() else []
        )
    def visitFor_stat(self,ctx:MT22Parser.For_statContext):  
        return ForStmt(
            init= AssignStmt(lhs=Id(ctx.IDENTIFIERS().getText()) if ctx.IDENTIFIERS() else self.visit(ctx.array_access()),
                             rhs=self.visit(ctx.exp(0))
                             ),
            cond= self.visit(ctx.exp(1)),
            upd= self.visit(ctx.exp(2)),
            stmt= self.visit(ctx.statement())
        )
    def visitWhile_stat(self,ctx:MT22Parser.While_statContext):
        return WhileStmt(
            cond= self.visit(ctx.exp()),
            stmt= self.visit(ctx.statement())
        )
    def visitDowhile_stat(self,ctx:MT22Parser.Dowhile_statContext):
        return DoWhileStmt(
            cond= self.visit(ctx.exp()),
            stmt= self.visit(ctx.blockstat())
        )
    def visitBreak_stat(self,ctx:MT22Parser.Break_statContext):
        return BreakStmt()
    def visitContinue_stat(self,ctx:MT22Parser.Continue_statContext):   
        return ContinueStmt()
    def visitFucnt_stat(self,ctx:MT22Parser.Fucnt_statContext):
        functall = self.visit(ctx.functcall())
        return CallStmt(
            name= functall.name,
            args= functall.args
        )
    def visitFunctcall(self,ctx:MT22Parser.FunctcallContext):
        return FuncCall(
            name= ctx.IDENTIFIERS().getText(),
            args= self.visit(ctx.exprlst()) if ctx.exprlst() else []
        )
    def visitReturn_stat(self,ctx:MT22Parser.Return_statContext):
        return ReturnStmt(self.visit(ctx.exp()) if ctx.exp() else [])

    def visitSpecialcall(self,ctx:MT22Parser.SpecialcallContext):
        return self.visitChildren(ctx)
    def visitReadIntegerfun(self, ctx:MT22Parser.ReadIntegerfunContext):
        return CallStmt("readInteger",[])
    def visitPrintIntegerfun(self, ctx:MT22Parser.PrintIntegerfunContext):
        return CallStmt('printInteger',args=[self.visit(ctx.exp())])
    def visitReadFloatfun(self, ctx:MT22Parser.ReadFloatfunContext):
        return CallStmt('readFloat',[])
    def visitPrintFloatfun(self, ctx:MT22Parser.PrintFloatfunContext):
        return CallStmt('printFloat',args=[self.visit(ctx.exp())])
    def visitReadBooleanfun(self, ctx:MT22Parser.ReadBooleanfunContext):
        return CallStmt('readBoolean',[])
    def visitPrintBooleanfun(self, ctx:MT22Parser.PrintBooleanfunContext):
        return CallStmt('printBoolean',args=[self.visit(ctx.exp())])
    def visitReadStringfun(self, ctx:MT22Parser.ReadStringfunContext):
        return CallStmt('readString',[])
    def visitPrintStringfun(self, ctx:MT22Parser.PrintStringfunContext):
        return CallStmt('printString',args=[self.visit(ctx.exp())])
    def visitSuperfun(self, ctx:MT22Parser.SuperfunContext):
        return CallStmt('super',args=self.visit(ctx.exprlst()) if ctx.exprlst() else [])
    def visitPreventDefaultfun(self,ctx:MT22Parser.PreventDefaultfunContext):
        return CallStmt('preventDefault',[])

    # *****EXPRESSION***** #
    def visitExprlst(self,ctx:MT22Parser.ExprlstContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.exp())]
        return [self.visit(ctx.exp())] + self.visit(ctx.exprlst())
    def visitExp(self,ctx:MT22Parser.ExpContext):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp1(0))
        else: return BinExpr(ctx.CONCAT().getText(),self.visit(ctx.exp1(0)),self.visit(ctx.exp1(1)))
    def visitExp1(self,ctx:MT22Parser.Exp1Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp2(0))
        else: return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
    def visitExp2(self,ctx:MT22Parser.Exp2Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp3())
        else: return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
    def visitExp3(self,ctx:MT22Parser.Exp3Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp4())
        else: return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
    def visitExp4(self,ctx:MT22Parser.Exp4Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp5())
        else: return BinExpr(ctx.getChild(1).getText(),self.visit(ctx.exp4()),self.visit(ctx.exp5()))
    def visitExp5(self,ctx:MT22Parser.Exp5Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp6())
        else: return UnExpr(ctx.NOT().getText(),self.visit(ctx.exp5()))
    def visitExp6(self,ctx:MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1: return self.visit(ctx.exp7())
        else: return UnExpr(ctx.SUB().getText(),self.visit(ctx.exp6()))
    def visitExp7(self,ctx:MT22Parser.Exp7Context):
        if ctx.subexp(): return self.visit(ctx.subexp())
        elif ctx.functcall(): return self.visit(ctx.functcall())
        elif ctx.array_access(): return self.visit(ctx.array_access())
        elif ctx.arraylit(): return self.visit(ctx.arraylit())
        elif ctx.INTLIT(): return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT(): 
            floatlit = ctx.FLOATLIT().getText()
            if floatlit.find(".e") != 1:
                if floatlit[0] == '.': floatlit = "0" + floatlit
            return FloatLit(float(floatlit))
        elif ctx.STRINGLIT(): return StringLit(ctx.STRINGLIT().getText())
        elif ctx.BOOLLIT(): return BooleanLit(True if ctx.BOOLLIT().getText() == 'true' else False)
        else: return Id(ctx.IDENTIFIERS().getText())
    def visitArraylit(self,ctx:MT22Parser.ArraylitContext):
        if ctx.exprlst(): return ArrayLit(self.visit(ctx.exprlst()))
        else: return ArrayLit([])
    def visitSubexp(self,ctx:MT22Parser.SubexpContext):
        return self.visit(ctx.exp())

    # *****TYPE SYSTEM***** #
    
    def visitAll_t(self, ctx: MT22Parser.All_tContext):
        if ctx.atomic_t(): return self.visit(ctx.atomic_t())
        elif ctx.void_t(): return self.visit(ctx.void_t())
        elif ctx.array_t(): return self.visit(ctx.array_t())
        else: return AutoType()
    def visitAtomic_t(self, ctx: MT22Parser.Atomic_tContext):
        if ctx.INTEGER(): return IntegerType()
        elif ctx.BOOLEAN(): return BooleanType()
        elif ctx.FLOAT(): return FloatType()
        else: return StringType()
    def visitAuto_t(self, ctx: MT22Parser.Auto_tContext):
        return AutoType()
    def visitVoid_t(self, ctx: MT22Parser.Void_tContext):
        return VoidType()
    def visitArray_t(self, ctx: MT22Parser.Array_tContext):
        return ArrayType(
            dimensions= self.visit(ctx.dimensionlist()),
            typ= self.visit(ctx.atomic_t())
        )
    def visitDimensionlist(self,ctx:MT22Parser.DimensionlistContext):
        if ctx.getChildCount() == 1: return [ctx.INTLIT().getText()]
        else: return [ctx.INTLIT().getText()] + self.visit(ctx.dimensionlist())
    
    
    def visitArray_access(self, ctx: MT22Parser.Array_accessContext):
        return ArrayCell(
            name= ctx.IDENTIFIERS().getText(),
            cell= self.visit(ctx.exprlst())
        )