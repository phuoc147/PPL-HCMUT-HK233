from Visitor import Visitor
from AST import *
from StaticError import *
import functools
from typing import List

# error when funcdecl doesn't have return ????????
class Array(Type): # rectangular array
    def __init__(self,dimension:List[int],typ:Type = None) -> None:
        self.dimension = dimension
        self.typ = typ
    def out_of_range(self): pass
    def check_valid_data(self,multiD_list:ArrayLit):
        check_dimen = [multiD_list]
        for i in self.dimension:
            tmp = []
            for j in check_dimen:
                if len(j.explist) != i: return False
                else: tmp += j.explist
            check_dimen = tmp.copy()
        first_type = type(check_dimen[0])
        if first_type != type(self.typ): pass
        for elem in check_dimen:
            if type(elem) != first_type:
                return False
        return True
    def __str__(self):
        return "ArrayType([{}], {})".format(", ".join([str(dimen) for dimen in self.dimension]), str(self.typ))
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
    def check_autoType(self,lst:list):
        if isinstance(lst[0],AutoType): return True
        return False
    def check_same_Array(self,arr1:Array,arr2:Array):
        if list(arr1.dimension) == list(arr2.dimension) and type(arr1.typ) == type(arr2.typ):
            return True
        return False
    def dimension_OneTypeArray(self,array:ArrayLit) -> list:
        tmp = array
        dimension = []
        while(isinstance(tmp,ArrayLit)):
            dimension.append(len(tmp.explist))
            tmp = tmp.explist[0]
        return dimension,tmp
    def validArgType_FuncCall(self,call_agr,declared_agr): 
        if len(call_agr) != len(declared_agr): return False
        for elem1,elem2 in zip(call_agr,declared_agr):
            if type(elem1) != type(elem2) and isinstance(elem1,AutoType) and isinstance(elem2,AutoType) :
                return False
        return True
    def MT22FuncDecl_to_FuncType(self,vst,funcdecl:FuncDecl):
        paratyp = [[vst.visit(i.typ,None),i.inherit] for i in funcdecl.params]
        return FuncType([funcdecl.return_type],paratyp)
    # if rettype_access is  Bool() of Python -> invalid access
    #                       Array() or primitive data -> valid access
    def redeclare_InheritParam(self,child:List[ParamDecl],par:List[ParamDecl]):
        inherit = [i.name for i in par if i.inherit]
        for i in child:
            if i.name in inherit: return i.name
        return ''
    def ID_Suite_Kind(self,id,kind:Kind,o:Scope) -> Name:
        name:str = id.name if isinstance(id,Id) else id
        tmp = o
        while(tmp):
            for i in tmp.var:
                if i.id == name and type(i.kind) == type(kind): return i
            tmp = tmp.var
        raise Undeclared(kind,name)
    def find_returnAutoParam(self,id:Name,param:List[Name])->Name:
        for idx,i in enumerate(param):
            if id.id == i.id: return idx,i
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
        utils = Utils()
        for x in lst1:
            for y in lst2:
                if type(x) == type(y):
                    if not(utils.checkInList(x,new_lst1)): new_lst1.append(x)
                    if not(utils.checkInList(y,new_lst2)): new_lst2.append(y)
                else:
                    if implicit != None:
                        if utils.checkInList(x,implicit) and utils.checkInList(y,implicit) :
                            if ((ordered and utils.indexOftype(x,implicit) <= utils.indexOftype(y,implicit)) or not ordered):
                                if not(utils.checkInList(x,new_lst1)): new_lst1.append(x)
                                if not(utils.checkInList(y,new_lst2)): new_lst2.append(y)
        return new_lst1,new_lst2
    #op1 op2 typ rettype
    # typ . rettype -> if result is [] typ = typ else typ = result 
    # op1 . typ ; op2 . typ -> if one of results is [] -> typemismatch
    def inferType(self,op1:Name,op2:Name,typ:List[Type],rettype,expr,implicit = None) ->Name:
        op1_auto = True if isinstance(op1.typ[0],AutoType) else False
        op2_auto = True if isinstance(op2.typ[0],AutoType) else False
        tmp1,tmp2 = op1,op2
        op1 = op1.typ if not(op1_auto) else typ if op1.typ[2] == [] else op1.typ[2]
        op2 = op2.typ if not(op2_auto) else typ if op2.typ[2] == [] else op2.typ[2]
        typ_tmp,ret= self.union2_ListType(typ,rettype,implicit,True) 
        if implicit: 
            if typ_tmp == []: raise TypeMismatchInExpression(expr)
            else: typ = typ_tmp
        op1,op1_typ = self.union2_ListType(op1,typ,implicit,True)
        op2,op2_typ = self.union2_ListType(op2,typ,implicit,True)
        op1,op2 = self.union2_ListType(op1,op2,implicit)
        if op1 == [] or op2 == []: raise TypeMismatchInExpression(expr)
        if not op1_auto: tmp1.typ = op1
        else: tmp1.typ[2] = op1
        if not op2_auto: tmp2.typ = op2
        else: tmp2.typ[2] = op2
        if ret == []: return Name(None,rettype,None)
        else: return Name(None,ret,None)
    def inferUnType(self,op:Name,typ:List[Type],rettype,expr,implicit = None):
        op_auto = True if isinstance(op.typ[0],AutoType) else False
        tmp = op
        op = op.typ if not(op_auto) else typ if op.typ[2] == [] else op.typ[2]
        typ_tmp,ret= self.union2_ListType(typ,rettype,implicit,True) 
        if implicit: 
            if typ_tmp == []: raise TypeMismatchInExpression(expr)
            else: typ = typ_tmp
        op,op_tmp = self.union2_ListType(op,typ,implicit,True)
        if op == []: raise TypeMismatchInExpression(expr)
        if not op_auto: tmp.typ = op
        else: tmp.typ[2] = op
        if ret == []: return Name(None,rettype,None)
        else: return tmp if tmp.id != None else Name(None,ret,None)
    # def inferAutoType(self,root:Name) ->bool: # return false if can't infer
    #     queue = [root] # ensure root is auto and root.typ[1] and [2] not empty
    #     while len(queue) != 0:
    #         if 
class StaticChecker(Visitor):
    def __init__(self,ast) -> None:
        self.utils = Utils()
        self.floattype = FloatType()
        self.integertype = IntegerType()
        self.voidtype = VoidType()
        self.booleantype = BooleanType()
        self.stringtype = StringType()
        self.atomic_t = [self.floattype,self.integertype,self.booleantype,self.stringtype]
        self.autotype = AutoType()
        self.ast = ast
        self.all_funcdecl = []
        self.global_evir:List[Name] = []
        lst = self.global_evir
        lst.append(Name('readInteger',FuncType(self.integertype,[]),Function()))
        lst.append(Name('printInteger',FuncType(self.voidtype,[self.integertype]),Function()))
        lst.append(Name('readFloat',FuncType(self.floattype,[]),Function()))
        lst.append(Name('printFloat',FuncType(self.voidtype,[self.floattype]),Function()))
        lst.append(Name('readBoolean',FuncType(self.booleantype,[]),Function()))
        lst.append(Name('printBoolean',FuncType(self.voidtype,[self.booleantype]),Function()))
        lst.append(Name('readString',FuncType(self.stringtype,[]),Function()))
        lst.append(Name('printString',FuncType(self.voidtype,[self.stringtype]),Function()))
        self.binOps = [
            [['+','-','*','/'],[self.integertype,self.floattype],[self.integertype,self.floattype],[self.integertype,self.floattype]],
            [['%'],[self.integertype],[self.integertype],None],
            [['&&','||'],[self.booleantype],[self.booleantype],None],
            [['==','>=','>','<'],[self.booleantype,self.integertype],[self.booleantype],None],
            [['::'],[self.stringtype],[self.stringtype],None],
            [['!'],[self.booleantype],[self.booleantype],None]
        ]
    def check(self):
        self.visit(self.ast,None)
        return []
    def visit(self, ast, param):
        return ast.accept(self, param)
    def visitProgram(self, ast:Program, o:Scope):
        prog = Scope("prog")
        decls = [i for i in ast.decls if isinstance(i,FuncDecl)]
        self.all_funcdecl = [[i,Utils().MT22FuncDecl_to_FuncType(self,i)] for i in decls]
        mainExist = False
        for decl,functype in self.all_funcdecl:
            if decl.name == "main":
                mainExist = True
                if not(isinstance(decl.return_type,VoidType)) or len(decl.params) > 0: raise NoEntryPoint()
        if not(mainExist): raise NoEntryPoint()
        for decl in ast.decls:
            self.visit(decl,prog) 
    ##### Declarations #####
    def visitVarDecl(self, ast:VarDecl, o:Scope):
        #redeclared
        for i in o.var:
            if i.id == ast.name: raise Redeclared(Variable(),ast.name)
        #TypeMM in decl
        left_typ = self.visit(ast.typ,o)
        new_typ = None
        right_auto = False
        left_auto = None
        if ast.init: 
            if isinstance(left_typ[0],AutoType): left_typ = self.atomic_t
            new_typ = self.visit(BinExpr('.',ast.init,left_typ),o)
            if new_typ == False: raise TypeMismatchInVarDecl(ast)
        else:
            if Utils().check_autoType(left_typ): raise Invalid(Variable(),ast.name)
        new_bind = Name(ast.name,new_typ.typ,Variable())
        if len(new_typ) == 4: 
            print("APPEND DECL")
            left_auto.typ[1].append(new_bind) 
        o.var.append(new_bind)  
    
        for i in o.var:
            print(i.id,i.typ)
    
    def visitParamDecl(self, ast, param):
        return super().visitParamDecl(ast, param)
    #auto x = auto a + auto b => a->b ; x = 
    def visitFuncDecl(self, ast:FuncDecl, o:Scope):
        # check redeclared ID and global_evir name
        for global_evir in self.global_evir:
            if ast.name == global_evir.id: raise Redeclared(Function,ast.name)
        for decl in o.var:
            if decl.id == ast.name and isinstance(decl.kind,Function): raise Redeclared(Function,decl.id)
        # add new Name into Parent's Scope and make new Scope
        func_scope = Scope(ast.name,parScope= o)
        param = ast.params
        list_paraName = [Name(i.name,[self.autotype,[],[]] if isinstance(i.typ,AutoType) else [i.typ],Parameter()) for i in ast.params]
        o.var.append(Name(ast.name,FuncType(rettype=[self.autotype,[],[]],
                                            paratype=list_paraName),Function()))
        func_scope.var += list_paraName
        #1if inherit -> check the existence of parent function
        #2           -> check redeclaration of inherit paramater
        #3           -> if parent has non-empty arglist -> first stmt must be super(par-arglist) or prevenDefault
        #4                                empty arglist -> if first stmt isn't super -> must be prevenDefault           
        parent_name = ast.inherit 
        body = ast.body.body
        parent_exist:FuncType = None 
        start = 0                               
        if parent_name:
            start = 1
            for decl,functype in self.all_funcdecl:
                if decl.name == ast.name:
                    redecl = Utils().redeclare_InheritParam(ast.params,decl.params)
                    if redecl != '': raise Redeclared(Parameter(),redecl) #2
                    parent_exist = functype
                    break
            if parent_exist is None: raise Undeclared(Function(),parent_name) #1
            else:
                # check first statement
                if len(body) == 0: raise InvalidStatementInFunction(ast.name)
                first_stmt = body[0]
                if isinstance(first_stmt,CallStmt):
                    if first_stmt.name == 'super':
                        args = [self.visit(i,o) for i in first_stmt.args]
                        if not(Utils().validArgType_FuncCall(args,[i[0] for i in parent_exist.paratype])): raise TypeMismatchInExpression(first_stmt)
                    elif first_stmt.name == 'preventDefault':
                        if len(first_stmt.args) > 0: raise TypeMismatchInExpression(first_stmt)
                    else: raise InvalidStatementInFunction(ast.name)
                else: raise InvalidStatementInFunction(ast.name) 
        #check body (vardecl, stmt) and check existance of return
        return_exist = False
        for i in body[start:]: self.visit(i,func_scope)
        #if not(return_exist) and not(isinstance(ast.return_type,VoidType)) : raise Invalid(Function(),ast.name)
    ##### Statement ######
    def visitAssignStmt(self, ast:AssignStmt, o:Scope): 
        # LHS: id is  undeclared ? ..... array_ac
        # acess is valid?
        # RHS is valid 
        left = self.visit(ast.lhs,o)
        left_typ = left.typ[2] if isinstance(left.typ[0],AutoType) else left.typ
        if left_typ == []: left_typ = left.typ[2] = self.atomic_t
        name = self.visit(BinExpr('.',ast.rhs,left_typ),o)
        if name == False: raise TypeMismatchInStatement(ast)
        if len(name.typ) > 4:
            print("APPEND ASSIGN")
            name.typ[1].append(left) 
        print('---- CHECK ASSIGN ----')
        for i in o.var:
            print(i.id,' : ',i.typ)
    def visitBlockStmt(self, ast:BlockStmt, o:Scope):
        for vardecl_or_stat in ast.body: self.visit(vardecl_or_stat,o)
    def visitIfStmt(self, ast:IfStmt, o:Scope):
        if_scope = Scope("if",parScope= o)
        if not(isinstance(self.visit(ast.cond,o),BooleanType)): raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt,if_scope)
        if ast.fstmt: 
            else_scope = Scope("else",parScope= o)
            self.visit(ast.fstmt,else_scope)
    def visitForStmt(self, ast, o:Scope): pass
    def visitWhileStmt(self, ast, o:Scope): pass
    def visitDoWhileStmt(self, ast, o:Scope): pass
    def visitBreakStmt(self, ast:BreakStmt, o:Scope): #dowhile ??
        nameSuite = ['for','while','if','else']
        mustbeName = ['for','while']
        tmp = o
        while(tmp):
            if tmp.name == "": continue
            elif not(tmp.name in nameSuite): raise MustInLoop(ast)
            else:
                if tmp.name in mustbeName: return
        raise MustInLoop(ast)
    def visitContinueStmt(self, ast:ContinueStmt, o:Scope):  # dowhile ??
        nameSuite = ['for','while','if','else']
        mustbeName = ['for','while']
        tmp = o
        while(tmp):
            if tmp.name == "": continue
            elif not(tmp.name in nameSuite): raise MustInLoop(ast)
            else:
                if tmp.name in mustbeName: return
        raise MustInLoop(ast)
    def visitReturnStmt(self, ast:ReturnStmt, o:Scope):
        exceptName = ['for','while','if','else','prog']
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
        if isinstance(functyp[0],VoidType):
            if ast.expr != None: raise TypeMismatchInStatement(ast)
        else:
            if ast.expr is None: raise TypeMismatchInStatement(ast)
            else:
                try:
                    self.visit(BinExpr('.',ast.expr,functyp))
                except:
                    raise TypeMismatchInExpression(ast)
                #functyp list[type] -> [Name:Auto]
                #                   -> [Name:Auto,Name:Auto,...] -> encounter !Auto
                #                   -> []
                
    def visitCallStmt(self, ast:CallStmt, o:Scope):  # args passed into TypeMM ????
        #check Undeclared
        func_decl = self.visit(Id(ast.name),[o,Function(),None])
        #check the length of args and check the type of argument
        agrs = [self.visit(i,o) for i in ast.args]
        param:List[Type] = [i[0] for i in func_decl.paratype ]
        if not(Utils().validArgType_FuncCall(agrs,param)): raise TypeMismatchInExpression
    ##### Expression #####
    def visitUnExpr(self, ast:UnExpr, o:Scope):
        typ = self.visit(ast.val,o).typ if not(isinstance(ast.val),Id) else [Utils().ID_Suite_Kind(ast.val.name,Variable(),o).typ]
        op = ast.op
        if op == '-': return Utils().inferUnType(typ,[self.integertype,self.floattype],[self.integertype,self.floattype],ast)
        elif op == '!':return Utils().inferUnType(typ,[self.booleantype],[self.booleantype],ast)
    def visitBinExpr(self, ast:BinExpr, o:Scope):
        binOps = self.binOps   # its ele : [[operator],[type must be for op],[return type]]
        op = ast.op
        left_typ,right_typ = None,None
        left,right = ast.left,ast.right
        if op == '.':
            if not(isinstance(left,BinExpr)):
                try:
                    return Utils().inferUnType(self.visit(left,o),right,right,ast,[self.integertype,self.floattype])
                except:
                    return False
            
            else:
                left_typ,right_typ = left,right
                self.visit(left_typ,o)   # check typemismatchinExp first -> check coerce 
                exp = left
                op = ([i for i in binOps if exp.op in i[0]])[0]
                x,typ = Utils().union2_ListType(op[2],right_typ,op[3],False if op[3] else True)
                if typ == []: return False
                try:
                    op1 = self.visit(BinExpr('.',exp.left,typ),o)
                    op2 = self.visit(BinExpr('.',exp.right,typ),o)
                except:
                    return False
                if op1 == False or op2 == False: return False
                return Utils().inferType(op1,op2,op[1],typ,exp,op[3])
        else: 
            left_typ,right_typ = self.visit(left,o),self.visit(right,o)
            for binOp  in binOps:
                if op in binOp[0]:
                    return Utils().inferType(left_typ,right_typ,binOp[1],binOp[2],ast,binOp[3])
    ##### LITERAL #####
    def visitArrayCell(self, ast:ArrayCell, o:Scope):
        # check Undeclared 
        typ:Array = None
        try: typ = self.visit(Id(ast.name),[o,None,Array([])]).typ
        except Undeclared: pass
        except: raise TypeMismatchInExpression(ast)
        # check length and check list is IntegerType 
        exprs = [self.visit(i,o) for i in ast.cell]
        len_orgin = len(typ.dimension)
        len_access = len(exprs)
        if len_orgin < len_access: raise TypeMismatchInExpression(ast)
        for expr in exprs:
            if not(isinstance(self.visit(expr),IntegerType)): raise TypeMismatchInExpression(ast)
        if len_orgin == len_access: return typ.typ
        elif len_orgin > len_access: return Array(dimension=exprs[(len_orgin - len_access):],typ=typ.typ)

        
    def visitIntegerLit(self, ast, o:Scope): return Name(None,[self.integertype],None)
    def visitFloatLit(self, ast, o:Scope): return Name(None,[self.floattype],None)
    def visitStringLit(self, ast, o:Scope): return Name(None,[self.stringtype],None)
    def visitBooleanLit(self, ast, o:Scope): return Name(None,[self.booleantype],None)
    # auto a; float x = a + 2; bool y = a == 2
    def visitArrayLit(self, ast:ArrayLit, o:Scope) -> Array:
        #{1,a} -> infer a is integer
        if len(ast.explist) == 0: return
        dimension,typ = Utils().dimension_OneTypeArray(ast)
        array_t = Array(dimension,self.visit(typ,o))
        if not(array_t.check_valid_data(ast)): raise IllegalArrayLiteral(ast)
        return [array_t]
    def visitFuncCall(self, ast:FuncCall, o:Scope):
        agrs = [self.visit(i,o) for i in ast.args] if len(ast.args) > 0 else []
        for i in self.global_evir:
            if ast.name == i.id:
                if not(Utils().validArgType_FuncCall(agrs,[x[0] for x in i.typ.paratype])): raise TypeMismatchInExpression(ast)
        #check Undeclared
        func_call:FuncType = self.visit(Id(ast.name),[o,Function(),None]).typ

        #check the length of args
        param:List[Type] = func_call.paratype
        if not(Utils().validArgType_FuncCall(agrs,[i[0] for i in param])): raise TypeMismatchInExpression(ast)
        return func_call.rettype
    def visitId(self, id:Id, o:Scope) -> Name:
        #Undeclared -> no raise error when 
        tmp = o
        while(tmp):
            for decl in tmp.var:
                if decl.id == id.name:
                        if type(decl.kind) != type(Function()) : return decl
            tmp = tmp.parScope
        raise Undeclared(Identifier(),id)
    def visitIntegerType(self, ast, param): return [self.integertype]
    def visitFloatType(self, ast, param): return [self.floattype]
    def visitBooleanType(self, ast, param): return [self.booleantype]
    def visitStringType(self, ast, param): return [self.stringtype]
    def visitArrayType(self, ast:ArrayType, param): 
        return Array(dimension=[int(i) for i in ast.dimensions],typ=ast.typ)
    def visitAutoType(self, ast, param): return self.atomic_t
    def visitVoidType(self, ast, param): return [self.voidtype]