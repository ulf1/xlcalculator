
# Excel reference: https://support.office.com/en-us/article/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568

import unittest

import pandas as pd

from koala_xlcalculator.function_library import PMT
from koala_xlcalculator.koala_types import XLCell
from koala_xlcalculator.exceptions import ExcelError
from koala_xlcalculator import ModelCompiler
from koala_xlcalculator import Evaluator


class TestPMT(unittest.TestCase):

    def setUp(self):
        compiler = ModelCompiler()
        self.model = compiler.read_and_parse_archive(r"./tests/resources/PMT.xlsx")
        self.model.build_code()
        self.evaluator = Evaluator(self.model)

    # def teardown(self):
    #     pass


    def test_pmt_basic(self):
        self.assertEqual(round(PMT.pmt(0.08/12, 10, 10000), 2), -1037.03)


    @unittest.skip("""Problem evalling: unsupported operand type(s) for +: 'int' and 'ExcelError' for Sheet1!A1, PMT.pmt(Evaluator.apply("divide",self.eval_ref("Sheet1!A2"),12,None),self.eval_ref("Sheet1!A3"),self.eval_ref("Sheet1!A4"))""")
    def test_evaluation_A1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!A1')
        value = self.evaluator.evaluate('Sheet1!A1')
        self.assertEqual( excel_value, value )


    @unittest.skip("""Problem evalling: unsupported operand type(s) for +: 'int' and 'ExcelError' for Sheet1!B1, PMT.pmt(Evaluator.apply("divide",self.eval_ref("Sheet1!A2"),12,None),self.eval_ref("Sheet1!A3"),self.eval_ref("Sheet1!A4"))""")
    def test_evaluation_B1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!B1')
        value = self.evaluator.evaluate('Sheet1!B1')
        self.assertEqual( excel_value, value )


    @unittest.skip("""Problem evalling: unsupported operand type(s) for +: 'int' and 'ExcelError' for Sheet1!C1, PMT.pmt(Evaluator.apply("divide",self.eval_ref("Sheet1!A12"),12,None),Evaluator.apply("multiply",self.eval_ref("Sheet1!A13"),12,None),0,self.eval_ref("Sheet1!A14"))""")
    def test_evaluation_C1(self):
        excel_value = self.evaluator.get_cell_value('Sheet1!C1')
        value = self.evaluator.evaluate('Sheet1!C1')
        self.assertEqual( excel_value, value )