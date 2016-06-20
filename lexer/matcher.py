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

    def insert(self, position, item):
        self.token_stream.insert(position, item)

    def __iter__(self):
        return self.token_stream

    def __len__(self):
        return len(self.token_stream)

    def __getitem__(self, item):
        return self.token_stream[item]

    def __eq__(self, other):
        return self.token_stream == other.token_stream


class Matcher:
    class WhatTheHellManException(HackersException):
        def __init__(self, pointer):
            super.__init__(pointer)

    # Let's define primary words and singletons here. Order defines order of significance
    @staticmethod
    def match_primary_keyword(tokenizer: Tokenizer):
        return [token for token in [
            HackersDelightMatcher.match(tokenizer),
            IntegerMatcher.match(tokenizer)
        ] if token][0]

    # Here are all indicator keyword matchers. For order same goes as above
    @staticmethod
    def match_indicator_keyword(order, tokenizer: Tokenizer):
        return [token for token in [
            MovePointerMatcher.match(tokenizer, order),
            EditCellMatcher.match(tokenizer, order),
            IONumMatcher.match(tokenizer, order),
            IOCharMatcher.match(tokenizer, order)
        ] if token][0]

    @staticmethod
    def start(tokenizer: Tokenizer):
        token_stream = TokenStream([])

        while not tokenizer.reached_end():
            token = Matcher.match_primary_keyword(tokenizer)

            if isinstance(token, HackersDelightMatcher.WordOrder):
                token = Matcher.match_indicator_keyword(token, tokenizer)

            if not token:
                Warnings.add_exception(Matcher.WhatTheHellManException(tokenizer.pointer_at()))
                tokenizer.consume()
            else:
                token_stream.append(token)

        return token_stream
