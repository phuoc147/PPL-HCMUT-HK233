import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """"""
        input = """a;b"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

