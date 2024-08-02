import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_435(self):
        self.assertTrue(TestChecker.test(
            """
            goo: function auto() {}
            add: function float(a:auto,b:auto){
                return a + b;
            }
            foo : function auto(a:auto,e:auto) {
                b: auto = 2 + a;
            }
            main:function void() {
            
            }
        """, 
            """Type mismatch in statement: AssignStmt(Id(b), StringLit(string))""", 
            435))