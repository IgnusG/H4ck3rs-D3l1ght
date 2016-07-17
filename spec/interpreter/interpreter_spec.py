import unittest
from interpreter.interpreter import Interpreter


class InterpreterTest(unittest.TestCase):

    def setUp(self):
        Interpreter.reset_storage()

    def test_interpreter_basic_output(self):
        user_input = 'HD! HD!    HD='
        self.assertEqual(Interpreter.run_interpreter(user_input), '2')

    def test_interpreter_hello_world(self):
        user_input = '72 H4ck3rs D3l1ght@ 101 H4ck3rs D3l1ght@ 108 D3l1ght H4ck3rs= H4ck3rs D3l1ght@ H4ck3rs D3l1ght@ H4ck3rs D3l1ght. 111 D3l1ght H4ck3rs= H4ck3rs D3l1ght@  32 H4ck3rs D3l1ght@  87 H4ck3rs D3l1ght@ H4ck3rs D3l1ght@ 114 H4ck3rs D3l1ght@ D3l1ght H4ck3rs. H4ck3rs D3l1ght@ 100 H4ck3rs D3l1ght@ 33 H4ck3rs D3l1ght@'
        self.assertEqual(Interpreter.run_interpreter(user_input), 'Hello World!')

    def test_interpreter_conditions(self):
        user_input = 'HD! HD! HD! HD? HD= DH! DH? HD! HD='
        self.assertEqual(Interpreter.run_interpreter(user_input), '3211')

    def test_interpreter_nested_conditions(self):
        user_input = 'HD! HD! HD! HD? HD= DH! HD. HD! HD! HD? HD= DH! DH? DH. DH?'
        self.assertEqual(Interpreter.run_interpreter(user_input), '321221121')
