from lexer.definitions.tokens import InputCharCell
from lexer.definitions.tokens import OutputCharCell
from lexer.tokenizer import Tokenizer

from lexer.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class IOCharMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder, pointer):
        tokenizer.take_snapshot()

        if not tokenizer.reached_end() and tokenizer.consume() == Keywords.IO_CHAR:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return OutputCharCell(pointer)
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return InputCharCell(pointer)
        else:
            tokenizer.rollback_snapshot()
            return False
