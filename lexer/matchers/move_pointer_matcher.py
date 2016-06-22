from lexer.definitions.tokens import PointerLeft
from lexer.definitions.tokens import PointerRight
from lexer.tokenizer import Tokenizer

from lexer.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class MovePointerMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder, pointer):
        tokenizer.take_snapshot()

        if not tokenizer.reached_end() and tokenizer.consume() == Keywords.MV_PTR:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return PointerRight(pointer)
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return PointerLeft(pointer)
        else:
            tokenizer.rollback_snapshot()
            return False
