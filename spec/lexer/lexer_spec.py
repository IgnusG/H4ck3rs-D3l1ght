import unittest

from lexer.definitions.tokens import *
from lexer.lexer import Lexer
from lexer.matcher import TokenStream


class TestLexerStream(unittest.TestCase):

    def test_move_pointer_stream(self):
        tokenstream_oracle = TokenStream([PointerRight(0), PointerLeft(15)])
        actual_tokenstream = Lexer.start('H4ck3rs Delight. Del1ghtH4ck3rs.')
        self.assertEqual(actual_tokenstream, tokenstream_oracle)

    def test_edit_cell_stream(self):
        tokenstream_oracle = TokenStream([IncrementCell(0), IncrementCell(15),
                                          IncrementCell(18), DecrementCell(21)])
        actual_tokenstream = Lexer.start('H4ck3rs Delight! HD! HD! Del1ghtH4ck3rs!')
        self.assertEqual(actual_tokenstream, tokenstream_oracle)

    def test_io_num_stream(self):
        tokenstream_oracle = TokenStream([OutputNumCell(0), InputNumCell(15)])
        actual_tokenstream = Lexer.start('H4ckers Del1ght= DH=')
        self.assertEqual(actual_tokenstream, tokenstream_oracle)

    def test_io_char_stream(self):
        tokenstream_oracle = TokenStream([OutputCharCell(0), InputCharCell(3), OutputCharCell(18)])
        actual_tokenstream = Lexer.start('HD@ Del1ghtH4ckers@ HD@')
        self.assertEqual(actual_tokenstream, tokenstream_oracle)

    def test_integer_stream(self):
        tokenstream_oracle = TokenStream([Integer(0, 152), InputCharCell(3), Integer(6, 546)])
        actual_tokenstream = Lexer.start('152 DH@   546')
        self.assertEqual(actual_tokenstream, tokenstream_oracle)

    def test_separate_integers_as_one_stream(self):
        tokenstream_oracle = TokenStream([Integer(0, 152546)])
        actual_tokenstream = Lexer.start('152          546')
        self.assertEqual(actual_tokenstream, tokenstream_oracle)
