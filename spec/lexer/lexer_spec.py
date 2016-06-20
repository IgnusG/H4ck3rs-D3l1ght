import unittest

from lexer.definitions.tokens import PointerRight, PointerLeft
from lexer.lexer import Lexer
from lexer.matcher import TokenStream


class TestLexer(unittest.TestCase):
    def test_lexer_stream(self):
        self.assertEqual(Lexer.start('H4ck3rs Delight. Del1ghtH4ck3rs.'),
                         TokenStream([PointerRight(0), PointerLeft(15)]))
