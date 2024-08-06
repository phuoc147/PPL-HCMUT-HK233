import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    
    
    def test_no_entry_point_1(self):
        input = """a: integer;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_no_entry_point_2(self):
        input = """a: function void(){}"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    
    
    ''' def test_func_pass(self):
        input = """
            main: function void() {
                c: auto = { {1 , 2}, { 1,1.5} };
            }
            """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(1.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 4000))
    
    def test_4001(self):
        input = """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a : auto = {{1,2},{goo(),4},{3,4}, b};
                a[4,4] = 1;
                return;
            }
            main:function void() {
                return;
            }
            """
        expect = ""
        
        self.assertTrue(TestChecker.test(input, expect, 4001))
        
    def test_4002(self):
        input = """
            goo: function auto() {}
            foo : function auto(b:auto) {
                a: integer;
                a = printInteger();
            }
            main:function void() {
                return;
            }
            """
        expect = "Type mismatch in expression: FuncCall(printInteger, [])"
        
        self.assertTrue(TestChecker.test(input, expect, 4002)) '''
    
    