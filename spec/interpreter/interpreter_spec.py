import unittest
from io import StringIO
import builtins

from interpreter.interpreter import Interpreter


class InterpreterTest(unittest.TestCase):
    original_input = builtins.input

    @staticmethod
    def mock_input(input_array):
        def mock_input():
            counter = [0]
            input_array.append('')

            def wrapper():
                value = input_array[counter[0]]
                counter[0] += 1
                return value
            return wrapper

        builtins.input = mock_input()

    def tearDown(self):
        builtins.input = InterpreterTest.original_input

    # TODO: I'll kill you if you don't reformat this before due
    def test_interpreter_basic_output(self):
        InterpreterTest.mock_input(['HD! HD!    HD='])
        out = StringIO()
        Interpreter.start(out)
        self.assertEqual(out.getvalue(), '2')

    def test_interpreter_hello_world(self):
        InterpreterTest.mock_input(['72 H4ck3rs D3l1ght@ 101 H4ck3rs D3l1ght@ 108 D3l1ght H4ck3rs= H4ck3rs D3l1ght@ H4ck3rs D3l1ght@ H4ck3rs D3l1ght. 111 D3l1ght H4ck3rs= H4ck3rs D3l1ght@  32 H4ck3rs D3l1ght@  87 H4ck3rs D3l1ght@ H4ck3rs D3l1ght@ 114 H4ck3rs D3l1ght@ D3l1ght H4ck3rs. H4ck3rs D3l1ght@ 100 H4ck3rs D3l1ght@ 33 H4ck3rs D3l1ght@'])
        out = StringIO()
        Interpreter.start(out)
        self.assertEqual(out.getvalue(), 'Hello World!')
