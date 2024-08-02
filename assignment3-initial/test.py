from test1 import *

def union2_ListType(lst1:list,lst2:list,implicit,ordered = False)->list:
    new_lst1 = []
    new_lst2 = []
    for x in lst1:
        for y in lst2:
            if type(x) == type(y):
                if not(x in new_lst1): new_lst1.append(x)
                if not(y in new_lst2): new_lst2.append(y)
            else:
                if implicit != None:
                    if x in implicit and y in implicit and ((ordered and implicit.index(x) <= implicit.index(y)) or not ordered):
                        if not(x in new_lst1): new_lst1.append(x)
                        if not(y in new_lst2): new_lst2.append(y)
    return new_lst1,new_lst2
def inferType(op1,op2,typ,rettype,expr,implicit ) :
        op1_auto = True if isinstance(op1[0],AutoType) else False
        op2_auto = True if isinstance(op2[0],AutoType) else False
        tmp1,tmp2 = op1,op2
        op1 = op1 if not(op1_auto) else typ if op1[2] == [] else op1[2]
        op2 = op2 if not(op2_auto) else typ if op2[2] == [] else op2[2]
        typ_tmp,ret= union2_ListType(typ,rettype,implicit,True) 
        if implicit: 
            if typ_tmp == []: raise Exception(expr)
            else: typ = typ_tmp

        print("typ",typ)
        op1,op1_typ = union2_ListType(op1,typ,implicit,True)
        op2,op2_typ = union2_ListType(op2,typ,implicit,True)
        op1,op2 = union2_ListType(op1,op2,implicit)
        print("op1",op1)
        print("op2",op2)
        ret_empty = True if ret == [] else False
        if op1 == [] or op2 == []: raise Exception(expr)
        if not op1_auto: tmp1 = op1.copy()
        else: tmp1[2] = op1
        if not op2_auto: tmp2 = op2.copy()
        else: tmp2[2] = op2
        if ret == []: return rettype
        else: return ret
int_ = Int()
float_ = Float()
boolean_ = Boolean()
string_ = String()
l1 = [int_]
l2 = [int_,float_]
result = union2_ListType([string_],[float_],[int_,float_],True)
print(l1)
print(l2)
print(result)
