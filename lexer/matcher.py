from lexer.definitions.tokens import Token
from lexer.matchers.edit_cell_matcher import EditCellMatcher
from lexer.matchers.hackersdelight_matcher import HackersDelightMatcher
from lexer.matchers.integer_matcher import IntegerMatcher
from lexer.matchers.io_num_matcher import IONumMatcher
from lexer.matchers.move_pointer_matcher import MovePointerMatcher
from lexer.tokenizer import Tokenizer
from lexer.warnings import Warnings

from helpers.error_handling import HackersException
from lexer.matchers.io_char_matcher import IOCharMatcher


class TokenStream:
    def __init__(self, init: [Token]):
        self.token_stream = init

    def append(self, item):
        self.token_stream.append(item)


class Matcher:
    class WhatTheHellManException(HackersException):
        def __init__(self, pointer):
            super.__init__(pointer)

    @staticmethod
    def start(tokenizer: Tokenizer):
        token_stream = TokenStream([])

        while not tokenizer.reached_end():
            token = [token for token in [
                HackersDelightMatcher.match(tokenizer),
                IntegerMatcher.match(tokenizer)
            ] if token][0]

            if isinstance(token, HackersDelightMatcher.WordOrder):
                token = [token for token in [
                    MovePointerMatcher.match(tokenizer, token),
                    EditCellMatcher.match(tokenizer, token),
                    IONumMatcher.match(tokenizer, token),
                    IOCharMatcher.match(tokenizer, token)
                ] if token][0]

            if not token:
                Warnings.add_exception(Matcher.WhatTheHellManException(tokenizer.pointer_at()))
                tokenizer.consume()
            else:
                token_stream.append(token)

        return token_stream
