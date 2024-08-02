import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):


    ##### TYPES & LITERALS #####
    def test100_atomic_t(self):
        input = """
            x: integer;
            y: float;
        """
        expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 100))

    def test101_auto_decl(self):
        input = """
            x: auto;
            y: string;
        """
        expect = """Program([
	VarDecl(x, AutoType)
	VarDecl(y, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 101))

    def test102_array_types(self):
        input = """x: array [5] of string = {"phuoc","ha"};"""
        expect = """Program([
	VarDecl(x, ArrayType([5], StringType), ArrayLit([StringLit(phuoc), StringLit(ha)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 102))

    def test103_decl(self):
        input = """
            x: integer = 14;
            y: float = 14.7e4;
            z: string = "phuoc_ha_truong";
            t: boolean = true;
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(14))
	VarDecl(y, FloatType, FloatLit(147000.0))
	VarDecl(z, StringType, StringLit(phuoc_ha_truong))
	VarDecl(t, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 103))

    def test104_array_types(self):
        input = """x: array [5] of integer;"""
        expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 104))

    def test105_init(self):
        input = """
            x: auto = 5;
            y: integer = 6;
        """
        expect = """Program([
	VarDecl(x, AutoType, IntegerLit(5))
	VarDecl(y, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input, expect, 105))

    def test106_assign_stmt(self):
        input = """
            main: function void(){
                a = 1;
                b = 1.1;
                c = "c";
                d = false;
            }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), FloatLit(1.1)), AssignStmt(Id(c), StringLit(c)), AssignStmt(Id(d), BooleanLit(False))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 106))

    def test107_assign_with_array_literal(self):
        input = """main: function void(){
            a = {1,2,3,4};
            b = {};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), AssignStmt(Id(b), ArrayLit([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 107))

    def test108_assign_array_literal(self):
        input = """main: function void(){
            a = {1,{2,{3,4}}};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), ArrayLit([IntegerLit(2), ArrayLit([IntegerLit(3), IntegerLit(4)])])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 108))

    def test109_mixedtype_array(self):
        input = """main: function void(){
            a = {"1",2,false,abc,abcd()};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([StringLit(1), IntegerLit(2), BooleanLit(False), Id(abc), FuncCall(abcd, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 109))

#     ##### DECLARATIONS #####
    def test110_short_vardecl(self):
        input = """x: integer;"""
        expect = """Program([
	VarDecl(x, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 110))

    def test111_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 111))

    def test112_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 112))

    def test113_full_vardecl_simple_expr(self):
        input = """x, y, z: integer = a, b, c;"""
        expect = """Program([
	VarDecl(x, IntegerType, Id(a))
	VarDecl(y, IntegerType, Id(b))
	VarDecl(z, IntegerType, Id(c))
])"""
        self.assertTrue(TestAST.test(input, expect, 113))

    def test114_full_vardecl_complex_expr(self):
        input = """x, y, z: integer = hello(), a+5, !b;"""
        expect = """Program([
	VarDecl(x, IntegerType, FuncCall(hello, []))
	VarDecl(y, IntegerType, BinExpr(+, Id(a), IntegerLit(5)))
	VarDecl(z, IntegerType, UnExpr(!, Id(b)))
])"""
        self.assertTrue(TestAST.test(input, expect, 114))

    def test115_empty_funcdecl(self):
        input = """main : function void(){}"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 115))

    def test116_empty_funcdecl(self):
        input = """main : function void(a:integer,b:string,c:boolean){}"""
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType), Param(b, StringType), Param(c, BooleanType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 116))

    def test117_inherit_empty_funcdecl(self):
        input = """main : function void(out a:integer, inherit b:string) inherit supermain{}"""
        expect = """Program([
	FuncDecl(main, VoidType, [OutParam(a, IntegerType), InheritParam(b, StringType)], supermain, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 117))

    def test118_normal_funcdecl(self):
        input = """main : function void(){
                a = a + 14;
                print(a);
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(14))), CallStmt(print, Id(a))]))
])"""
        
        self.assertTrue(TestAST.test(input, expect, 118))

    def test119_inherit_out_funcdecl(self):
        input = """main : function void(inherit out c: float) inherit supermain{}"""
        expect = """Program([
	FuncDecl(main, VoidType, [InheritOutParam(c, FloatType)], supermain, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 119))

    def test120_mixeddecl1(self):
        input = """x: integer = 1;
        main : function void(){
            x = x+1;
            }"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), BinExpr(+, Id(x), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 120))

    def test121_mixeddecl2(self):
        input = """x: integer;
        main : function void(){
            x: float = 2.0;
            }"""
        expect = """Program([
	VarDecl(x, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, FloatType, FloatLit(2.0))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 121))

    def test122_mixeddecl3(self):
        input = """
        sum: function integer(x: integer, y:integer){
            return x+y;
        }
        main : function void(){
            x: integer = sum(1,2);
            }"""
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(x, IntegerType), Param(y, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(x), Id(y)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FuncCall(sum, [IntegerLit(1), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 122))

    def test123_mixeddecl4(self):
        input = """x: array [2] of integer = {1,2};
        main : function void(){
            x = {1,2,3};
            }"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 123))

    def test124_mixeddecl5(self):
        input = """x: array [2] of integer = {1,2};
        main : function void(x: auto){
            print(x);
            return;
            }"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	FuncDecl(main, VoidType, [Param(x, AutoType)], None, BlockStmt([CallStmt(print, Id(x)), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 124))

    ##### EXPRESSIONS #####
    def test125_empty_call_expr(self):
        input = """
        main: function void (){
            hello();
            good_boy();
            are_you_ok();
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, ), CallStmt(good_boy, ), CallStmt(are_you_ok, )]))
])"""

        self.assertTrue(TestAST.test(input, expect, 125))

    def test126_index_1D_ops(self):
        input = """
        main: function void (){
            a[0] = 5;
            b[1] = "string";
            c[3] = 0.5e6;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(5)), AssignStmt(ArrayCell(b, [IntegerLit(1)]), StringLit(string)), AssignStmt(ArrayCell(c, [IntegerLit(3)]), FloatLit(500000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 126))

    def test127_index_ND_ops(self):
        input = """
        main: function void (){
            b[0,1] = "string";
            c[1,2,3] = 0.5e6;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(b, [IntegerLit(0), IntegerLit(1)]), StringLit(string)), AssignStmt(ArrayCell(c, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), FloatLit(500000.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 127))

    def test128_param_lit_call_expr(self):
        input = """
        main: function void (){
            hello(1);
            good_boy("Sang","Kha");
            are_you_ok(true);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, IntegerLit(1)), CallStmt(good_boy, StringLit(Sang), StringLit(Kha)), CallStmt(are_you_ok, BooleanLit(True))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 128))

    def test129_param_id_call_expr(self):
        input = """
        main: function void (){
            hello(a);
            good_boy(b,e);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, Id(a)), CallStmt(good_boy, Id(b), Id(e))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 129))

    def test130_nested_func_call(self):
        input = """
        main: function auto (){
            func(func(),5,foo());
        }"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([CallStmt(func, FuncCall(func, []), IntegerLit(5), FuncCall(foo, []))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 130))

    def test131_unary_operator(self):
        input = """
        main: function void (){
            a = -4;
            a = --4;
            a = !true;
            a = b[5];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, IntegerLit(4))), AssignStmt(Id(a), UnExpr(-, UnExpr(-, IntegerLit(4)))), AssignStmt(Id(a), UnExpr(!, BooleanLit(True))), AssignStmt(Id(a), ArrayCell(b, [IntegerLit(5)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 131))

    def test132_nested_array(self):
        input = """
        main: function void (){
            a = {1,2,3,{4,5,6}};
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 132))

    def test133_multivar_array(self):
        input = """
        main: function void (){
            b = a[1,2,3];
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(b), ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 133))

    def test134_binary_operator(self):
        input = """
        main: function void (){
            a = 1*b;
            a = true && false;
            a = a==b;
            a = a!=b;
            a = (a::b);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(*, IntegerLit(1), Id(b))), AssignStmt(Id(a), BinExpr(&&, BooleanLit(True), BooleanLit(False))), AssignStmt(Id(a), BinExpr(==, Id(a), Id(b))), AssignStmt(Id(a), BinExpr(!=, Id(a), Id(b))), AssignStmt(Id(a), BinExpr(::, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 134))

    def test135_complex_binary_operator(self):
        input = """
        main: function void (){
            a = a*b*c + a/b/c;
            a = a + b%c + d;
            a = a&&b||a;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, BinExpr(*, BinExpr(*, Id(a), Id(b)), Id(c)), BinExpr(/, BinExpr(/, Id(a), Id(b)), Id(c)))), AssignStmt(Id(a), BinExpr(+, BinExpr(+, Id(a), BinExpr(%, Id(b), Id(c))), Id(d))), AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 135))

    def test136_complex_binary_operator_with_paren1(self):
        input = """
        main: function void (){
            a = a*b*(c+a)/b/c;
            a = a + (b%c + d);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(/, BinExpr(/, BinExpr(*, BinExpr(*, Id(a), Id(b)), BinExpr(+, Id(c), Id(a))), Id(b)), Id(c))), AssignStmt(Id(a), BinExpr(+, Id(a), BinExpr(+, BinExpr(%, Id(b), Id(c)), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 136))

    def test137_complex_binary_operator_with_paren2(self):
        input = """
        main: function void (){
            a = (a&&b) || (a>=b && b);
            a = (a + (-b - c*(d+e)))*5;
            a = a::((b::c)::d);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(a), Id(b)), BinExpr(>=, Id(a), BinExpr(&&, Id(b), Id(b))))), AssignStmt(Id(a), BinExpr(*, BinExpr(+, Id(a), BinExpr(-, UnExpr(-, Id(b)), BinExpr(*, Id(c), BinExpr(+, Id(d), Id(e))))), IntegerLit(5))), AssignStmt(Id(a), BinExpr(::, Id(a), BinExpr(::, BinExpr(::, Id(b), Id(c)), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 137))

    def test138_numeric_left_to_right(self):
        input = """
        main: function void (){
            a = b*c/d%e;
            a = b+c-d+e;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(%, BinExpr(/, BinExpr(*, Id(b), Id(c)), Id(d)), Id(e))), AssignStmt(Id(a), BinExpr(+, BinExpr(-, BinExpr(+, Id(b), Id(c)), Id(d)), Id(e)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 138))

    def test139_logic_left_to_right(self):
        input = """
        main: function void (){
            a = b&&c||d;
            a = b||c&&d;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BinExpr(&&, Id(b), Id(c)), Id(d))), AssignStmt(Id(a), BinExpr(&&, BinExpr(||, Id(b), Id(c)), Id(d)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 139))

    def test140_relational_nonassoc(self):
        input = """
        main: function void (){
            a = b&&c;
            a = b!=c;
            a = b>=c;
            a = b<=c;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(&&, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(!=, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(>=, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(<=, Id(b), Id(c)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 140))

    def test141_string_nonassoc(self):
        input = """
        main: function void (){
            a = b::c;
            a = b::(c::d);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(::, Id(b), Id(c))), AssignStmt(Id(a), BinExpr(::, Id(b), BinExpr(::, Id(c), Id(d))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 141))

    def test142_funccall(self):
        input = """
        main: function void (){
            t = getA(a) :: getB(b);
            x: integer = getX(x);
            a[1] = getA1(a[0]);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(t), BinExpr(::, FuncCall(getA, [Id(a)]), FuncCall(getB, [Id(b)]))), VarDecl(x, IntegerType, FuncCall(getX, [Id(x)])), AssignStmt(ArrayCell(a, [IntegerLit(1)]), FuncCall(getA1, [ArrayCell(a, [IntegerLit(0)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 142))

    def test143_full_order1(self):
        input = """
        main: function void (){
            a = -7+6/3/2*3-4%2;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(-, BinExpr(+, UnExpr(-, IntegerLit(7)), BinExpr(*, BinExpr(/, BinExpr(/, IntegerLit(6), IntegerLit(3)), IntegerLit(2)), IntegerLit(3))), BinExpr(%, IntegerLit(4), IntegerLit(2))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 143))

    def test144_full_order2(self):
        input = """
        main: function void (){
            a = (-a + !b) * e[6] && b  >= 6;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(>=, BinExpr(&&, BinExpr(*, BinExpr(+, UnExpr(-, Id(a)), UnExpr(!, Id(b))), ArrayCell(e, [IntegerLit(6)])), Id(b)), IntegerLit(6)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 144))

#     ##### STATEMENTS #####
    def test145_scalar_asm(self):
        input = """
        main: function void (){
            a = 14;
            b = "ez";
            c = .2e-3;
            d = {a,b,c,d};
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(14)), AssignStmt(Id(b), StringLit(ez)), AssignStmt(Id(c), FloatLit(0.0002)), AssignStmt(Id(d), ArrayLit([Id(a), Id(b), Id(c), Id(d)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 145))

    def test146_indexops_asm(self):
        input = """
        main: function void (){
            a[0] = 2;
            a[1,2,3] = 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(2)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 146))

    def test147_complex_asm(self):
        input = """
        main: function void (){
            a[0] = func(1,2,"3");
            a[1,2] = omg(omg(1));
            ez = ez*2 + 6*(7-func());
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(0)]), FuncCall(func, [IntegerLit(1), IntegerLit(2), StringLit(3)])), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), FuncCall(omg, [FuncCall(omg, [IntegerLit(1)])])), AssignStmt(Id(ez), BinExpr(+, BinExpr(*, Id(ez), IntegerLit(2)), BinExpr(*, IntegerLit(6), BinExpr(-, IntegerLit(7), FuncCall(func, [])))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 147))

    def test148_normal_if(self):
        input = """
        main: function void (){
            if(check_float("2.12")==true){
                printString("float");
            }
            else{
                printString("Not float");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(check_float, [StringLit(2.12)]), BooleanLit(True)), BlockStmt([CallStmt(printString, StringLit(float))]), BlockStmt([CallStmt(printString, StringLit(Not float))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 148))

    def test149_if_sequence(self):
        input = """
        main: function void (){
            if(a){
            }
            else if (b){
            }
            else{
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(a), BlockStmt([]), IfStmt(Id(b), BlockStmt([]), BlockStmt([])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 149))

    def test150_if_nested(self):
        input = """
        main: function void (){
            if(calc_score(score)==9){
                printString("idolll :3");
            }
            else {
                if (calc_score(score)==5){
                    printString("vua du qua mon :))");
                }
                else{
                    printString("doan xem");
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, FuncCall(calc_score, [Id(score)]), IntegerLit(9)), BlockStmt([CallStmt(printString, StringLit(idolll :3))]), BlockStmt([IfStmt(BinExpr(==, FuncCall(calc_score, [Id(score)]), IntegerLit(5)), BlockStmt([CallStmt(printString, StringLit(vua du qua mon :))))]), BlockStmt([CallStmt(printString, StringLit(doan xem))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 150))

    def test151_if_nested(self):
        input = """
        main: function void (){
            if(rich==true){
                if(nice==true){
                    setState("kind and rich");
                }
                else setState("unkind and rich");
            } 
            else setState("not rich");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(rich), BooleanLit(True)), BlockStmt([IfStmt(BinExpr(==, Id(nice), BooleanLit(True)), BlockStmt([CallStmt(setState, StringLit(kind and rich))]), CallStmt(setState, StringLit(unkind and rich)))]), CallStmt(setState, StringLit(not rich)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 151))

    def test152_if(self):
        input = """
        main: function void (){
            if(happy) setHappy(true);
            else setHappy(false);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(Id(happy), CallStmt(setHappy, BooleanLit(True)), CallStmt(setHappy, BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 152))

    def test153_if_oneline_nested(self):
        input = """
        main: function void (){
            if(rich==true)
                if(nice==true)
                    setState("kind and rich");
                else setState("unkind and rich");
            else setState("not rich");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(rich), BooleanLit(True)), IfStmt(BinExpr(==, Id(nice), BooleanLit(True)), CallStmt(setState, StringLit(kind and rich)), CallStmt(setState, StringLit(unkind and rich))), CallStmt(setState, StringLit(not rich)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 153))

    def test154_loop(self):
        input = """
        main: function void (){
            for(i=get_started(),i<=5,i+2){
                printInteger("Yoooo!");
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(get_started, [])), BinExpr(<=, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([CallStmt(printInteger, StringLit(Yoooo!))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 154))

    def test155_nested_loop(self):
        input = """
        main: function void (){
            for(i=get_started(), i<5*2, i+2){
                for(j=get_started(), j<5*2, j+1){
                    printInteger(i+j);
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), FuncCall(get_started, [])), BinExpr(<, Id(i), BinExpr(*, IntegerLit(5), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ForStmt(AssignStmt(Id(j), FuncCall(get_started, [])), BinExpr(<, Id(j), BinExpr(*, IntegerLit(5), IntegerLit(2))), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printInteger, BinExpr(+, Id(i), Id(j)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 155))

    def test156_normal_while(self):
        input = """
        main: function void (){
            while(a<5){
                printInteger(a);
                a = a+1;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(5)), BlockStmt([CallStmt(printInteger, Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 156))

    def test157_nested_while(self):
        input = """
        main: function void (){
            a: integer = 0;
            while(match(a)<10){
                printInteger(a);
                while(match(a)*match(a)<69)
                    printInteger(10-a);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(<, FuncCall(match, [Id(a)]), IntegerLit(10)), BlockStmt([CallStmt(printInteger, Id(a)), WhileStmt(BinExpr(<, BinExpr(*, FuncCall(match, [Id(a)]), FuncCall(match, [Id(a)])), IntegerLit(69)), CallStmt(printInteger, BinExpr(-, IntegerLit(10), Id(a))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 157))

    def test158_dowhile(self):
        input = """
        main: function void (){
            do {
                a = a+1;
                b = b-1;
            }
            while(a!=b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(b), BinExpr(-, Id(b), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 158))

    def test159_nested_dowhile(self):
        input = """
        main: function void (){
            do{ 
                //a = a+1;
                //i: integer = 0;
                do{
                    printInteger(i);
                    i = i+1;
                }
                while(i<a);
            }
            while(a<10);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([DoWhileStmt(BinExpr(<, Id(i), Id(a)), BlockStmt([CallStmt(printInteger, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 159))
    
    def test160_break_return(self):
        input = """
        main: function void (){
            for(i=1,i<2,i+1){
                if(i==t)
                    break;
                if(i<0)
                    continue;
                else printInteger(i);
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), Id(t)), BreakStmt()), IfStmt(BinExpr(<, Id(i), IntegerLit(0)), ContinueStmt(), CallStmt(printInteger, Id(i)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 160))
    
    def test161_nested_loop(self):
        input = """
        main: function void (){
            for(i=1,i<getMax(),i+1){
                while(true){
                    print("kaka");
                    do{
                        print("kuku");
                    }
                    while(false);
                }
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(getMax, [])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([CallStmt(print, StringLit(kaka)), DoWhileStmt(BooleanLit(False), BlockStmt([CallStmt(print, StringLit(kuku))]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 161))
        
    def test162_loop(self):
        input = """
        main: function void (){
            k: integer = 5;
            for(i=1,i<getMax(),i+1)
                printInteger(i);
            while((k<200) && (k>0))
                k = k + 5;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(k, IntegerType, IntegerLit(5)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), FuncCall(getMax, [])), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i))), WhileStmt(BinExpr(&&, BinExpr(<, Id(k), IntegerLit(200)), BinExpr(>, Id(k), IntegerLit(0))), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(5))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 162))
    
    def test163_func_call(self):
        input = """
        main: function void (){
            hello();
            hello("Sang");
            hello("Sang","Kha");
            hello(hello("Sang"),"Kha");
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(hello, ), CallStmt(hello, StringLit(Sang)), CallStmt(hello, StringLit(Sang), StringLit(Kha)), CallStmt(hello, FuncCall(hello, [StringLit(Sang)]), StringLit(Kha))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 163))

    def test164_nested_call(self):
        input = """
        main: function void (){
            f(f());
            f(f(f(f(f()))));
            f(f(f(f(f(f())))),f(f(f(f(f())))));
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, FuncCall(f, [])), CallStmt(f, FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [])])])])), CallStmt(f, FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [])])])])]), FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [FuncCall(f, [])])])])]))]))
])"""    
        self.assertTrue(TestAST.test(input, expect, 164))
    
    def test165_func_call(self):
        input = """
        main: function void (){   
            f(1*x,_123,"sss"::"aaa",dsa("dsa"),x%5);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f, BinExpr(*, IntegerLit(1), Id(x)), Id(_123), BinExpr(::, StringLit(sss), StringLit(aaa)), FuncCall(dsa, [StringLit(dsa)]), BinExpr(%, Id(x), IntegerLit(5)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 165))
    
    def test166_block(self):
        input = """
        main: function void (){
            {}
            {
                hello();
            }
            {
                a:integer = 1;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([]), BlockStmt([CallStmt(hello, )]), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 166))

    def test167_return(self):
        input = """
            hello: function void(){
                printString("hello");
            }
            one: function integer(x:integer){
                return 1;
            }
        """
        expect = """Program([
	FuncDecl(hello, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(hello))]))
	FuncDecl(one, IntegerType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 167))
    
    def test168_return(self):
        input = """
            isOdd: function boolean(x:integer){
                return x!=0;
            }
            getArr: function array [3] of integer (x:integer){
                return {x,x*2,x*3};
            }
        """
        expect = """Program([
	FuncDecl(isOdd, BooleanType, [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(!=, Id(x), IntegerLit(0)))]))
	FuncDecl(getArr, ArrayType([3], IntegerType), [Param(x, IntegerType)], None, BlockStmt([ReturnStmt(ArrayLit([Id(x), BinExpr(*, Id(x), IntegerLit(2)), BinExpr(*, Id(x), IntegerLit(3))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 168))
    
    def test169_single_if(self):
        input = """
        main: function void (){   
            if(a==1) return 1;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 169))
    
    def test170_empty_loops(self):
        input = """
        main: function void (){   
            for(i=1,i<5,i+1){}
            while(true){}
            do{}while(true);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([])), WhileStmt(BooleanLit(True), BlockStmt([])), DoWhileStmt(BooleanLit(True), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 170))
    
    def test171_idxop_loops(self):
        input = """
        main: function void (){   
            for(a[i]=1,i<5,i+1){}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 171))
    
    def test172_idxop_loops(self):
        input = """
        main: function void (){   
            for(a[i]=1,i<5,i+1){}
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(a, [Id(i)]), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 172))
    
    def test173_dowhile(self):
        input = """
        main: function void (){   
            while(true){
                do{}
                while(true);
            }
            do{
                while(true){}
            }
            while(true);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([]))])), DoWhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 173))
    
    def test174_dowhile(self):
        input = """
        main: function void (){   
            while(true)
                do{}
                while(true);
            do{
                while(true){}
            }
            while(true);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BooleanLit(True), DoWhileStmt(BooleanLit(True), BlockStmt([]))), DoWhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 174))

    ##### MIXED CASES #####
    def test175_simple_program(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 175))

    def test176_more_complex_program(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 176))
    
    def test177_full_decl_program(self):
        input = """
        i: integer = 6;
        main: function void () {
            x: integer = 7;
        }
        j: integer = 8;
        foo: function void () {
            y: integer = 8;
        }
        """
        expect = """Program([
	VarDecl(i, IntegerType, IntegerLit(6))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(7))]))
	VarDecl(j, IntegerType, IntegerLit(8))
	FuncDecl(foo, VoidType, [], None, BlockStmt([VarDecl(y, IntegerType, IntegerLit(8))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 177))
    
    def test178_test_stmt(self):
        input = """main: function void () {
            // cond stmt
            if (a>1){
                a = 1;
            }
            else if (a<1){
                a = 0;
            }
            else{
                a = 0.5;
            }
            // iter stmt
            while(a>0){
                a = a*0.4;
                print(a);
                if (a<1) break;
            }
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(1))]), IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(0))]), BlockStmt([AssignStmt(Id(a), FloatLit(0.5))]))), WhileStmt(BinExpr(>, Id(a), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), BinExpr(*, Id(a), FloatLit(0.4))), CallStmt(print, Id(a)), IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BreakStmt())]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 178))
    
    def test179_test_stmt(self):
        input = """main: function void () {
            a: integer;
            if (a>0)
                for(a=10,a>0,a-1)
                    if (a>5) print("a>5");
                    else continue;
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType), IfStmt(BinExpr(>, Id(a), IntegerLit(0)), ForStmt(AssignStmt(Id(a), IntegerLit(10)), BinExpr(>, Id(a), IntegerLit(0)), BinExpr(-, Id(a), IntegerLit(1)), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), CallStmt(print, StringLit(a>5)), ContinueStmt())))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 179))

    def test180_binary_search(self):
        input = """
            binarySearch: function integer (arr:integer, x:integer, low:integer, high:integer){
                if (low>high) return -1;
                else{
                    mid: integer = (low+high)/2;
                    if (x == arr[mid]) return mid;
                    else if (x > arr[mid]) return binarySearch(arr,x,mid+1,high);
                    else return binarySearch(arr,x,low,mid-1);
                }
            }
        """
        expect = """Program([
	FuncDecl(binarySearch, IntegerType, [Param(arr, IntegerType), Param(x, IntegerType), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>, Id(low), Id(high)), ReturnStmt(UnExpr(-, IntegerLit(1))), BlockStmt([VarDecl(mid, IntegerType, BinExpr(/, BinExpr(+, Id(low), Id(high)), IntegerLit(2))), IfStmt(BinExpr(==, Id(x), ArrayCell(arr, [Id(mid)])), ReturnStmt(Id(mid)), IfStmt(BinExpr(>, Id(x), ArrayCell(arr, [Id(mid)])), ReturnStmt(FuncCall(binarySearch, [Id(arr), Id(x), BinExpr(+, Id(mid), IntegerLit(1)), Id(high)])), ReturnStmt(FuncCall(binarySearch, [Id(arr), Id(x), Id(low), BinExpr(-, Id(mid), IntegerLit(1))]))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 180))

    def test181_interpolation_search(self):
        input = """
            interpolationSearch: function boolean (arr:array [1407] of integer, x:integer, n:integer){
                low: integer = 0;
                high: integer = n-1;
                while((low<=high) && (target>=arr[low]) && (target <=arr[high])){
                    pos:integer = low + (((target - arr[low]) * (high - low)) / (arr[high] - arr[low]));
 
                    // Check if the target element is at the calculated position
                    if( arr[pos] == target){
                        return pos;
                    }
            
                    // If the target element is less than the element at the calculated position, search the left half of the list
                    if(arr[pos] > target){
                        high = pos - 1;
                    }
                    else{
                        // If the target element is greater than the element at the calculated position, search the right half of the list
                        low = pos + 1;
                    }
                }
                return -1;
            }
        """
        expect = """Program([
	FuncDecl(interpolationSearch, BooleanType, [Param(arr, ArrayType([1407], IntegerType)), Param(x, IntegerType), Param(n, IntegerType)], None, BlockStmt([VarDecl(low, IntegerType, IntegerLit(0)), VarDecl(high, IntegerType, BinExpr(-, Id(n), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(&&, BinExpr(<=, Id(low), Id(high)), BinExpr(>=, Id(target), ArrayCell(arr, [Id(low)]))), BinExpr(<=, Id(target), ArrayCell(arr, [Id(high)]))), BlockStmt([VarDecl(pos, IntegerType, BinExpr(+, Id(low), BinExpr(/, BinExpr(*, BinExpr(-, Id(target), ArrayCell(arr, [Id(low)])), BinExpr(-, Id(high), Id(low))), BinExpr(-, ArrayCell(arr, [Id(high)]), ArrayCell(arr, [Id(low)]))))), IfStmt(BinExpr(==, ArrayCell(arr, [Id(pos)]), Id(target)), BlockStmt([ReturnStmt(Id(pos))])), IfStmt(BinExpr(>, ArrayCell(arr, [Id(pos)]), Id(target)), BlockStmt([AssignStmt(Id(high), BinExpr(-, Id(pos), IntegerLit(1)))]), BlockStmt([AssignStmt(Id(low), BinExpr(+, Id(pos), IntegerLit(1)))]))])), ReturnStmt(UnExpr(-, IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 181))

    def test182_selection_sort(self):
        input = """
            selectionSort: function void (out arr:array [1407] of integer, n:integer){
                i, j, min_idx: integer;
                // One by one move boundary of
                // unsorted subarray
                for (i = 0, i < n-1, i+1)
                {
                    // Find the minimum element in
                    // unsorted array
                    min_idx = i;
                    for (j = i+1, j < n, j+1)
                    {
                    if (arr[j] < arr[min_idx])
                        min_idx = j;
                    }
                    // Swap the found minimum element
                    // with the first element
                    if (min_idx!=i)
                        swap(arr[min_idx], arr[i]);
                }
            }
        """
        expect = """Program([
	FuncDecl(selectionSort, VoidType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(min_idx, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(min_idx), Id(i)), ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), Id(n)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(arr, [Id(j)]), ArrayCell(arr, [Id(min_idx)])), AssignStmt(Id(min_idx), Id(j)))])), IfStmt(BinExpr(!=, Id(min_idx), Id(i)), CallStmt(swap, ArrayCell(arr, [Id(min_idx)]), ArrayCell(arr, [Id(i)])))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 182))

    def test183_merge_sort(self):
        input = """
            mergeSort: function void (out arr: array [1407] of integer, start:integer, end:integer){
                if (start >= end)
                    return; // Returns recursively
            
                mid: auto = start + (end - start) / 2;
                mergeSort(arr, start, mid);
                mergeSort(arr, mid + 1, end);
                merge(arr, start, mid, end);
            }
        """
        expect = """Program([
	FuncDecl(mergeSort, VoidType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(start, IntegerType), Param(end, IntegerType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(start), Id(end)), ReturnStmt()), VarDecl(mid, AutoType, BinExpr(+, Id(start), BinExpr(/, BinExpr(-, Id(end), Id(start)), IntegerLit(2)))), CallStmt(mergeSort, Id(arr), Id(start), Id(mid)), CallStmt(mergeSort, Id(arr), BinExpr(+, Id(mid), IntegerLit(1)), Id(end)), CallStmt(merge, Id(arr), Id(start), Id(mid), Id(end))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 183))

    def test184_quick_sort(self):
        input = """
            quickSort: function void (out arr:array [1407] of integer, low:integer, high:integer){
                if (low < high) {
                    /* pi is partitioning index, arr[p] is now
                    at right place */
                    pi:integer = partition(arr, low, high);
            
                    // Separately sort elements before
                    // partition and after partition
                    quickSort(arr, low, pi - 1);
                    quickSort(arr, pi + 1, high);
                }
            }
        """
        expect = """Program([
	FuncDecl(quickSort, VoidType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(low, IntegerType), Param(high, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<, Id(low), Id(high)), BlockStmt([VarDecl(pi, IntegerType, FuncCall(partition, [Id(arr), Id(low), Id(high)])), CallStmt(quickSort, Id(arr), Id(low), BinExpr(-, Id(pi), IntegerLit(1))), CallStmt(quickSort, Id(arr), BinExpr(+, Id(pi), IntegerLit(1)), Id(high))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 184))

    def test185_heap_sort(self):
        input = """
            heapSort: function void (out arr:array [1407] of integer, n:integer){
                // Build heap (rearrange array)
                for (i = N / 2 - 1, i >= 0, i-1)
                    heapify(arr, N, i);
            
                // One by one extract an element
                // from heap
                for (i = N - 1, i > 0, i-1) {
            
                    // Move current root to end
                    swap(arr[0], arr[i]);
            
                    // call max heapify on the reduced heap
                    heapify(arr, i, 0);
                }
            }
        """
        expect = """Program([
	FuncDecl(heapSort, VoidType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, BinExpr(/, Id(N), IntegerLit(2)), IntegerLit(1))), BinExpr(>=, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), CallStmt(heapify, Id(arr), Id(N), Id(i))), ForStmt(AssignStmt(Id(i), BinExpr(-, Id(N), IntegerLit(1))), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(swap, ArrayCell(arr, [IntegerLit(0)]), ArrayCell(arr, [Id(i)])), CallStmt(heapify, Id(arr), Id(i), IntegerLit(0))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 185))

    def test186_insertion_sort(self):
        input = """
            insertionSort: function void (out arr:array [1407] of integer, n:integer){
                i, key, j: integer;
                for (i = 1, i < n, i+1)
                {
                    key = arr[i];
                    j = i - 1;
            
                    // Move elements of arr[0..i-1], 
                    // that are greater than key, to one
                    // position ahead of their
                    // current position
                    while ((j >= 0) && (arr[j] > key))
                    {
                        arr[j + 1] = arr[j];
                        j = j - 1;
                    }
                    arr[j + 1] = key;
                }
            }
        """
        expect = """Program([
	FuncDecl(insertionSort, VoidType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(key, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(key), ArrayCell(arr, [Id(i)])), AssignStmt(Id(j), BinExpr(-, Id(i), IntegerLit(1))), WhileStmt(BinExpr(&&, BinExpr(>=, Id(j), IntegerLit(0)), BinExpr(>, ArrayCell(arr, [Id(j)]), Id(key))), BlockStmt([AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), ArrayCell(arr, [Id(j)])), AssignStmt(Id(j), BinExpr(-, Id(j), IntegerLit(1)))])), AssignStmt(ArrayCell(arr, [BinExpr(+, Id(j), IntegerLit(1))]), Id(key))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 186))

    def test187_depth_tree(self):
        input = """
            findDepthRec: function integer (out arr:array [1407] of integer, n:integer, out index:integer){
                if ((index >= n) || (tree[index] == "l"))
                    return 0;
            
                // calc height of left subtree (In preorder
                // left subtree is processed before right)
                index=index+1;
                left: integer = findDepthRec(tree, n, index);
            
                // calc height of right subtree
                index=index+1;
                right: integer = findDepthRec(tree, n, index);
            
                return max(left, right) + 1;
            }
            findDepth: function void (out arr:array [1407] of integer, n:integer){
                index: integer = 0;
                return findDepthRec(tree, n, index);
            }
        """
        expect = """Program([
	FuncDecl(findDepthRec, IntegerType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(n, IntegerType), OutParam(index, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(>=, Id(index), Id(n)), BinExpr(==, ArrayCell(tree, [Id(index)]), StringLit(l))), ReturnStmt(IntegerLit(0))), AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), VarDecl(left, IntegerType, FuncCall(findDepthRec, [Id(tree), Id(n), Id(index)])), AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1))), VarDecl(right, IntegerType, FuncCall(findDepthRec, [Id(tree), Id(n), Id(index)])), ReturnStmt(BinExpr(+, FuncCall(max, [Id(left), Id(right)]), IntegerLit(1)))]))
	FuncDecl(findDepth, VoidType, [OutParam(arr, ArrayType([1407], IntegerType)), Param(n, IntegerType)], None, BlockStmt([VarDecl(index, IntegerType, IntegerLit(0)), ReturnStmt(FuncCall(findDepthRec, [Id(tree), Id(n), Id(index)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 187))

    def test188_lcs(self):
        input = """
            lcs: function integer (out X:array [1407] of integer, out Y:array [1407] of integer, n:integer, m:integer){
                if ((m == 0) || (n == 0))
                    return 0;
                if (X[m-1] == Y[n-1])
                    return 1 + lcs(X, Y, m-1, n-1);
                else
                    return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
            }
        """
        expect = """Program([
	FuncDecl(lcs, IntegerType, [OutParam(X, ArrayType([1407], IntegerType)), OutParam(Y, ArrayType([1407], IntegerType)), Param(n, IntegerType), Param(m, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(m), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(0))), ReturnStmt(IntegerLit(0))), IfStmt(BinExpr(==, ArrayCell(X, [BinExpr(-, Id(m), IntegerLit(1))]), ArrayCell(Y, [BinExpr(-, Id(n), IntegerLit(1))])), ReturnStmt(BinExpr(+, IntegerLit(1), FuncCall(lcs, [Id(X), Id(Y), BinExpr(-, Id(m), IntegerLit(1)), BinExpr(-, Id(n), IntegerLit(1))]))), ReturnStmt(FuncCall(max, [FuncCall(lcs, [Id(X), Id(Y), Id(m), BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(lcs, [Id(X), Id(Y), BinExpr(-, Id(m), IntegerLit(1)), Id(n)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 188))

    def test189_spiral_matrix(self):
        input = """
            spiralPrint: function void (out X:array [100,100] of integer, n:integer, m:integer){
                i,k,l:integer = -1,0,0;
                while ((k < m) && (l < n)) {
                    /* Print the first row from the remaining rows */
                    for (i = l, i < n, i+1) {
                        printString(a[k,i]);
                    }
                    k=k+1;
            
                    /* Print the last column from the remaining columns */
                    for (i = k, i < m, i+1) {
                        printString(a[i,n-1]);
                    }
                    n=n-1;
            
                    /* Print the last row from the remaining rows */
                    if (k < m) {
                        for (i = n - 1, i >= l, i-1) {
                            printString(a[m-1,i]);
                        }
                        m=m-1;
                    }
                    /* Print the first column from the remaining columns */
                    if (l < n) {
                        for (i = m - 1, i >= k, i-1) {
                            printString(a[i,l]);
                        }
                        l=l+1;
                    }
                }
            }
        """
        expect = """Program([
	FuncDecl(spiralPrint, VoidType, [OutParam(X, ArrayType([100, 100], IntegerType)), Param(n, IntegerType), Param(m, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(k, IntegerType, IntegerLit(0)), VarDecl(l, IntegerType, IntegerLit(0)), WhileStmt(BinExpr(&&, BinExpr(<, Id(k), Id(m)), BinExpr(<, Id(l), Id(n))), BlockStmt([ForStmt(AssignStmt(Id(i), Id(l)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [Id(k), Id(i)]))])), AssignStmt(Id(k), BinExpr(+, Id(k), IntegerLit(1))), ForStmt(AssignStmt(Id(i), Id(k)), BinExpr(<, Id(i), Id(m)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [Id(i), BinExpr(-, Id(n), IntegerLit(1))]))])), AssignStmt(Id(n), BinExpr(-, Id(n), IntegerLit(1))), IfStmt(BinExpr(<, Id(k), Id(m)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(n), IntegerLit(1))), BinExpr(>=, Id(i), Id(l)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [BinExpr(-, Id(m), IntegerLit(1)), Id(i)]))])), AssignStmt(Id(m), BinExpr(-, Id(m), IntegerLit(1)))])), IfStmt(BinExpr(<, Id(l), Id(n)), BlockStmt([ForStmt(AssignStmt(Id(i), BinExpr(-, Id(m), IntegerLit(1))), BinExpr(>=, Id(i), Id(k)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printString, ArrayCell(a, [Id(i), Id(l)]))])), AssignStmt(Id(l), BinExpr(+, Id(l), IntegerLit(1)))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 189))
        
    def test190_func_empty(self):
        input = "main: function void(){}"
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 190))
    
    def test191_assign(self):
        input = """main: function void(){
                a = 1;
                a = b;
                a[0] = 1;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(a), Id(b)), AssignStmt(ArrayCell(a, [IntegerLit(0)]), IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 191))
        
    def test192_floatlit(self):
        input = """main: function void(){
                a = .e23;
                b = 10.21e2;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), FloatLit(0.0)), AssignStmt(Id(b), FloatLit(1021.0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 192))
    
    def test193_vardecl_single_if(self):
        input = """main: function void(){
                if (n == 1)  {a,b: integer;}
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 193))

    
    def test194_stringlit(self):
        input = """main: function void(){
                a = "abc\txyz";
            }"""
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(abc	xyz))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 194))
    
    def test195_stringlit(self):
        input = r"""main: function void(){
                a = "phuoc\\ha";
            }"""
        expect = r"""Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), StringLit(phuoc\\ha))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 195))
    
    def test196(self):
        input = r"""main: function void(){
                a = -.e23;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(-, FloatLit(0.0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 196))
    
    
    def test197(self):
        input = r"""main: function void(){
                a: auto = 6;
            }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, AutoType, IntegerLit(6))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 197))
        
    def test198(self):
        input = """a: array [3] of integer;""" 
        expect = """Program([
	VarDecl(a, ArrayType([3], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 198))
    def test199(self):
        input = """foo: function void () {
            if(x > 0)
                if(y > 0) {
                    printBoolean(x * y > 0);
                }
                else if (z > 0)
                    printBoolean(x * z > 0);
        }"""
        expect = """Program([
	FuncDecl(foo, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, Id(x), IntegerLit(0)), IfStmt(BinExpr(>, Id(y), IntegerLit(0)), BlockStmt([CallStmt(printBoolean, BinExpr(>, BinExpr(*, Id(x), Id(y)), IntegerLit(0)))]), IfStmt(BinExpr(>, Id(z), IntegerLit(0)), CallStmt(printBoolean, BinExpr(>, BinExpr(*, Id(x), Id(z)), IntegerLit(0))))))]))
])"""

        self.assertTrue(TestAST.test(input, expect, 199))