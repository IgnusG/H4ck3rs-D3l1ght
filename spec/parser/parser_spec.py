import unittest

from parser.complex_tokens import *
from lexer.matcher import TokenStream
from parser.parser import Parser


class TestParserStream(unittest.TestCase):

    def test_direct_input_stream(self):
        tokenstream_oracle = TokenStream([InputNumDirect(Integer(0, 111), InputNumCell(3))])
        actual_tokenstream = Parser.start(TokenStream([Integer(0, 111), InputNumCell(3)]))
        self.assertSequenceEqual(actual_tokenstream, tokenstream_oracle)

    def test_direct_output_stream(self):
        tokenstream_oracle = TokenStream([OutputNumDirect(Integer(0, 2223), OutputNumCell(4))])
        actual_tokenstream = Parser.start(TokenStream([Integer(0, 2223), OutputNumCell(4)]))
        self.assertSequenceEqual(actual_tokenstream, tokenstream_oracle)

    def test_condition_stream(self):
        tokentream_oracle = TokenStream([IncrementCell(0), ConditionalStatement(Condition(3), [PointerRight(6)]), OutputNumCell(12)])
        actual_tokenstream = Parser.start(TokenStream([IncrementCell(0), Condition(3), PointerRight(6), JumpBack(9), OutputNumCell(12)]))
        self.assertSequenceEqual(actual_tokenstream, tokentream_oracle)

    def test_nested_condition_stream(self):
        tokentream_oracle = TokenStream([IncrementCell(0), ConditionalStatement(Condition(3), [PointerRight(6), ConditionalStatement(Condition(9), [PointerLeft(12)])]), OutputNumCell(21)])
        actual_tokenstream = Parser.start(TokenStream([IncrementCell(0), Condition(3), PointerRight(6), Condition(9), PointerLeft(12), JumpBack(15), JumpBack(18), OutputNumCell(21)]))
        self.assertSequenceEqual(actual_tokenstream, tokentream_oracle)
