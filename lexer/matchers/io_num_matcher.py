from lexer.definitions.tokens import InputNumCell
from lexer.definitions.tokens import OutputNumCell
from lexer.tokenizer import Tokenizer

from lexer.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class IONumMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.IO_NUM:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return OutputNumCell()
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return InputNumCell()
        else:
            tokenizer.rollback_snapshot()
            return False
