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

    def replace_with(self, position, item: Token):
        self.token_stream.insert(position, item)

        for i in range(item.token_count):
            del self.token_stream[position+1]

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
            super(Matcher.WhatTheHellManException, self).__init__(pointer)

    # Let's define primary words and singletons here. Order defines order of significance
    @staticmethod
    def match_primary_keyword(tokenizer: Tokenizer):
        tokens = [token for token in [
            HackersDelightMatcher.match(tokenizer),
            IntegerMatcher.match(tokenizer)
        ] if token]

        return tokens[0] if tokens else False

    # Here are all indicator keyword matchers. For order same goes as above
    @staticmethod
    def match_indicator_keyword(order, pointer, tokenizer: Tokenizer):
        tokens = [token for token in [
            MovePointerMatcher.match(tokenizer, order, pointer),
            EditCellMatcher.match(tokenizer, order, pointer),
            IONumMatcher.match(tokenizer, order, pointer),
            IOCharMatcher.match(tokenizer, order, pointer)
        ] if token]

        return tokens[0] if tokens else False

    @staticmethod
    def start(tokenizer: Tokenizer):
        token_stream = TokenStream([])

        while not tokenizer.reached_end():
            word_start_pointer = tokenizer.pointer_at()
            token = Matcher.match_primary_keyword(tokenizer)

            if isinstance(token, HackersDelightMatcher.WordOrder):
                token = Matcher.match_indicator_keyword(token, word_start_pointer, tokenizer)

            if not token:
                Warnings.add_exception(Matcher.WhatTheHellManException(tokenizer.pointer_at()))
                tokenizer.consume()
            else:
                token_stream.append(token)

        return token_stream
