import unittest

from parser.complex_tokens import *
from lexer.matcher import TokenStream
from parser.parser import Parser


class TestParserStream(unittest.TestCase):

    def test_direct_input_stream(self):
        tokenstream_oracle = TokenStream([InputNumDirect(Integer(0, 111), InputNumCell(3))])
        actual_tokenstream = Parser.start(TokenStream([Integer(0, 111), InputNumCell(3)]))
        self.assertEqual(actual_tokenstream, tokenstream_oracle)

    def test_direct_output_stream(self):
        tokenstream_oracle = TokenStream([OutputNumDirect(Integer(0, 2223), OutputNumCell(4))])
        actual_tokenstream = Parser.start(TokenStream([Integer(0, 2223), OutputNumCell(4)]))
        self.assertEqual(actual_tokenstream, tokenstream_oracle)
