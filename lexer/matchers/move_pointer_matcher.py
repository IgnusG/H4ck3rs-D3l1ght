from lexer.definitions.tokens import PointerLeft
from lexer.definitions.tokens import PointerRight
from lexer.tokenizer import Tokenizer

from lexer.definitions.keywords import Keywords
from .hackersdelight_matcher import HackersDelightMatcher


class MovePointerMatcher:
    @staticmethod
    def match(tokenizer: Tokenizer, baseword_order: HackersDelightMatcher.WordOrder):
        tokenizer.take_snapshot()

        if tokenizer.consume() == Keywords.MV_PTR:
            if baseword_order == HackersDelightMatcher.WordOrder.HD:
                return PointerRight()
            elif baseword_order == HackersDelightMatcher.WordOrder.DH:
                return PointerLeft()
        else:
            tokenizer.rollback_snapshot()
            return False
