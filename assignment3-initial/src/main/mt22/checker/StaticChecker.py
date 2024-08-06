from Visitor import Visitor
from AST import *
from StaticError import *
import functools
from typing import List

# error when funcdecl doesn't have return ????????
class Array(Type): # rectangular array
    def __init__(self,dimension:List[int],typ:List[Type] = None) -> None:
        self.dimension = dimension
        self.typ = typ
    def out_of_range(self): pass
class FuncType(Type):
    def __init__(self,rettype,paratype:list) -> None:
        self.rettype = rettype
        self.paratype = paratype
        self.return_exist = False
class Name:
    def __init__(self,id:str,typ:Type,kind:Kind) -> None:
        self.id = id
        self.typ = typ
        self.kind = kind
class Scope:
    def __init__(self,name:str,parScope = None) -> None:
        self.name = name
        self.var: List[Name] = []
        self.parScope:Scope = parScope
class Utils:
    def check_autoType(self,lst):
        if isinstance(lst,Array): return False
        if len(lst) >= 4: return True
        return False
        
    def MT22FuncDecl_to_Name(self,vst,funcdecl:FuncDecl):
        lst = [funcdecl.name]
        paratyp = []
        for i in funcdecl.params:
            if i.name in lst: raise Redeclared(vst.parameter,i.name)
            paratyp += [[Name(i.name,vst.visit(i.typ,None),vst.parameter),i.inherit]]
            lst += [i.name]
        return Name(funcdecl.name,FuncType(vst.visit(funcdecl.return_type,None),paratyp),vst.function)
    # if rettype_access is  Bool() of Python -> invalid access
    #                       Array() or primitive data -> valid access
    def ID_Suite_Kind(self,name:str,kind:Kind,o:Scope) -> Name:
        tmp = o
        while(tmp):
            for i in tmp.var:
                if i.id == name : return i
            tmp = tmp.parScope
        raise Undeclared(kind,name)
    def indexOftype(self,x,lst):
        for idx,i in enumerate(lst):
            if type(x) == type(i): 
                return idx
    def checkInList(self,x,lst):
        for i in lst:
            if type(i) == type(x): return True
        return False
    def union2_ListType(self,lst1:list,lst2:list,implicit,ordered = False):
        new_lst1 = []
        new_lst2 = []
        for x in lst1:
            for y in lst2:
                if type(x) == type(y):
                    if not(self.checkInList(x,new_lst1)): new_lst1.append(x)
                    if not(self.checkInList(y,new_lst2)): new_lst2.append(y)
                else:
                    if implicit != None:
                        if self.checkInList(x,implicit) and self.checkInList(y,implicit) :
                            if ((ordered and self.indexOftype(x,implicit) <= self.indexOftype(y,implicit)) or not ordered):
                                if not(self.checkInList(x,new_lst1)): new_lst1.append(x)
                                if not(self.checkInList(y,new_lst2)): new_lst2.append(y)
        return new_lst1,new_lst2
    #op1 op2 typ rettype
    # typ . rettype -> if result is [] typ = typ else typ = result 
    # op1 . typ ; op2 . typ -> if one of results is [] -> typemismatch
    def getTypeOfName(self,name:Name):
        if isinstance(name.typ,FuncType): 
            if isinstance(name.typ.rettype[0],VoidType): return name.id
            return name.typ.rettype
        else: return name.typ
    def setTypeOfName(self,name:Name,typ):
        if isinstance(name.typ,FuncType): name.typ.rettype = typ
        else: name.typ = typ
    def inferType(self,op1:Name,op2:Name,typ:List[Type],rettype,expr,implicit = None) ->Name:
        if isinstance(op1.typ,Array) or isinstance(op2.typ,Array): raise TypeMismatchInExpression(expr)
        tmp1,tmp2 = op1,op2
        op1,op2 = self.getTypeOfName(op1),self.getTypeOfName(op2)
        if isinstance(op1,str) : raise TypeMismatchInExpression(FuncCall(op1,[]))
        if isinstance(op2,str): raise TypeMismatchInExpression(FuncCall(op2,[]))
        typ_tmp,ret= self.union2_ListType(typ,rettype,implicit,True) 
        if implicit: 
            if typ_tmp == []: raise TypeMismatchInExpression(expr)
            else: typ = typ_tmp
        op1,op1_typ = self.union2_ListType(op1,typ,implicit,True)
        op2,op2_typ = self.union2_ListType(op2,typ,implicit,True)
        x,ret1 = self.union2_ListType(op1,ret,implicit,True)
        y,ret2 = self.union2_ListType(op2,ret,implicit,True)
        ret1,ret2 = self.union2_ListType(ret1,ret2,None)
        ret = ret1 if len(ret1) < len(ret2) else ret2
        # op1,op2 = self.union2_ListType(op1,op2) ???????????????
        if op1 == [] or op2 == []: raise TypeMismatchInExpression(expr)
        self.setTypeOfName(tmp1,op1),self.setTypeOfName(tmp2,op2)
        if ret == []: return Name(None,rettype,None)
        else: return Name(None,ret,None)
    def inferUnType(self,op:Name,typ:List[Type],rettype,expr,implicit = None):
        if isinstance(op.typ,Array) and isinstance(rettype,Array): 
            if len(op.typ.dimension) != len(rettype.dimension): raise Exception("")
            for x,y in zip(op.typ.dimension,rettype.dimension):
                if x != y: raise Exception("")
            return True
        tmp1 = None
        if isinstance(typ,Name): tmp1,typ = typ,typ.typ
        tmp = op
        op = self.getTypeOfName(op)
        if isinstance(op,str): raise TypeMismatchInExpression(FuncCall(op,[]))
        typ_tmp,ret= self.union2_ListType(typ,rettype,implicit,True) 
        if implicit: 
            if typ_tmp == []: raise TypeMismatchInExpression(expr)
            else: typ = typ_tmp
        op,op_tmp = self.union2_ListType(op,typ,implicit,True)
        if op == []: raise TypeMismatchInExpression(expr)
        self.setTypeOfName(tmp,op)
        if tmp1: self.setTypeOfName(tmp1,op_tmp)
        if ret == []: return Name(None,rettype,None)
        else: return tmp if tmp.id != None else Name(None,ret,None)
    # def inferAutoType(self,root:Name) ->bool: # return false if can't infer
    #     queue = [root] # ensure root is auto and root.typ[1] and [2] not empty
    #     while len(queue) != 0:
    #         if 

    def infertype_ArrayLit(self,ast,vst,implicit,o:Scope): # return False -> invalid input
        typ = []
        # [1,2,3]
        if isinstance(ast,ArrayLit):
            length = dimen = 0
            for i in ast.explist:
                tmp,dimen = self.infertype_ArrayLit(i,vst,implicit,o)
                if dimen != []:
                    if length == 0: length = dimen[-1]
                    else: 
                        if length != dimen[-1]: return False,False
                else:
                    if length != 0: return False,False
                if typ == []: typ = tmp
                else:
                    # x,y = self.union2_ListType(typ,tmp,implicit,True)
                    # x1,y1 = self.union2_ListType(tmp,typ,implicit,True)
                    # if y == [] and y1 == []: return False,False
                    # typ = y if len(y) >= len(y1) else y1
                    x,y = self.union2_ListType(typ,tmp,None)
                    if x == [] or y == []: return False,False
                    typ = x
            return typ, [len(ast.explist)] + dimen
        else:
            typ = self.getTypeOfName(vst.visit(ast,o))
            return typ,[]
        # func: [[Name,boolean_inherit]]
    def suite_Param(self,func:list,call:List[Expr],vst,o:Scope):
        if len(func) != len(call): return False
        func = [i[0] for i in func]
        call = [vst.visit(i,o) for i in call]
        for x,y in zip(call,func):
            if len(self.getTypeOfName(x)) < 4:
                x,y = self.union2_ListType(self.getTypeOfName(x),self.getTypeOfName(y),[vst.integertype,vst.floattype],True)
                if x == [] or y == []: return False
        return True
class StaticChecker(Visitor):
    def __init__(self,ast) -> None:
        self.utils = Utils()
        self.floattype = FloatType()
        self.integertype = IntegerType()
        self.voidtype = VoidType()
        self.booleantype = BooleanType()
        self.stringtype = StringType()
        self.function = Function()
        self.parameter = Parameter()
        self.variable = Variable()
        self.atomic_t = [self.floattype,self.integertype,self.booleantype,self.stringtype]
        self.autotype = AutoType()
        self.ast = ast
        self.all_funcdecl = []
        
        self.binOps = [
            [['+','-','*','/'],[self.integertype,self.floattype],[self.integertype,self.floattype],[self.integertype,self.floattype]],
            [['%'],[self.integertype],[self.integertype],None],
            [['&&','||'],[self.booleantype],[self.booleantype],None],
            [['<=','>=','>','<'],[self.integertype,self.floattype],[self.booleantype],None],
            [['==','!='],[self.booleantype,self.integertype],[self.booleantype],None],
            [['::'],[self.stringtype],[self.stringtype],None],
            [['!'],[self.booleantype],[self.booleantype],None]
        ]
    def check(self):
        self.visit(self.ast,None)
        return ""
    def visit(self, ast, param):
        return ast.accept(self, param)
    def visitProgram(self, ast:Program, o:Scope):
        prog = Scope("prog")
        lst = prog.var
        lst.append(Name('readInteger',FuncType([self.integertype],[]),self.function))
        lst.append(Name('printInteger',FuncType([self.voidtype],[[Name(None,[self.integertype],self.parameter),0]]),self.function))
        lst.append(Name('readFloat',FuncType([self.floattype],[]),self.function))
        lst.append(Name('writeFloat',FuncType([self.voidtype],[[Name(None,[self.floattype],self.parameter),0]]),self.function))
        lst.append(Name('readBoolean',FuncType([self.booleantype],[]),self.function))
        lst.append(Name('printBoolean',FuncType([self.voidtype],[[Name(None,[self.booleantype],self.parameter),0]]),self.function))
        lst.append(Name('readString',FuncType([self.stringtype],[]),self.function))
        lst.append(Name('printString',FuncType([self.voidtype],[[Name(None,[self.stringtype],self.parameter),0]]),self.function))
        decls = [i for i in ast.decls if isinstance(i,FuncDecl)]
        self.all_funcdecl:List[Name] = [] + prog.var
        self.all_funcdecl  += [Utils().MT22FuncDecl_to_Name(self,i) for i in decls]
        mainExist = False
        for decl in ast.decls:
            self.visit(decl,prog) 
        for decl in self.all_funcdecl:
            if decl.id == "main":
                mainExist = True
                if not(isinstance(decl.typ.rettype[0],VoidType)) or len(decl.typ.paratype) > 0: raise NoEntryPoint()
        if not(mainExist): raise NoEntryPoint()
    ##### Declarations #####
    def visitVarDecl(self, ast:VarDecl, o:Scope):
        #redeclared
        for i in o.var:
            if i.id == ast.name: raise Redeclared(self.variable,ast.name)
        #TypeMM in decl
        left_typ = self.visit(ast.typ,o)
        new_typ = None
        right_auto = False
        left_auto = None
        new_bind = Name(ast.name,left_typ,Variable())
        if ast.init:
            # a = b -> Bin('.',b:exp,a.typ:List[Type])
            self.visit(ast.init,o)
            new_typ = self.visit(BinExpr('.',ast.init,left_typ if isinstance(ast.init,BinExpr) else new_bind),o)
            if new_typ == False: raise TypeMismatchInVarDecl(ast)
            elif isinstance(new_typ,Name): new_bind.typ = new_typ.typ
        else:
            if Utils().check_autoType(left_typ): raise Invalid(Variable(),ast.name)
        o.var.append(new_bind)  

        # print('---- CHECK VARDECL ----')
        # for i in o.var:
        #     print(i.id,' : ',i.typ)
    
    def visitParamDecl(self, ast, param):
        return super().visitParamDecl(ast, param)
    #auto x = auto a + auto b => a->b ; x = 
    def visitFuncDecl(self, ast:FuncDecl, o:Scope):
        # check redeclared ID and global_evir name
        for decl in o.var:
            if decl.id == ast.name: raise Redeclared(self.function,decl.id)
        func_decl = None
        for i in self.all_funcdecl:
            if i.id == ast.name: 
                func_decl = i
                break
        # add new Name into Parent's Scope and make new Scope
        o.var.append(func_decl)
        func_decl = func_decl.typ
        func_scope = Scope(ast.name,parScope= o)
        list_paraName = [i[0] for i in func_decl.paratype]
        func_scope.var += list_paraName
        #1if inherit -> check the existence of parent function
        #2           -> check redeclaration of inherit paramater
        #3           -> if parent has non-empty arglist -> first stmt must be super(par-arglist) or prevenDefault
        #4                                empty arglist -> if first stmt isn't super -> must be prevenDefault           
        parent_name = ast.inherit 
        body = ast.body.body
        parent_exist:Name = False
        start = 0                               
        if parent_name:
            start = 1
            for par_func in self.all_funcdecl:
                if par_func.id == parent_name:
                    inherit = [i[0].id for i in par_func.typ.paratype if i[1]]
                    for i in ast.params:
                        if i.name in inherit: raise Invalid(self.parameter,i.name) #2
                    parent_exist = par_func
            if parent_exist == False: raise Undeclared(Function(),parent_name) #1
            else:
                # check first statement
                if len(body) == 0: raise InvalidStatementInFunction(ast.name)
                first_stmt = body[0]
                func_scope.var += [i[0] for i in parent_exist.typ.paratype if i[1]]
                if len(parent_exist.typ.paratype) != 0:
                    if isinstance(first_stmt,CallStmt):
                        if first_stmt.name == 'super':
                            para = parent_exist.typ.paratype
                            args = first_stmt.args
                            if Utils().suite_Param(para,args,self,func_scope) == False:
                                if len(args) > len(para): 
                                    raise TypeMismatchInExpression(args[len(para)])
                                elif len(args) < len(para):
                                    raise TypeMismatchInExpression()
                        elif first_stmt.name == 'preventDefault':
                            if len(first_stmt.args) > 0: raise TypeMismatchInExpression(first_stmt)
                        else: raise InvalidStatementInFunction(ast.name)
                    else: raise InvalidStatementInFunction(ast.name)
                else: 
                    if isinstance(first_stmt,CallStmt):
                        if first_stmt.name == "preventDefault":
                            start = 1
                        else: start = 0
                #check body (vardecl, stmt) and check existance of return
        return_exist = False
        for i in body[start:]: 
            self.visit(i,func_scope)
        # print('---- CHECK FUNCDECL ----')
        # for i in func_scope.var:
        #     print(i.id," : ",i.typ)
        #if not(return_exist) and not(isinstance(ast.return_type,VoidType)) : raise Invalid(Function(),ast.name)
    ##### Statement ######
    def visitAssignStmt(self, ast:AssignStmt, o:Scope): 
        # LHS: id is  undeclared ? ..... array_ac
        # acess is valid?
        # RHS is valid 
        self.visit(ast.rhs,o).typ
        left = self.visit(ast.lhs,o)
        left_typ = left.typ
        name = self.visit(BinExpr('.',ast.rhs,left_typ if isinstance(ast.rhs,BinExpr) else left),o)
        if name == False: raise TypeMismatchInStatement(ast)
        elif isinstance(name,Name): left.typ = name.typ
        # print('---- CHECK ASSIGN ----')
        # for i in o.var:
        #     print(i.id,' : ',i.typ)
    def visitBlockStmt(self, ast:BlockStmt, o:Scope):
        block_scope = Scope("",o)
        for vardecl_or_stat in ast.body: self.visit(vardecl_or_stat,block_scope)
    def visitIfStmt(self, ast:IfStmt, o:Scope):
        if_scope = Scope("if",parScope= o)
        name = self.visit(ast.cond,if_scope)
        try:
            Utils().inferUnType(name,[self.booleantype],[self.booleantype],ast.cond,None)
        except:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt,if_scope)
        if ast.fstmt: 
            else_scope = Scope("else",parScope= o)
            self.visit(ast.fstmt,else_scope)
    def visitForStmt(self, ast:ForStmt, o:Scope):
        for_scope = Scope("for",parScope=o)
        self.visit(ast.init,for_scope)
        name = self.visit(ast.cond,for_scope)
        try:
            Utils().inferUnType(name,[self.booleantype],[self.booleantype],ast.cond,None)
        except:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.upd,for_scope)
        self.visit(ast.stmt,for_scope)
    def visitWhileStmt(self, ast:WhileStmt, o:Scope): 
        while_scope = Scope('while',o)
        name = self.visit(ast.cond,while_scope)
        try:
            Utils().inferUnType(name,[self.booleantype],[self.booleantype],ast.cond,None)
        except:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt,while_scope)
    def visitDoWhileStmt(self, ast:DoWhileStmt, o:Scope):
        dowhile_scope = Scope("do",o)
        name = self.visit(ast.cond,dowhile_scope)
        try:
            Utils().inferUnType(name,[self.booleantype],[self.booleantype],ast.cond,None)
        except:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.stmt,dowhile_scope)
    def visitBreakStmt(self, ast:BreakStmt, o:Scope): #dowhile ??
        nameSuite = ['for','while','if','else','do','']
        mustbeName = ['for','while','do']
        tmp = o
        while(tmp):
            if not(tmp.name in nameSuite): raise MustInLoop(ast)
            else:
                if tmp.name in mustbeName: return
                tmp = tmp.parScope
        raise MustInLoop(ast)
    def visitContinueStmt(self, ast:ContinueStmt, o:Scope):  # dowhile ??
        nameSuite = ['for','while','if','else','do','']
        mustbeName = ['for','while','do']
        tmp = o
        while(tmp):
            if not(tmp.name in nameSuite): raise MustInLoop(ast)
            else:
                if tmp.name in mustbeName: return
                tmp = tmp.parScope
        raise MustInLoop(ast)
    def visitReturnStmt(self, ast:ReturnStmt, o:Scope):
        exceptName = ['for','while','if','else','prog','']
        tmp = o
        functyp:FuncType = None
        func:Name = None
        #find the function
        while(tmp):
            if not(tmp.name in exceptName):
                x = tmp
                tmp = tmp.parScope
                func = tmp.var[-1]
                functyp = func.typ
                tmp = x
                break
            else: tmp = tmp.parScope
        if tmp is None: raise TypeMismatchInStatement(ast)
        if isinstance(functyp.rettype[0],VoidType):
            if ast.expr != None: raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is None: raise TypeMismatchInStatement(ast)
            else:
                name = self.visit(BinExpr('.',ast.expr,functyp.rettype),o)
                if name == False: raise TypeMismatchInExpression(ast)
                func.typ.rettype = name.typ
                #functyp list[type] -> [Name:Auto]
                #                   -> [Name:Auto,Name:Auto,...] -> encounter !Auto
                #                   -> []
                
    def visitCallStmt(self, ast:CallStmt, o:Scope):  # args passed into TypeMM ????
        #check Undeclared
        func_call = None
        for i in self.all_funcdecl:
            if i.id == ast.name: func_call = i
        if func_call is None: raise Undeclared(self.function,ast.name)
        #check the length of args
        if len(func_call.typ.paratype) != len(ast.args): raise TypeMismatchInStatement(ast)
        if Utils().suite_Param(func_call.typ.paratype,ast.args,self,o) ==  False: 
            raise TypeMismatchInStatement(ast)
    ##### Expression #####
    def visitUnExpr(self, ast:UnExpr, o:Scope):
        typ = self.visit(ast.val,o)
        op = ast.op
        if op == '-': return Utils().inferUnType(typ,[self.integertype,self.floattype],[self.integertype,self.floattype],ast)
        elif op == '!':return Utils().inferUnType(typ,[self.booleantype],[self.booleantype],ast)
    def visitBinExpr(self, ast:BinExpr, o:Scope):
        binOps = self.binOps   # its ele : [[operator],[type must be for op],[return type]]
        op = ast.op
        left_typ,right_typ = None,None
        left,right = ast.left,ast.right
        if op == '.':
            if isinstance(right,Name):# -> a (right) = b (left); a = -2; .... SINGLE ASSIGNMENT
                left = self.visit(left,o)
                # print(right.id,right.typ)
                # print(left.id,left.typ)
                try:
                    Utils().inferUnType(left,right,right.typ,ast,[self.integertype,self.floattype])
                except:
                    return False
                # if isinstance(left.typ,Array):
                #     if len(right.typ) == 4: 
                #         right.typ = left.typ
                #         return
                #     elif not(isinstance(right.typ,Array)): return False
                #     else: right_typ,left_typ = right.typ.typ,left.typ.typ
                # else:
                #     if isinstance(left.typ,Array): return False
                #     else: right_typ,left_typ = right.typ,left.typ
                # left_typ,right_typ = Utils().union2_ListType(left_typ,right_typ,[self.integertype,self.floattype],True)
                # #print(right.id,right.typ)
                # if left_typ == []: return False
                # else: 
                #     if isinstance(left.typ,Array): left.typ.typ,right.typ.typ = left_typ,right_typ
                #     else: left.typ,right.typ = left_typ,right_typ

                # if left.id != None and len(left_typ) >= 4: # -> auto type
                #     left.typ.append(right)
                    # print('ASSIGN AUTO DEPENDENCIES')
                return
            elif not(isinstance(left,BinExpr)):
                try:
                    return Utils().inferUnType(self.visit(left,o),right,right,ast,[self.integertype,self.floattype])
                except:
                    return False
            else:
                left_typ,right_typ = left,right
                exp = left
                op = ([i for i in binOps if exp.op in i[0]])[0]
                typ,x = Utils().union2_ListType(op[2],right_typ,[self.integertype,self.floattype],True)
                if typ == []: return False
                try:
                    if op[3]:
                        op1 = self.visit(BinExpr('.',exp.left,Utils().union2_ListType(op[1],x,op[3],True)[0]),o)
                        op2 = self.visit(BinExpr('.',exp.right,Utils().union2_ListType(op[1],x,op[3],True)[0]),o)
                    else:
                        op1 = self.visit(BinExpr('.',exp.left,op[1]),o)
                        op2 = self.visit(BinExpr('.',exp.right,op[1]),o)
                except:
                    return False
                if op1 == False or op2 == False: return False
                Utils().inferType(op1,op2,op[1],typ,exp,op[3])
                return Name(None,x,None)
        else: 
            left_typ,right_typ = self.visit(left,o),self.visit(right,o)
            for binOp  in binOps:
                if op in binOp[0]:
                    return Utils().inferType(left_typ,right_typ,binOp[1],binOp[2],ast,binOp[3])
    ##### LITERAL #####
    def visitArrayCell(self, ast:ArrayCell, o:Scope):
        # check Undeclared 
        typ = None
        typ = self.visit(Id(ast.name),o).typ
        # check length and check list is IntegerType 
        if not(isinstance(typ,Array)): raise TypeMismatchInExpression(ast) 
        exprs = ast.cell
        len_orgin = len(typ.dimension)
        len_access = len(exprs)
        if len_orgin < len_access: raise TypeMismatchInExpression(ast)
        for expr in exprs:
            Utils().inferUnType(self.visit(expr,o),[self.integertype],[self.integertype],expr,[self.integertype,self.floattype])
            # name = self.visit(BinExpr('.',expr,[self.integertype] if isinstance(expr,BinExpr) else self.visit(expr,o)),o)
            # if name == False: raise TypeMismatchInExpression(ast)
        if len_orgin == len_access: return Name(None,typ.typ,None)
        elif len_orgin > len_access: return Array(dimension=exprs[(len_orgin - len_access):],typ=typ.typ)

        
    def visitIntegerLit(self, ast, o:Scope): return Name(None,[self.integertype],None)
    def visitFloatLit(self, ast, o:Scope): return Name(None,[self.floattype],None)
    def visitStringLit(self, ast, o:Scope): return Name(None,[self.stringtype],None)
    def visitBooleanLit(self, ast, o:Scope): return Name(None,[self.booleantype],None)
    # auto a; float x = a + 2; bool y = a == 2
    def visitArrayLit(self, ast:ArrayLit, o:Scope) -> Array:
        #{1,a} -> infer a is integer
         
        typ,dimension = Utils().infertype_ArrayLit(ast,self,[self.integertype,self.floattype],o)
        if typ == False: raise IllegalArrayLiteral(ast)
        array_t = Array(dimension,typ)
        return Name(None,array_t,None)
    def visitFuncCall(self, ast:FuncCall, o:Scope):
        #check Undeclared
        func_call = None
        for i in self.all_funcdecl:
            if i.id == ast.name: func_call = i
        if func_call is None: raise Undeclared(self.function,ast.name)
        #check the length of args
        if len(func_call.typ.paratype) != len(ast.args): raise TypeMismatchInExpression(ast)
        if Utils().suite_Param(func_call.typ.paratype,ast.args,self,o) ==  False: 
            raise TypeMismatchInExpression(ast)
        return func_call
    def visitId(self, id:Id, o:Scope) -> Name:
        #Undeclared -> no raise error when 
        tmp = o
        while(tmp):
            for decl in tmp.var:
                if decl.id == id.name:
                        if type(decl.kind) != type(Function()) : return decl
            tmp = tmp.parScope
        raise Undeclared(Identifier(),id.name)
    def visitIntegerType(self, ast, param): return [self.integertype]
    def visitFloatType(self, ast, param): return [self.floattype]
    def visitBooleanType(self, ast, param): return [self.booleantype]
    def visitStringType(self, ast, param): return [self.stringtype]
    def visitArrayType(self, ast:ArrayType, param): 
        typ = self.integertype
        for i in self.atomic_t: 
            if type(i) == type(ast.typ): typ = i
        return Array([int(i) for i in ast.dimensions],[typ])
    def visitAutoType(self, ast, param): return self.atomic_t
    def visitVoidType(self, ast, param): return [self.voidtype]