from lexer.classes.definitions.tokens import PointerLeft
from lexer.classes.definitions.tokens import PointerRight
from lexer.classes.tokenizer import Tokenizer
from lexer.classes.definitions.keywords import Keywords
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
