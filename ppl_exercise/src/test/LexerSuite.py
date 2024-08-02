import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_real(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("1111_2","1111_2,<EOF>",101))
